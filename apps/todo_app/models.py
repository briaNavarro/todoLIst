from django.db import models

# Create your models here.


class TodoList(models.Model):
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'The text: {self.text}, The complete: {self.completed}, ID: {self.id}'
