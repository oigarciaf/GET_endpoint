from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from students.models import Student
from students.serializers import StudentSerializer
# Create your views here.

@csrf_exempt
def studentApi(request,id = 0):
    if request.method =='GET':
        students = Student.objects.all()
        students_serializer = StudentSerializer(students,many=True)
        return JsonResponse(students_serializer.data,safe=False)
    elif request.method == 'POST':
        students_data = JSONParser().parse(request)
        students_serializer = StudentSerializer(data = students_data)
        if students_serializer.is_valied():
            students_serializer.save()
            return JsonResponse("Se agrego correctamente", safe=False)
        return JsonResponse("Fallo", safe=False)
    elif request.method == 'PUT':
        students_data = JSONParser().parse(request)
        students = Student.objects.get(StudentId=students_data['StudentId'])
        students_serializer = StudentSerializer(students, data = students_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("actualizacion correcta", safe=False)
        return JsonResponse("fallo la actualizacion")
    elif request.method == 'DELETE':
        students = Student.objects.get(StudentId=id)
        students.delete()
        return JsonResponse("se elimino correctamente", safe=False)
    































