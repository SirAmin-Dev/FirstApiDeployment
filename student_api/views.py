from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Student
# Create your views here.

class StudentListEndPoint(APIView):
    def get(self, request):
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Post added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        try:
            student = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            raise Response({"error": "Student does not esist"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = StudentSerializer(Student, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({"message": "Data Successfully updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try: 
            student = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            raise Response({"error": "Student does not exists"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

