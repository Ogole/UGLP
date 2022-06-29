from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,reverse
from django.shortcuts import render
from django.contrib import messages
 

from .people_selector import get_Peoples,get_people
from .vht_selector import get_VHTS,get_VHT
from .register_vht_form import VHTForm

def index_view(request):
    return render(request, "index.html")

# Create your views here.
def manage_VHT(request):
    get_vhts = get_VHTS()
    vht_form= VHTForm()
    if request.method == "POST":
        vht_form=VHTForm(request.POST,request.FILES)
        if vht_form.is_valid():
            vht_form.save()
            messages.success(request,'VHT data submitted successfully')
        else:
            messages.WARNING(request, 'Data submission failed') 
        

    context={
        "vht_form":vht_form,
        "get_vhts": get_vhts
    }
    return render(request,"vht.html",context)
