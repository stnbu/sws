import smtplib
from email.mime.text import MIMEText

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Tab, Content

def _send_mail(form):

    name = form.data['name']
    message = form.data['message']
    email = form.data['email']
    
    _from = 'noreply@unintuitive.org'
    to = 'hshimamoto@gmail.com'
    subject = 'Message from "{0} <{1}>"'.format(name, email)

    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = _from
    message['To'] = to
    s = smtplib.SMTP('localhost')
    s.sendmail(_from, [to], message.as_string())
    s.quit()


def tab(request, current_tab_name):
    tabs = Tab.objects.order_by('order')
    current_tab = Tab.objects.get(name=current_tab_name)
    content = get_object_or_404(Content, tab=current_tab)
    context = {
        'tabs': tabs,
        'current_tab': current_tab,
        'content': content,
    }
    if current_tab_name == 'contact':
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                _send_mail(form)
                context['contact_form_submitted'] = True
        else:
            form = ContactForm()
        context['form'] = form
    return render(request, 'tabs/index.html', context)
