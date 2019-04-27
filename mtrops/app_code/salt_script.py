#!/usr/bin/python2.7
# coding:utf-8


# salt api
def Client(tgt, module, argv):
    import salt.client
    local = salt.client.LocalClient()
    if argv:
        result = local.cmd(tgt, module, argv, tgt_type='list')
    else:
        result = local.cmd(tgt, module, tgt_type='list')
    return result

# 执行函数


def Install(ips, script):
    tgt = ips
    module = 'cmd.script'
    argv = [script]
    result = Client(tgt, module, argv)
    return result
