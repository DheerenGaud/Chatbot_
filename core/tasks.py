# from celery import Celery
# from celery.schedules import crontab
# from core.utils import delete_old_data

# app = Celery('core', broker='redis://localhost:6379/0')

# app.conf.beat_schedule = {
#     'delete-old-data': {
#         'task': 'core.tasks.delete_old_data_task',
#         'schedule': crontab(hour=18, minute=32)  # Runs every day at 2am
#     },
# }

# @app.task
# def delete_old_data_task():
#     delete_old_data()
