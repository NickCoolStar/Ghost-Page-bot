bind = "0.0.0.0:10000"
workers = 1
worker_class = "aiohttp.worker.GunicornWebWorker"
timeout = 120
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = "info" 