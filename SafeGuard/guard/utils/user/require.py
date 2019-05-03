from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.contrib import auth
from guard.settings import SECRET_KEY
from django.http import JsonResponse

s=Serializer(SECRET_KEY,expires_in=60*60*24*7)


def require_login(func):
    def warpper(request,*args,**kwargs):
        # print(request.META)
        token = request.META.get('HTTP_AUTHORIZATION')
        value=s.loads(token)
        user=auth.authenticate(**value)
        if user is not None:
            request.user= user
            return func(request,*args,**kwargs)
        else:
            request.user=None
            return JsonResponse({'msg':'user need login'})
    return warpper
    