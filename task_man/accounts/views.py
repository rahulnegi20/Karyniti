from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse 
from django.http import HttpResponseRedirect 

def register(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'register':
            #getting form values
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            #validating password
            if password == password2:
            # Check username
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That username is taken')
                    return render(request, 'accounts/loginandreg.html')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'That email is being used')
                        return render(request, 'accounts/loginandreg.html')

                    else:              
                        user = User.objects.create_user(username=username, password=password, email=email)
                        user.save()
                        messages.success(request, 'You are now registered and can log in')
                        return render(request, 'accounts/loginandreg.html')
            else: 
                messages.error(request, 'Passwords do not match')
                return render(request, 'accounts/loginandreg.html')
    # else:
    #     return render(request, 'accounts/loginandreg.html')


        elif request.POST.get('submit') == 'login':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, 'accounts/loginandreg.html')
    
    return render(request, 'accounts/loginandreg.html')

        
