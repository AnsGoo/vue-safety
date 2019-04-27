#!/usr/bin/python
# -*- coding: utf-8 -*-


def Client(tgt, module, argv):

    import salt.client

    local = salt.client.LocalClient()
    if argv:
        result = local.cmd(tgt, module, [argv], tgt_type='list')
    else:
        result = local.cmd(tgt, module, tgt_type='list')
    return result


def Os(tgt):
    os_argvs = ['localhost', 'kernel', 'kernelrelease', 'cpu_model', 'num_cpus', 'productname', 'os', 'osrelease',
                'mem_total']

    os_module = 'grains.item'

    oss = {}
    for argv in os_argvs:
        result = Client(tgt, os_module, argv)
        oss[argv] = result

    os_info = {}

    for ip in tgt:
        try:
            os_list = {}

            for argv in os_argvs:
                data = oss[argv][ip][argv]
                os_list[argv] = data
            os_info[ip] = os_list
        except:
            pass
    return os_info


def Disk(tgt):
    disk_argvs = ['/', '/home', '/alidata']

    disk_module = 'status.diskusage'

    disks = {}
    for argv in disk_argvs:
        result = Client(tgt, disk_module, argv)
        disks[argv] = result

    disk_info = {}

    for ip in tgt:

        try:
            data_list = {}
            for argv in disk_argvs:
                try:
                    data = disks[argv][ip][argv]
                except:
                    data = {'available': 0, 'total': 0}
                data_list[argv] = data
            disk_info[ip] = data_list
        except:
            pass

    return disk_info


def Mem(tgt):
    argv = None
    module = 'status.meminfo'
    result = Client(tgt, module, argv)

    mem_info = {}

    for ip in tgt:
        try:
            SwapTotal = result[ip]['SwapTotal']['value']

        except:
            SwapTotal = 0
        mem_info[ip] = {"SwapTotal": SwapTotal}

    return mem_info


def main(tgt):
    os_info = Os(tgt)
    disk_info = Disk(tgt)
    mem_info = Mem(tgt)
    data = {}
    for ip in tgt:
        try:
            sys_info = dict(os_info[ip].items() +
                            disk_info[ip].items() + mem_info[ip].items())
            data[ip] = sys_info
        except:
            pass
    return data


if __name__ == '__main__':
    tgt = ['192.168.1.218', '192.168.1.191']
    result = main(tgt)
    print(result)
