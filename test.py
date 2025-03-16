from django.http import HttpResponse
from django.utils.safestring import mark_safe
import json

def vulnerable_view(request):
    user_input = request.GET.get("name", "Anonymous")

    data = {
        "greeting": f"Hello {user_input}"
    }

    json_data = mark_safe(json.dumps(data))

    html = f"""
    <html>
      <head><title>Demo</title></head>
      <body>
        <h1>Greeting JSON:</h1>
        <pre>{json_data}</pre>
      </body>
    </html>
    """
    return HttpResponse(html)

