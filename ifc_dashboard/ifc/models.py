from django.db import models

# Create your models here.
class Organization(models.Model):
    organization_name = models.CharField(max_length=200)
    # IFC, PHC, MCGC
    parent_organization = models.CharField(max_length=4)
