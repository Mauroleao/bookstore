from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import git
import json
import os

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            event = request.headers.get('X-GitHub-Event')

            if event == 'ping':
                return HttpResponse("Ping event received", status=200)
            elif payload.get('ref') == 'refs/heads/main':
                # Path to your repository on PythonAnywhere
                repo_path = '/home/mauroleao1/bookstore'
                try:
                    repo = git.Repo(repo_path)
                    origin = repo.remotes.origin
                    origin.pull()

                    # Reload the WSGI application
                    os.system('touch /var/www/mauroleao1_pythonanywhere_com_wsgi.py')

                    return HttpResponse("Code updated successfully", status=200)
                except Exception as e:
                    return HttpResponse(f"Error pulling code: {str(e)}", status=500)
            else:
                return HttpResponse("Ignoring event", status=200)

        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON payload", status=400)
        except Exception as e:
            return HttpResponse(f"Error processing request: {str(e)}", status=500)

    return HttpResponse("Webhook active", status=200)