from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User
# Create your views here.

data_structure = [
    [{'user_name': 'Tom', 'age': 25}],
]

@csrf_exempt
def http_server(request):
    if request.method == 'GET':
        return JsonResponse(data_structure, status=200)
    
    elif request.method == 'POST':
        text = request.body
        
        print()
        print(text)
        print(type(text))
        print()

        get_data = json.loads(text)

        print(f'get_data["name"] = {get_data["name"]}')
        print()
        new_user = User(user_name=get_data["name"], age=get_data["age"])
        new_user.save()
        print(f'new_user.id = {new_user.id}')
        data_structure.append(get_data)

        print(data_structure)

        return JsonResponse(get_data, status=200)