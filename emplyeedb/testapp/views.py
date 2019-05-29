from django.shortcuts import render
from testapp.models import Employee

def Employee_info(request):
    emp_list=Employee.objects.all()
    my_dict={"emp_list":emp_list}
    return render(request,"testapp/index.html",context=my_dict)

def __str__(self):
    return (self.eno)
