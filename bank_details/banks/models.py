from django.db import models


class BankName(models.Model):
    bank_name = models.CharField(max_length=200, blank=False, unique=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ['id']


class BankData(models.Model):
    bank = models.ForeignKey(BankName, on_delete=models.DO_NOTHING, related_name='b_id')
    ifsc = models.CharField(max_length=12, blank=False, unique=True, primary_key=True)
    branch = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=300, blank=False)
    city = models.CharField(max_length=50, blank=False)
    district = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ['ifsc']
            

