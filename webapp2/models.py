from django.db import models

class Record(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=12)
    province = models.CharField(max_length=12)
    country = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return self.first_name + " " + self.last_name 
