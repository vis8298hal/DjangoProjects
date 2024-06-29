from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string
# Create your views here.

monthly_challenges ={
    'january': 'Prepare Mathematics',
    'february': 'Prepare English',
    'march': 'Prepare Data Structure & Algorithm',
    'april': 'Practice the test Papers',
    'may': 'Learn Application Development',
    'june': 'Create some Applications',
    'july': 'Go for M01',
    'august': 'Go for M02',
    'september': 'Go for M03',
    'october': 'Just try being on track for Data Analytics',
    'november': 'Be on Application Development',
    'december': 'Learn ML & Apply in your application'
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {'months': months})

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseRedirect("/challenges/Error")
    else:
        forward_month = months[month-1].lower()
        redirect_path = reverse("monthly_challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        error_path = reverse("show_error")
        return HttpResponseRedirect(error_path)
    


def show_error(request):
    return HttpResponse("<div class='error'><h1>404</h1><h2>Invalid Month</h2></div>")
