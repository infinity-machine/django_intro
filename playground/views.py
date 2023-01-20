from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# THIS HANDLES DATA EXCHANGE req => res


# REQUEST HANDLER
def say_hello(request):
    return render(request, 'hello.html')
