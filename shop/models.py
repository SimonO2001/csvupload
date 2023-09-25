# shop/models.py

from django.db import models

class Product(models.Model):
    Location = models.CharField(max_length=1000, null=True,blank=True)
    Customer_id = models.CharField(max_length=1000, null=True,blank=True)
    MAC = models.CharField(max_length=1000, null=True,blank=True)
    Model = models.CharField(max_length=1000, null=True,blank=True)
    S_N = models.CharField(max_length=1000, null=True,blank=True)
    Name = models.CharField(max_length=1000, null=True,blank=True)
    Image = models.CharField(max_length=1000, null=True,blank=True)
    GW_IP = models.CharField(max_length=1000, null=True,blank=True)
    Notes = models.CharField(max_length=1000, null=True,blank=True)
    Journalsystem = models.CharField(max_length=1000, null=True,blank=True)
    Analyzers = models.CharField(max_length=1000, null=True,blank=True)
    SIM = models.CharField(max_length=1000, null=True,blank=True)
    

    def __str__(self):
        return f"{self.Location} {self.Customer_id} {self.MAC} {self.Model} {self.S_N} {self.Name} {self.Image} {self.GW_IP} {self.Notes} {self.Journalsystem} {self.Analyzers} {self.SIM}"