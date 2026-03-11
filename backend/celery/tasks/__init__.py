"""
celery tasks package

通过在 worker / app / periodical-worker 启动时递归导入该包，
确保所有 @register_celery_task 的任务被注册。
"""

