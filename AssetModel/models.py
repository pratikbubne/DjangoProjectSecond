from django.db import models
from django.urls import reverse

class AssetModel(models.Model):
    Model_ID = models.AutoField(primary_key=True)
    Model_Number = models.CharField(max_length=50)
    Model_Name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('AssetModelListView')

    def __str__(self):
        return self.Model_Name

    class Meta:
        ordering = ['Model_Name']
