from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'ChenchuLakshmi','age':22}
    return render(request,'jinga_printing.html',context=d)