from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail
from django.contrib import messages

from django.conf import settings
from contactForm.models import Contact
from PortfolioContact.tasks import send_mail_to_admin, send_mail_to_user



# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, subject=subject, desc=desc, date=datetime.today())
        contact.save()

        messages.success(request, 'Your message has been sent.')

        mail_to_user = send_mail_to_user.delay(name, email)

        mail_to_admin = send_mail_to_admin.delay(name, email, subject, desc)

        if mail_to_user==1 and mail_to_admin==1:
            print("Mail sent successfully")

        
    return render(request, 'index.html')



def contactMe(request): 
    if request.method == "POST":
        name = request.POST.get('portfolioName')
        email = request.POST.get('portfolioEmail')
        subject = request.POST.get('portfolioSubject')
        desc = request.POST.get('portfolioDesc')

        print(name, email, subject, desc)
        
    return render(request, 'akhilPortfolio.html')