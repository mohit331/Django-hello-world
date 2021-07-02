from django.shortcuts import render, redirect


def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')



    else:
        username1 = request.POST['username']
        password1 = request.POST['password']
        from django.contrib import auth
        user = auth.authenticate(username=username1, password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
