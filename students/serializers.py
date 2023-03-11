from rest_framework import serializers
from students.models import Student
class StudentSerializer(serializers.ModelSerializers):
    class Meta:
        model = Student
        fields = ('StusdentId','StudentName', 'StudentLastName', 'StudentAccount')
