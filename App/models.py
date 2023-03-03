from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class EmpClockin(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clockinTime = models.TimeField(auto_now=True)
    clockinDate = models.DateField(auto_now=True)
