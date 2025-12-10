# Author: kk.Fang(fkfkbill@gmail.com)

from celery import platforms

from settings import backend_conf


platforms.C_FORCE_ROOT = True

def build_redis_url(db: int):
    user_password = ""
    if backend_conf.redis_user or backend_conf.redis_password:
        user_password = f"{backend_conf.redis_user}:{backend_conf.redis_password}"
    return f"redis://{user_password + '@' if user_password else ''}{backend_conf.redis_host}:{backend_conf.redis_port}/{db}"

broker_url = build_redis_url(1)
result_backend = build_redis_url(2)

# enable_utc = False
timezone = 'Asia/Shanghai'
task_serializer = 'json'
accept_content = ['pickle', 'json', 'msgpack', 'yaml']
result_serializer = 'json'
worker_max_tasks_per_child = 10
worker_prefetch_multiplier = 1
worker_deduplicate_successful_tasks = True
task_acks_late = True
broker_transport_options = {'visibility_timeout': 60*60*24*9}
worker_concurrency = 5

imports = []
task_routes = {}
task_queues = set()
