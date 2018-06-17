from django.http import HttpResponse
from django.shortcuts import render

def special_case_2003(request, year, month):
    return HttpResponse('%s %s' % (year, month))

def test_function(request):
    people = ['keith', 'erin', 'paul', 'ryan']
    return render(request, 'example.html', {'people': people})

def list_clients(request):
    return HttpResponse('Hello znc')

