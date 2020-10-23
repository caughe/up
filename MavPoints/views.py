from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *


def app_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.userprofile.role == 'customer':
                    return HttpResponseRedirect('home')
                elif user.userprofile.role == 'employee':
                    return HttpResponseRedirect('employee_home')
                else:
                    return HttpResponseRedirect(reverse('home'))
            else:
                print("Login attempt failed")
                print("Username : {} and Password : {}".format(username, password))
                return HttpResponse("Invalid credentials!")
        else:
            return HttpResponse("Invalid Form")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})


def create_account(request):
    if request.method == "GET":
        return render(request, "registration/customer_new.html", {"form": CustomerForm})
    elif request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('MavPoints:home'))
        else:
            return HttpResponseRedirect(reverse('MavPoints:home'))


def home(request):
    return render(request, 'main_pages/home.html',
                  {'MavPoints': home})


def promotions(request):
    return render(request, 'main_pages/promotions.html',
                  {'MavPoints': promotions})


def contact(request):
    return render(request, 'main_pages/contact.html',
                  {'MavPoints': contact})


def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_date = timezone.now()
            customer.save()
            customers = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'employee_pages/view_customers.html',
                          {'customers': customers})
    else:
        form = CustomerForm()
        # print("Else")
    return render(request, 'registration/customer_new.html', {'form': form})


# @login_required
# def accountOverview(request):
# return render(request, 'main_pages/accounts.html',  /* MADE A PLACE HOLDER FOR ACCT OVERVIEW */
# {'MavPoints': accounts}) #


@login_required
def rewards(request):
    return render(request, 'main_pages/rewards.html',
                  {'MavPoints': rewards})


@login_required()
def view_customers(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'employee_pages/view_customers.html',
                  {'customers': customer})


@login_required()
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'employee_pages/view_customers.html',
                          {'customers': customer})
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'employee_pages/edit_customer.html', {'form': form})


@login_required()
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('employee_pages:view_customers')
