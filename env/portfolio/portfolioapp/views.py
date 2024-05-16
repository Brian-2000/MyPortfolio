from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
# Create your views here.

def homepage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            messageupload = form.save(commit=False)
            messageupload.name = form.cleaned_data['name']
            messageupload.email = form.cleaned_data['email']
            messageupload.message = form.cleaned_data['message']

            messageupload.save()
            return redirect('portfolioapp:home')
    else:
        form = MessageForm()
    return render(request=request, template_name="portfolioapp/index.html", context={'form':form})