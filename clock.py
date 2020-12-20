from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from whats import send

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send, 'interval', seconds=10)

sched.start()