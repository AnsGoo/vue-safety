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


def upfile(ip, src, dest):
    tgt = [ip]
    module = 'cp.get_file'
    argv = [src, dest, "makedirs=True"]
    result = Client(tgt, module, argv)
    return result

# 执行函数


def downfile(ip, dest):
    tgt = [ip]
    module = 'cp.push'
    argv = [dest]
    result = Client(tgt, module, argv)
    return result


if __name__ == "__main__":
    tgt = ["192.168.1.191"]
    module = 'cp.get_file'
    argv = ["salt:///opt/hostinfo.json",
            "/opt/upload/hostinfo.json", "makedirs=True"]
    result = Client(tgt, module, argv)
    print(result)
