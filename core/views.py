from django.shortcuts import render

def smth(request):
    return render(request,'base.html', context={'hello': 'hello'})
