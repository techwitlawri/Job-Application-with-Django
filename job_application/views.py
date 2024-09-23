from django.shortcuts import render, redirect
from .forms import ApplicationForm
from  .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
     if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Save form data to database
            Form.objects.create(**form.cleaned_data)
            
            # Email configuration
            first_name = form.cleaned_data["first_name"]
            email = form.cleaned_data["email"]
            message_body = f"A new job application was submitted.\nThank you, {first_name}."
            subject = "Form submission confirmation"
            
            try:
                email_message = EmailMessage(
                    subject=subject,
                    body=message_body,
                    to=[email]
                )
                email_message.send()
                messages.success(request, "Form submitted and email sent")
            except Exception as e:
                messages.error(request, f"Form submitted but email failed: {str(e)}")
            
            return redirect('index')  # Redirect after submission
     else:
        form = ApplicationForm()

        return render(request, "index.html", {'form': form})
