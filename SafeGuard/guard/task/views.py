from django.shortcuts import render

# Create your views here.
def test_task(request):
    import time
    from apscheduler.schedulers.background import BackgroundScheduler
    from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
    try:  
        # 实例化调度器
        scheduler = BackgroundScheduler()
        # 调度器使用DjangoJobStore()
        scheduler.add_jobstore(DjangoJobStore(), "default")
        # 'cron'方式循环，周一到周五，每天9:30:10执行,id为工作ID作为标记
        # ('scheduler',"interval", seconds=1)  #用interval方式循环，每一秒执行一次
        @register_job(scheduler, 'cron', day_of_week='mon-fri', hour='9', minute='40', second='10',id='task_time')
        def test_job():
            t_now = time.localtime()
            print(t_now)
            print('我是任务我已经执行了')

        # 监控任务
        register_events(scheduler)

        scheduler.start()
    except Exception as e:
        print(e)
        scheduler.shutdown()
        # 报错则调度器停止执行
