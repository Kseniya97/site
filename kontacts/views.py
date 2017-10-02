from django.shortcuts import render

def kontacts(request):
    return render(request, 'kontacts/kontacts.html', locals())