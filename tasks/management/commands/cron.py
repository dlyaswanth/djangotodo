from django.core.management.base import BaseCommand, CommandError
import datetime
from django.core.mail import send_mail
from tasks.models import Task
from tasks.serializer import TaskSerializer
from users.models import User

class Command(BaseCommand):
    help = 'TO RUN CRON JOB'
    def handle(self, *args, **kwargs):
        try:
            print('---------------------- CRON STARTED ----------------------')
            today = datetime.date.today() 
            print('DATE : ',today)
            tasks = Task.objects.get(pk=int('1'))
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