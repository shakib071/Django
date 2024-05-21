from django.shortcuts import render
import datetime

# Create your views here.


def home(request):
    d={'author' : 'rahim', 'age' : 17,'lst' : ['python','is','best'],'birthday':datetime.datetime.now(),
      'val' : " " ,'courses' :[
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 5000
        }, 
        {
            'id' : 2,
            'name' : 'django',
            'fee' : 10000
        }, {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000
        },
    ]}
    # return render(request,'home.html',context=d)
    return render(request,'home.html',d)
#context diye home.html  a d ta pass kore dicci
#khali d dileoo hbe abar context=d dileooo hbe
