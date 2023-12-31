from django.http import HttpResponse
from django.shortcuts import render,redirect

from . models import About



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


def about_index(request):

    all_data = About.objects.all()

    data = {'d':all_data}
    # print("this is root url function")
    return render(request,'admin/about.html',data)


from datetime import datetime
def about_insert(request):


    name = request.POST.get('uname')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    exp = request.POST.get('exp')
    no_cust = request.POST.get('no_cust')
    no_project = request.POST.get('no_project')
    no_of_awards = request.POST.get('no_of_awards')
    desc = request.POST.get('desc')
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y - %I:%M %p")

    about_obj = About()

    about_obj.u_name = name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = exp
    about_obj.no_happy_customers = no_cust
    about_obj.no_project_finished = no_project
    about_obj.no_digital_awards = no_of_awards
    about_obj.description = desc
    about_obj.date_time = formatted_datetime

    about_obj.save()


    # print("this is root url function")
    return redirect('about')

def edit_index(request,id):

    data = About.objects.get(id=id)
    d = {'data':data}
    return render(request,'admin/edit.html',d)

def about_edit(request):

    id = request.POST.get('id')
    name = request.POST.get('uname')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    exp = request.POST.get('exp')
    no_cust = request.POST.get('no_cust')
    no_project = request.POST.get('no_project')
    no_of_awards = request.POST.get('no_of_awards')
    desc = request.POST.get('desc')
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y - %I:%M %p")

    about_obj = About.objects.get(id=id)

    about_obj.u_name = name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = exp
    about_obj.no_happy_customers = no_cust
    about_obj.no_project_finished = no_project
    about_obj.no_digital_awards = no_of_awards
    about_obj.description = desc
    # about_obj.date_time = formatted_datetime

    about_obj.save()


    # print("this is root url function")
    return redirect('about')


def delete_index(request,id):

    data = About.objects.get(id=id)
    data.delete()
    return redirect('about')



