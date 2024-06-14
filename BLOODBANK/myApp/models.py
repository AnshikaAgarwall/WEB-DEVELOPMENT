from django.db import models

class DONOR_DATA(models.Model):
    d_name=models.CharField(max_length=20)
    d_email=models.EmailField()
    d_mother=models.CharField(max_length=20)
    d_father=models.CharField(max_length=20)
    d_dob=models.DateField()
    d_gender=models.CharField(max_length=20)
    d_weight=models.IntegerField()
    d_bloodgroup=models.CharField(max_length=20)
    d_adhar=models.BigIntegerField(null=False,default=0)
    d_uadhar=models.ImageField(null=True)

class BloodDonation(models.Model):
    city = models.CharField(max_length=100)
    blood_group_A_positive = models.IntegerField(default=0)
    blood_group_A_negative = models.IntegerField(default=0)   
    blood_group_B_positive = models.IntegerField(default=0)
    blood_group_B_negative = models.IntegerField(default=0)
    blood_group_AB_positive = models.IntegerField(default=0)
    blood_group_AB_negative = models.IntegerField(default=0)
    blood_group_O_positive = models.IntegerField(default=0)
    blood_group_O_negative = models.IntegerField(default=0)
