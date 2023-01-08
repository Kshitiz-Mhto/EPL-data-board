from django.shortcuts import render

from .apilol import standingS, scorer, todayMatch

def home(request):
    standing = standingS()
    formi = []
    for teams in standing:
        form = teams['form'].replace(",","")
        formi.append(form+" ")
    
    dates, top_scorers = scorer()

    matches = todayMatch()

    return render(
        request,
        'epl.html',
        {
            'standings':standing,
            'form':formi,
            'start':dates['startDate'],
            'end':dates['endDate'],
            'topper':top_scorers,
            'todayMatches':matches
            })