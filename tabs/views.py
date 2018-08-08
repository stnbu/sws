from django.shortcuts import get_object_or_404, render
from .models import Tab, Content

def tab(request, current_tab):
    tabs = Tab.objects.order_by('order')
    tab = Tab.objects.get(name=current_tab)
    content = get_object_or_404(Content, tab=tab)
    context = {
        'tabs': tabs,
        'current_tab': current_tab,
        'content': content,
    }
    return render(request, 'tabs/index.html', context)
