import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def search_media(request):
    # Handling POST method
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            query = body.get("query")
            media_type = body.get("media_type", "image")  # Default to image if not provided
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)
    
    # Handling GET method
    elif request.method == "GET":
        query = request.GET.get("query")
        media_type = request.GET.get("media_type", "image")  # Default to image if not provided
    else:
        return JsonResponse({"error": "Only GET and POST methods are allowed"}, status=405)

    # Validate if query is provided
    if not query:
        return JsonResponse({"error": "Query is required"}, status=400)

    # Build the Openverse API URL
    url = f"https://api.openverse.org/v1/{media_type}/?q={query}"

    try:
        # Send the GET request to Openverse API
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Will raise an exception for 4xx/5xx errors
    except requests.exceptions.Timeout:
        return JsonResponse({"error": "Openverse API timeout"}, status=504)
    except requests.exceptions.RequestException as e:
        # Handle all other types of exceptions
        return JsonResponse({"error": f"Error fetching data: {str(e)}"}, status=500)

    # Return the data from Openverse API as JSON response
    return JsonResponse(response.json(), safe=False)
