from django.shortcuts import render, redirect
from .forms import ApplicationForm
from  .models import Form
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            Form.objects.create(**form.cleaned_data)
            messages.success(request, "Form submitted")
            return redirect('index')
        else:
            messages.error(request, "Form invalid. Please check errors.")
    else:
        form = ApplicationForm()

    return render(request, "index.html", {'form': form})
