from django.shortcuts import render
from price.models import Woman, Man, Dlinna, Nails, Nails_type,Other, Other_type

def price(request):
    return render(request, 'price/price.html', locals())
def nogty(request):
    nails_3 = Nails.objects.filter(type_id = 3)
    nails_2 = Nails.objects.filter(type_id = 2)
    nails_null = Nails.objects.filter(type_id = 1)
    nails_type = Nails_type.objects.all()
    return render(request, 'price/nogty.html', {'nails_2': nails_2,'nails_3': nails_3, 'nails_null': nails_null,'nails_type': nails_type,})
def paric(request):
    woman = Woman.objects.all()
    man = Man.objects.all()
    dlinna=Dlinna.objects.all()
    return render(request, 'price/paric.html',{'woman': woman,'man': man, 'dlinna': dlinna,})
def other(request):
    other_2 = Other.objects.filter(type_id=2)
    other_1 = Other.objects.filter(type_id=1)
    other_type = Other_type.objects.all()
    return  render(request, 'price/other.html', {'other_1': other_1, 'other_2': other_2, 'other_type': other_type })
