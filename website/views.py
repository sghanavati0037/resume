from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {'name':'Sara Ghanavati'}
    return render(request, 'website/index.html', context)

def about_view(request):
    return render(request, 'website/about.html')

def education_view(request):
    context = {'name':'Sara Ghanavati'}
    return render(request, 'website/education.html', context)

def experience_view(request):
    context = {'name':'Sara Ghanavati'}
    return render(request, 'website/experience.html', context)

def skills_view(request):
    context = {'name':'Sara Ghanavati'}
    return render(request, 'website/skills.html', context)

def project_view(request):
    context = {'name':'Sara Ghanavati'}
    return render(request, 'website/project.html', context)

def contact_view(request):
    context = {'name':'Sara Ghanavati'}
    return render(request, 'website/contact.html', context)