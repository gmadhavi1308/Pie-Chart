from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=30)
    population = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'PieChart'
