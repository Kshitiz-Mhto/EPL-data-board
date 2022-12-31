from django.shortcuts import render

from .apilol import standingS, scorer

# Create your views here.

#bd93962d45c9409bbadbf0d29c25e67e

def home(request):
    standing = standingS()
    formi = []
    for teams in standing:
        form = teams['form'].replace(",","")
        formi.append(form+" ")
    
    dates, top_scorers = scorer()

    return render(
        request,
        'epl.html',
        {
            'standings':standing,
            'form':formi,
            'start':dates['startDate'],
            'end':dates['startDate'],
            'topper':top_scorers
            })