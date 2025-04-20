from django.shortcuts import render,HttpResponseRedirect
from .form import ContactForm,NewsletterForm
from django.contrib import messages
from blog.models import Post

def index_view(request):
    posts = Post.objects.filter(status=True)[:3]
    return render(request, "website/index.html",{'posts':posts})

def Newsletter_view(request):

    if request.method == "POST":
        form  = NewsletterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = NewsletterForm()

    return render(request, "newsletter/",{'form':form})

def contact_view(request):

    if request.method == "POST":
        form  = ContactForm(request.POST)
        
        if form.is_valid():
            #Course practice
            # data={
            #     'name':'Unknown',
            #     'email': form.cleaned_data['email'],
            #     'subject': form.cleaned_data['subject'],
            #     'message': form.cleaned_data['message'],
            # }
            # form = ContactForm(data,initial=data)
            change_name = form.save(commit=False)
            change_name.name = 'Unknown'
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Form submitted successfully.')
            return HttpResponseRedirect("/contact/")
        else:
            messages.add_message(request, messages.ERROR, 'Captcha incorrect!')
            return HttpResponseRedirect("/contact/")
    else:
        form = ContactForm()
        

    return render(request, "website/contact.html",{'form':form})

def about_view(request):
    return render(request, "website/about.html")