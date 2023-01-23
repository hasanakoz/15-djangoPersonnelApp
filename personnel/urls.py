from django.urls import path
from .views import DepartmentView, PersonnelListCreateView, PersonnelGetUpdateDelete, DepartmentPersonnelView

urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personnel/", PersonnelListCreateView.as_view()),
    path("personnel/<int:pk>/", PersonnelGetUpdateDelete.as_view()),
    path("department/<str:department>/", DepartmentPersonnelView.as_view()),
]
