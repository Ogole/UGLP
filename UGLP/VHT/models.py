from django.db import models

# Create your models here.
import uuid
class Register_VHT(models.Model):
    VHTIDN=models.UUIDField(default=uuid.uuid4,editable=False)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=15)
    DOB=models.DateField()
    Reg_date=models.DateTimeField(auto_now=True)
    NIN=models.CharField(max_length=20, null=False, blank=False)
    Village_or_Zone=models.CharField(max_length=20)
    Parish_or_Ward=models.CharField(max_length=20)
    SubCounty=models.CharField(max_length=20)
    DISTRICT_TYPE_CHOICES=[
        ('Kampala','Kampala'),
        ('Arua Central', 'Arua Central '),
        ('Koboko', 'Koboko')

    ]

    District=models.CharField(max_length=30, choices=DISTRICT_TYPE_CHOICES, default='Kampala')


class Register_People(models.Model):
    UPIDN=models.UUIDField(default=uuid.uuid4,editable=False)
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    GENDER_TYPE_CHOICES=[
        ('Male', 'Male'),
        ('Female','Female')
    ]
    Gender=models.CharField(GENDER_TYPE_CHOICES, default='Male', max_length=10 )
    Date_Of_Birth=models.DateField(max_length=10)
    Village_or_Zone=models.CharField(max_length=30)
    Parish_or_Ward=models.CharField(max_length=30)
    SubCounty=models.CharField(max_length=30)
    City_or_Municipality=models.CharField(max_length=30)
    District=models.ForeignKey(Register_VHT, on_delete=models.CASCADE)
    STATUS_TYPE_CHOICES=[
        ('Dead', 'Dead'),
        ('Alive','Alive')
    ]
    Status=models.CharField(STATUS_TYPE_CHOICES, default='Alive',max_length=10 )
    Attach_BirthCertificate=models.ImageField(upload_to='Birth_Certificates')
    Father_Name=models.CharField(max_length=20)
    Mother_Name=models.CharField(max_length=20)
    




    

