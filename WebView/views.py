from django.shortcuts import render,redirect
from .models import Event,PLOT,FARM,CONSTRUCTION,AGRICULTURE,CONSULTANT,UNDERGRADUATE,MICROCREDIT,EDUCATION,Broker,Contact,Suscribe
from .form import BrokerForm
from .contact import ContactForm
from .suscribe import SuscribeForm
from django.contrib import messages

def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == "POST":
       cont_form=ContactForm(request.POST)

       if cont_form.is_valid():
          cont_form.save() 
          messages.success(request,"Your form is successful submitted.")
       else:
           messages.error(request,"request failed.")
       return redirect("contact")
    
    else:
        form=ContactForm()
        context={
            'contactform':form
        }
    return render(request,'contact.html',context)


def events(request):
    upd_event=Event.objects.all()
    context={
        'event':upd_event
    }
    return render(request,'events.html',context)


def non_real_estate(request):
    return render(request,'non_real_estate.html')

def non_real_tabs_1(request):
    upd_consultant=CONSULTANT.objects.all()
    context={
        'consultant':upd_consultant
    }
    return render(request,'non_real_tabs_1.html',context)

def non_real_tabs_2(request):
    upd_undergraduate=UNDERGRADUATE.objects.all()
    context={
        'undergraduate': upd_undergraduate
    }
    return render(request,'non_real_tabs_2.html',context)

def non_real_tabs_3(request):
    upd_microcredit=MICROCREDIT.objects.all()
    context={
        'microcredit': upd_microcredit
    }
    return render(request,'non_real_tabs_3.html',context)

def non_real_tabs_4(request):
    upd_education=EDUCATION.objects.all()
    context={
        'education': upd_education
    }
    return render(request,'non_real_tabs_4.html',context)


def real_estate(request):
    return render(request,'real_estate.html')

def real_tabs_1(request):

    upd_plot=PLOT.objects.all()
    context={
        'plot': upd_plot
    }
    return render(request,'real_tabs_1.html',context)


def real_tabs_2(request):
    upd_farm=FARM.objects.all()
    context={
        'farm': upd_farm
    }
    return render(request,'real_tabs_2.html',context)


def real_tabs_3(request):
    upd_construction=CONSTRUCTION.objects.all()
    context={
        'construction':  upd_construction
    }
    return render(request,'real_tabs_3.html',context)


def real_tabs_4(request):
    upd_agriculture=AGRICULTURE.objects.all()
    context={
        'agriculture':  upd_agriculture
    }
    return render(request,'real_tabs_4.html',context)

def brokers(request):
    if request.method == "POST":
        my_form=BrokerForm(request.POST)
        if my_form.is_valid():
            my_form.save() 
            #messages.success(request,'you are broker is successful captured,thanks!!')
        else:
            messages.error(request,'Error, identified.')
        
        return redirect('broker_post')
    
    else:
        my_form=BrokerForm()
        context={
                 'form':my_form,
                 }
    return render(request,'brokers.html',context)

def broker_post(request):
    broker=Broker.objects.all().order_by('-username') 
    #if no order_by() then Broker.objects.all
    context={
         'broker':broker
        }
    return render(request,'broker_post.html',context)

def suscribe(request):
    if request.method=="POST":
        suscribe=SuscribeForm(request.POST)
        if suscribe.is_valid():
           suscribe.save() 
           messages.success(request,"Thanks for suscribe us.")
        else:
            messages.error(request,"error, try again.")
        
        return redirect("footer")
    
    else:
        suscribe=SuscribeForm()
        context={
            "form":suscribe
        }
    return render(request,"footer.html",context)