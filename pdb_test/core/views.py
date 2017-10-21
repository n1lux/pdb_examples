from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    info = get_info()
    
    import pdb; pdb.set_trace() 
    
    html = "<strong>Hello Word in {} {}</strong>".format(info['name'], info['data'])
    return HttpResponse(html)




def get_info():
    data = {"name": "Grupy-sp Indaiatuba",
            "date": "21/10/2017"}
    
    return data
