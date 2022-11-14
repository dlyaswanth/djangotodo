from django.db import models
from users.models import User
# Create your models here.
class Task(models.Model):

    user = models.ForeignKey(User,on_delete=User)
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    completed = models.BooleanField(null=True,default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True,null=True)

