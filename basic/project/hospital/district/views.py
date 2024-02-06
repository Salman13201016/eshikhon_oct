from django.shortcuts import render,redirect

from division.models import Divisions
from .models import Districts

# Create your views here.


def index(request):
    data = Divisions.objects.all().order_by('-id')
    data2 = Districts.objects.select_related('div_id').all()
    data_context = {'d':data,'d2':data2}
    return render(request,'admin/district.html',data_context)

def insert(request):
    id = request.POST.get('id')
    name = request.POST.get('name')

    dis_obj = Districts()
    div_obj = Divisions.objects.get(id=id)
    dis_obj.name = name 
    dis_obj.div_id = div_obj

    

    dis_obj.save()

    return redirect('dis_index')
