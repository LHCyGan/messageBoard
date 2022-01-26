from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageModelForm
# Create your views here.
def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def page_error(request):
    return render(request, '500.html', status=500)


def index(request):
    messages = Message.objects.all().order_by('-id')
    if request.method == 'POST':
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'index.html', locals())