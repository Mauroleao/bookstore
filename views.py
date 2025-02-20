from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import git
import json

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        # Parse the GitHub webhook payload
        payload = json.loads(request.body)
        
        # Check if this is a push to the main branch
        if payload.get('ref') == 'refs/heads/main':
            repo = git.Repo('/home/mauroleao1/bookstore')
            origin = repo.remotes.origin
            
            # Fetch and pull the latest changes
            origin.fetch()
            origin.pull()
            
            return HttpResponse("Código atualizado com sucesso!", status=200)
            
        return HttpResponse("Evento recebido mas não é um push para main", status=200)
        
    return HttpResponse("Esperando POST do GitHub", status=200)