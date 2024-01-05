from django.views import View
from .models import Alumno
from  django.http import JsonResponse

class ApiStudentsAll(View):
    def get(self,request):
        glist = Alumno.objects.all()
        return JsonResponse(list(glist.values()), safe = False)
class ApiStudent(View):
    def get(self,request,search):
        glist =Alumno.objects.all().filter(idPlayer=search)
        return JsonResponse(list(glist.values()),safe = False)