from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# THIS HANDLES DATA EXCHANGE req => res


# REQUEST HANDLER
## RENDER TAKES IN REQUEST, A TEMPLATE, AND AN OBJECT OF INFO, THAT CAN BE CONDITIONALLY RENDERED IN TEMPLATE HTML
def say_hello(request):
    print('ok')
    return render(request, 'hello.html', {
        'name': 'Connor'
    })
