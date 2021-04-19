from django.db import models
from django.urls import reverse

# Create your models here.
class ProjectSite(models.Model):
    Site_ID = models.AutoField(primary_key=True)
    Site_Name = models.CharField(max_length=50)
    Site_Location = models.CharField(max_length=50)
    Site_Department = models.CharField(max_length=50)
    Site_Code = models.CharField(max_length=50)
    Organization_ID = models.IntegerField()
    Organization_Name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('ProjectSiteListView')

    def __str__(self):
        return self.Site_Name

    class Meta:
        ordering = ['Site_Name']
