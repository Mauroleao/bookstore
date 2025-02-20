from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import git
import json

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        repo = git.Repo('/home/mauroleao1/bookstore')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Atualizado com sucesso!")
    return HttpResponse("Aguardando requisição POST do GitHub")
