from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonnelSerializer
from rest_framework import generics
from .models import Department, Personnel
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStafforReadOnly
from rest_framework.response import Response
from rest_framework import generics, status
# Create your views here.


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated, IsStafforReadOnly]


class PersonnelListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.request.user.is_staff:
            personnel = self.perform_create(serializer)
            data = {
                "message": f"Personnel {personnel.first_name} is saved successfully",
                "personnel": serializer.data
            }

        else:
            data = {
                "message": "You are unauthorized"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        person = serializer.save()
        return person
