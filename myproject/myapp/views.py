from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database
            messages.success(request, 'Thank you for your message!') # Show success message
            return render(request, 'myapp/success.html')
    else:
        form = ContactForm()
    
    return render(request, 'myapp/contact.html', {'form': form})
