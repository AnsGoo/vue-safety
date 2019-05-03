from gevent import monkey
monkey.patch_all() # 打补丁, 将python原来的同步阻塞式的通信, 变成异步非阻塞通信

import argparse # 命令行解析
from gevent.pywsgi import WSGIServer # 替代原来django的服务器
from geventwebsocket.handler import WebSocketHandler
from ironfort.wsgi import application
import os
version = '1.0.0'

root_path = os.path.dirname(__file__)

parser = argparse.ArgumentParser(description="IronFort - 基于WebSocket的SSH堡垒机")
parser.add_argument('--port','-p',
                    type=int,
                    default=8001,
                    help='服务器端口默认为8000')

parser.add_argument('--host','-H',
                    default='0.0.0.0',
                    help='服务器ip默认是0.0.0.0')

args = parser.parse_args()

print('[IronFort] {0} running on {1} : {2}'.format(version, args.host, args.port))

ws_server = WSGIServer(
    (args.host, args.port),
    application,
    log=None,
    handler_class=WebSocketHandler
)

try:
    ws_server.serve_forever()
except KeyboardInterrupt:
    print("服务器关闭...")
