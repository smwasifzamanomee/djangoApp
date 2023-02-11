from django.urls import path
from myApi import views

urlpatterns = [
    path('planList/', views.PlanList.as_view()),
    path('planCreate/', views.PlanCreate.as_view()),
    path('planDestroy/<int:id>', views.PlanDestroy.as_view()),
]
