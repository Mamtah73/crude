from django.shortcuts import render, redirect
from .models import Studentlist
from django.contrib import messages
#  Create your views here.

# Crud operations
# c = create
# r = read
# u = update
# d = delete
def home(request):
    studentlist = Studentlist.objects.all()
    context = {
        'studentlist': studentlist,
    }
    return render(request, "index.html", context)

def addnew(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if len(name)<2 or len(email)<3 or len(phone)<6 or len(address)<3:
            messages.error(request,"please fill it properly")
        else:
            addstudent = Studentlist(name=name, email=email, phone=phone, address=address)
            addstudent.save()

            messages.success(request," your data has been saved")
    return redirect( "home")

def edit(request):
    editstudent = Studentlist.objects.all()
    context = {
        'editstudent': editstudent,
    }
    return redirect(request, "home", context)

def update(request, id):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if len(name)<2 or len(email)<3 or len(phone)<6 or len(address)<3:
            messages.error(request,"please fill it properly")
        else:
            addstudent = Studentlist(id=id, name=name, email=email, phone=phone, address=address)
            addstudent.save()

            messages.success(request," successfully updated")
            return redirect( "home")
    