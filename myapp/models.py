from django.db import models

class MyForm(models.Model):
    Name=models.CharField(max_length=150)
    Age=models.IntegerField()

    def __str__(self):
        return self.Name

