from django.shortcuts import render

def works(request):
    return render(request, 'works/works.html', locals())