from .models import Register_VHT

def get_VHTS():
    return Register_VHT.objects.all()

def get_VHT(VHT_ID):   
    return Register_VHT.objects.get(pk=VHT_ID)
     
