from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings



def contact(request):
    title = 'Connect with us'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from Garud Travels'
        message = '%s %s' %(name, comment)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail( subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks for the messages"
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None
        
    context = { 'title' : title, 'form' : form, 'confirm_message': confirm_message, }
    context = locals()
    return render(request, 'contact.html', context)
