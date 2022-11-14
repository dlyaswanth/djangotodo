import logging
import datetime
from django.core.mail import send_mail
from django_cron import CronJobBase, Schedule

from .models import Task
from .serializer import TaskSerializer
from users.models import User

# Get an instance of a logger
logger = logging.getLogger(__name__)

class CheckDeadlineCron(CronJobBase):
    RUN_EVERY_MINS = 0 # every 1 minutes
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tasks.CheckDeadlineCron'    # a unique code
    def do(self):
        try:
            print('---------------------- CRON STARTED ----------------------')
            today = datetime.date.today() 
            print('DATE : ',today)
            tasks = Task.objects.filter(user_id=1)
            print(tasks)
            serializer = TaskSerializer(data=tasks,many=True)
            if serializer.is_valid():
                serializer = serializer.data
                print(serializer)
                for i in serializer:
                    user_email = User.objects.filter(id=i.user).email
                    print(user_email)
                    send_mail(
                        'Today is the last day from '+i.title,
                        'This is a remainder mail for your todo list , make sure that you compelet the task on time',
                        ['test@gmail.com'],
                        ['django-todo@yopmail.com'],
                        fail_silently=False,
                    )
            print('---------------------- CRON ENDED ------------------------')
        except Exception as error:
            print(error)
            print('---------------------- CRON ENDED ------------------------')
        