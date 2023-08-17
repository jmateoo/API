from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def index_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        return render(request, "index.html")