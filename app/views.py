import email
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from mailersend import emails
from mailerlite import MailerLiteApi
import math
import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf8')


def index(request):
    return render(request, 'app/index.html')

def thanks(request):
    return render(request, 'app/thanks.html')

def getGroup(request):
    api = MailerLiteApi(settings.MAILERLITE_API_KEY)
    print(api.groups.all(gfilters='Relcanonical'))
    return redirect("thanks")


def submitForm(request):
    if(request.method == "POST"):
        page_count = float(request.POST.get("page_count"))
        current_arpu = float(request.POST.get("current_arpu"))
        first_name = request.POST.get("first_name")
        email_address = request.POST.get("email_address")
        estimated_crawl = math.ceil((float(settings.ROWT_ESTIMATED_CRAWL)/100)*page_count)
        estimated_visits = math.ceil((float(settings.ROWT_ESTIMATED_VISIT)/100)*estimated_crawl)
        estimated_conversions = math.ceil((float(settings.ROWT_ESTIMATED_CONVERSIONS)/100)*estimated_visits)
        rowt = math.ceil(current_arpu*estimated_conversions)

        api_key = settings.MAILERSEND_API_KEY
        api = MailerLiteApi(settings.MAILERLITE_API_KEY)

        mailer = emails.NewEmail(api_key)

        # define an empty dict to populate with mail values
        mail_body = {}

        mail_from = {
            "name": "ROWT",
            "email": "founder@rowt.co.uk",
        }

        recipients = [
            {
                "name": first_name,
                "email": email_address,
            }
        ]

        reply_to = [
            {
                "name": "ROWT",
                "email": "founder@rowt.co.uk",
            }
        ]

        mailer.set_mail_from(mail_from, mail_body)
        mailer.set_mail_to(recipients, mail_body)
        mailer.set_subject(first_name+", Here's Your ROWT", mail_body)
        content = getTextTemplateForMail(locale.format("%d", math.ceil(page_count), grouping=True), 
        locale.format("%d", math.ceil(current_arpu), grouping=True),
        first_name,
        locale.format("%d", estimated_crawl, grouping=True),
        locale.format("%d", estimated_visits, grouping=True),
        locale.format("%d", estimated_conversions, grouping=True),
        locale.format("%d", rowt, grouping=True))
        mailer.set_plaintext_content(content, mail_body)
        mailer.set_reply_to(reply_to, mail_body)

        # using print() will also return status code and data
        print(mailer.send(mail_body))
        api.groups.add_single_subscriber(group_id=54475389360145449, subscribers_data={"email": email_address, "name": first_name}, autoresponders=False, resubscribe=False, as_json=False)
    return redirect(settings.ROWT_REDIRECT_URL)

def getTextTemplateForMail(page_count, current_arpu, first_name, estimated_crawl, 
        estimated_visits, estimated_conversions, rowt):
        return '''Hi, '''+first_name+'''!

Kindly find your ROWT below:

Page Count: '''+str(page_count)+'''
Current ARPU: £'''+str(current_arpu)+'''
====================
Estimated Crawls: '''+str(estimated_crawl)+'''
Estimated Monthy Visits: '''+str(estimated_visits)+'''
Estimated Monthly Conversions: '''+str(estimated_conversions)+'''
====================
Average ROWT: £'''+str(rowt)+'''
====================

ROWT is a product of Relcanonical.
Create 400k+ Pages with Dynamic Content in 2s
https://relcanonical.com/account/request

ROWT
'''