from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse
# Create your views here.

#function based view
'''
def index(request):
    return render(request,'index.html')
'''

class CBView(View):
    def get(self,request):
        return HttpResponse("Class Based View (CBV) are so COOL!")
