from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255, blank=False)
   

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False, unique=True)
    department = models.ForeignKey(Department, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name