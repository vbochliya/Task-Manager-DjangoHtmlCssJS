from django.db import models
from django.contrib.auth.models import User


class all_the_tasks(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE,related_name="tasks")
    title=models.CharField(max_length=100)
    date_time_now=models.DateTimeField(auto_now_add=True)
    date_time_target=models.DateTimeField()
    description=models.TextField(max_length=10000)
    complete=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title} {self.date_time_target}'
    
    class Meta:
        ordering=['date_time_target']