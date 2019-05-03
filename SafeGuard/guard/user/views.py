import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from utils.user.auth import create_token
from utils.user.require import require_login

# Create your views here.

def login(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            token = create_token(username=username, password=password)
            group = Group.objects.get(user=user)
            return JsonResponse({'status': True, 'username': username, 'token': token, 'isadmin': user.is_superuser,'group':group.name})
        else:
            return JsonResponse({'status': False, 'username': None, 'token': None,'group':None,'isadmin':False})
    else:
        return JsonResponse({'status': False, 'username': None, 'token': None})

@require_login
def user_list(request):
    data=json.loads(request.body)
    group = Group.objects.get(id=data.get('group')) 
    users = list(group.user_set.all().values('id','username','email','is_superuser','is_staff','last_login'))
    return JsonResponse(users,safe=False)