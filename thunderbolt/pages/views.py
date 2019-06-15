from django.shortcuts import render
from .models import Roadmap,Sponsors,TeamMembers,Usecase,Advisors
# Create your views here.
def index(request):
    backers = Sponsors.objects.all()
    sponsors = {
        'sponsors':backers,
    }
    return render(request,'pages/index.html',sponsors)
def about(request):
    context =TeamMembers.objects.all()
    advisors = Advisors.objects.all()
    members = {
        'members':context,
        'advisors':advisors,
    }
    return render(request,'pages/about.html',members)
def usecase(request):
    use_case_details = Usecase.objects.all()
    usecases = {
        'usecases':use_case_details,
    }
    return render(request,'pages/usecase.html',usecases)
def community(request):
    return render(request,'pages/community.html')

def roadmap(request):
    details = Roadmap.objects.all()
    milestones = {
        'roadmap':details,
    }
    return render(request,'pages/roadmap.html',milestones)