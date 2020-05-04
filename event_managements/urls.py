# users/urls.py
from django.urls import path
from .views import SignUpView, EventAPIView, EventDetails, TroupeAPIView, TroupeDetails


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('event/', EventAPIView.as_view()),
    path('event/<int:id>/', EventDetails.as_view()),
    path('troupe/', TroupeAPIView.as_view()),
    path('troupe/<int:id>/', TroupeDetails.as_view()),
]