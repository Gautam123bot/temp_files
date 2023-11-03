from django.db import models

# Create your models here.

class emp(models.Model):
    name = models.CharField(max_length=200, null=True)
    emp_no = models.CharField(max_length=200, null=True)
    salary = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name