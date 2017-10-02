from django.shortcuts import render

def glavnaya(request):

    return render(request, 'glavnaya/glavnaya.html', locals())
