from django.contrib import messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']

            user = register_form.save()
            login(request, user)
            messages.success(request, 'Hi {username}, you have successfully registered!!!')
            return redirect('/')
        else:
            messages.error(request, 'Something went wrong!!!')


    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'form': register_form})


from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    # subject = request.POST.get('subject', '')
    # message = request.POST.get('message', '')
    # from_email = request.POST.get('from_email', '')
    subject = 'test'
    message = 'barev'
    from_email = 'manukyan.tigran22@gmail.com'

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['mher.sahakyan.03@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
