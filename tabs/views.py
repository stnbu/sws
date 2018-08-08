from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Tab, Content

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
                context['contact_form_submitted'] = 'Your message has been sent. Thank you.'
        else:
            form = ContactForm()
        context['form'] = form
    return render(request, 'tabs/index.html', context)
