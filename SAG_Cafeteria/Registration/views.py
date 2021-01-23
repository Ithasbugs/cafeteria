from django.shortcuts import render, redirect, HttpResponse
from Cafeteriacore.models import ExtendedUserInfo, User
from django.contrib import messages
from django.contrib.auth import authenticate


def login(request):
    if request.method == 'POST':
        username = request.POST['username-login']
        password = request.POST['password-login']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        return HttpResponse("welcome to the django app")
    else:
        return render(request, 'signup.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['passwd-inp'] != request.POST['passwd-conf']:
            messages.error(request, "Passwords did not match please renter the details")
            return redirect('login')
        image = request.FILES['img']
        user = User.objects.create_user(request.POST['username'],
                                   request.POST['email'],
                                   request.POST['passwd-inp'])
        new_user = ExtendedUserInfo.objects.create(user=user,
                                                   phone_number=request.POST['mob-no'],
                                                   employee_id=request.POST['emp-id'],
                                                   organization=request.POST['org'])
        new_user.id_card = image
        new_user.save(update_fields=['id_card'])
        messages.success(request, "You have successfully registered to SAG cafeteria.\
                         Please login with your credentials")
        return redirect('signup')
    return render(request, 'signup.html')
