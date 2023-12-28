from django.http import HttpResponse
from django.shortcuts import render



def demo(request):
    title = "This is a demo html"
    name = "salman"
    product_name = ['p1','p2','p3']
    data = {"t":title,'name':name,'prod':product_name}
    # print("this is root url function")
    return render(request,'demo/portfolio.html',data)

def demo1(request):
    a = 10
    b = 20 
    c = a +b
    # print("this is root url function")
    return HttpResponse(c)
