from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            event = request.headers.get('X-GitHub-Event')

            if event == 'ping':
                return HttpResponse("Ping event received", status=200)
            else:
                # Your existing logic for handling push events goes here
                # For example:
                # if payload.get('ref') == 'refs/heads/main':
                #     # ... your git pull logic ...
                return HttpResponse("Webhook received", status=200)

        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

    return HttpResponse("Webhook active", status=200)