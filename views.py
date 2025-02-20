from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import git
import json
import os

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        try:
            # Caminho do repositório no PythonAnywhere
            repo_path = '/home/mauroleao1/bookstore'
            
            # Forçar o pull independente do branch
            repo = git.Repo(repo_path)
            repo.git.reset('--hard')
            repo.git.clean('-f', '-d')
            repo.remotes.origin.pull()
            
            # Recarregar a aplicação
            os.system('touch /var/www/mauroleao1_pythonanywhere_com_wsgi.py')
            
            return HttpResponse("Deploy realizado com sucesso!", status=200)
            
        except Exception as e:
            return HttpResponse(f"Erro no deploy: {str(e)}", status=500)
            
    return HttpResponse("Webhook ativo", status=200)