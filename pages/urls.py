from django.urls import path
from .views import HomePageView, EvaluateHomerPageView, HomerEvaluatedPageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('evaluate/', EvaluateHomerPageView, name='evaluate_homer'),
    path('evaluated/<int:pk>/', HomerEvaluatedPageView, name='homer_evaluated'),
    ]
