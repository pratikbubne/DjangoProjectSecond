from django.db import models
from django.urls import reverse

# Create your models here.
class Supplier(models.Model):
    Supplier_ID = models.AutoField(primary_key=True)
    Supplier_Name = models.CharField(max_length=50)
    Supplier_Mailid = models.CharField(max_length=50)
    Supplier_Mobile = models.IntegerField()
    City = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('SupplierListView')

    def __str__(self):
        return self.Supplier_Name

    class Meta:
        ordering = ['Supplier_Name']
