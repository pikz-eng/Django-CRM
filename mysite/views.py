from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Customer



def home(request):
    customers = Customer.objects.all()



    # check to see if loggin in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Esti logat!')
            return redirect('home')
        else:
            messages.success(request, 'User-ul nu existaTry again!')
            return redirect('home')
    else:
        return render(request, 'home.html',  {'customers':customers})



def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out!')
    return redirect('home')

def register_user(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'you have Successfully Registered!')
            return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def customer_record(request,pk):
    if request.user.is_authenticated:

        customer_record = Customer.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})

    else:
        messages.success(request, 'You must to be logged in!')
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Customer Deleted!')
        return redirect('home')
    else:
        messages.success(request, 'You must to be logged in!')
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()


                messages.success(request, 'Record Added!')
                return redirect('home')
        return render(request, 'add_record.html',{'form':form})
    else:
        messages.success(request, 'You must to be logged in!')
        return redirect('home')





