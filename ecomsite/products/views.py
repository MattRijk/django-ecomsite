from django.shortcuts import render
from lib2to3.fixes.fix_input import context


# Create your views here.
def home(request):
    
    if request.user.is_authenticated():
        username_is = "Matt using context"
        context = {"username_is": request.user.email}   # or just request.user
    else:
        context = {"username_is":"unknown"}
    
    
    template = 'base.html'
    return render(request, template, context)
