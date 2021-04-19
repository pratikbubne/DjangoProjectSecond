from django.db import models
from django.urls import reverse

# Create your models here.
class FunctionalGroup(models.Model):
    Fun_ID = models.AutoField(primary_key=True)
    Functional_Group = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('FunctionalGroupListView')

    def __str__(self):
        return self.Functional_Group

    class Meta:
        ordering = ['Functional_Group']
