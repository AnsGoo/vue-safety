from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from guard.settings import SECRET_KEY

s=Serializer(SECRET_KEY,expires_in=60*60*24*7)

def create_token(username,password):
    token =s.dumps({'username':username,"password":password})
    return str(token,encoding='utf-8')

# # 计算年龄
# def calculate_age(born):
#     today = datetime.datetime.now()
#     return int(today.year-born.year)
    