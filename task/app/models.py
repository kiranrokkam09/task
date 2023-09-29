from django.db import models


class banks(models.Model):
    name=models.CharField(max_length=50)
    id=models.BigIntegerField(primary_key=True)

class branches(models.Model):
    ifsc=models.CharField(max_length=50,primary_key=True)
    bank_id=models.ForeignKey(banks,on_delete=models.CASCADE)
    branch=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)

