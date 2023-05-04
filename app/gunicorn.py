backlog = 2048

bind = "0.0.0.0:5000"
workers = 1  # multiprocessing.cpu_count() * 2 + 1
timeout = 240
threads = 2
worker_class = "uvicorn.workers.UvicornWorker"
reload = True
errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
