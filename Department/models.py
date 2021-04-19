from django.db import models
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    Dept_ID = models.AutoField(primary_key=True)
    Dept_Name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('DepartmentListView')

    def __str__(self):
        return self.Dept_Name

    class Meta:
        ordering = ['Dept_Name']
