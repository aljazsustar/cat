from django.urls import path, include

from indicators.views import ListCreateSymbolsAPIView, GetUpdateDeleteAPIView

urlpatterns = [
    path('', ListCreateSymbolsAPIView.as_view()),
    path('<str:symbol>', GetUpdateDeleteAPIView.as_view())
]
