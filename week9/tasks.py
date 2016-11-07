import time
import random
import datetime

from celery import Celery

app = Celery('tasks')


@app.task
def cal_decombobulator_xy():
    now = datetime.datetime.now()
    time.sleep(random.randint(0, 5))
    print(now)
