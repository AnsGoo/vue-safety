import json
from django.http import JsonResponse
from django.contrib.auth.models import Group
from utils.user.require import require_login
from cmdb.models import CMDB

# Create your views here.

@require_login
def cmdb_list(request):
    data=json.loads(request.body)
    group = Group.objects.get(id=data.get('group')) 
    cmdb_set = CMDB.objects.select_related('creator').filter(group=group)
    # print(cmdb_set[0].creator.username)
    # print(CMDB.objects.prefetch_related('creator__username').filter(group=group).values('id','device_type','port','hostname','addtime','creator_username'))
    cmdbs=[]
    for cmdb in cmdb_set:
        cmdbs.append({
            'id':cmdb.id,
            'device_type':cmdb.device_type,
            'port':cmdb.port,
            'hostname':cmdb.hostname,
            'addtime':cmdb.addtime.strftime('%Y-%m-%d %H:%M:%S'),
            'user':cmdb.creator.username,
            'ip':cmdb.ip
        })
    return JsonResponse(cmdbs,safe=False)