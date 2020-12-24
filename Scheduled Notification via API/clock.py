from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from first import send, wish, monday, tuesday, wednesday, thursday, friday, sunday, saturday, alarm, step1, step2

sched = BlockingScheduler()

# Schedule to send message on each day;
sched.add_job(wish, trigger='cron', hour='00', minute='1')
sched.add_job(alarm, trigger='cron', hour='7', minute='00')
sched.add_job(step1, trigger='cron', hour='10', minute='00')
sched.add_job(step2, trigger='cron', hour='14', minute='00')

sched.add_job(monday, trigger='cron', day_of_week='0')
sched.add_job(tuesday, trigger='cron', day_of_week='1')
sched.add_job(wednesday, trigger='cron', day_of_week='2')
sched.add_job(thursday, trigger='cron', day_of_week='3')
sched.add_job(friday, trigger='cron', day_of_week='4')
sched.add_job(saturday, trigger='cron', day_of_week='5')
sched.add_job(sunday, trigger='cron', day_of_week='6')


sched.start()