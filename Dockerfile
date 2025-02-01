# Use Python 3.12-slim
FROM python:3.12-slim

# Defina variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instale dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    git \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Atualize o pip
RUN pip install --upgrade pip

# Instale o Poetry via pip
RUN pip install poetry

# Adicione o Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Configure o Poetry para não criar ambientes virtuais
RUN poetry config virtualenvs.create false

# Verifique a versão do Poetry
RUN poetry --version

# Defina o diretório de trabalho
WORKDIR /opt/pysetup

# **Copie o código do projeto inteiro antes da instalação das dependências**
COPY . .

# Instale todas as dependências (incluindo dev)
RUN poetry install --with dev

# Colete arquivos estáticos
RUN poetry run python manage.py collectstatic --noinput

# Comando para executar o servidor
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
