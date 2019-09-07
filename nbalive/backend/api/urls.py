from django.urls import path
from . import views

urlpatterns = [
    path('api/game/', views.GameList.as_view()),
    path('api/game/<int:pk>', views.GameDetail.as_view()),
    path('api/boxscore/', views.BoxScoreList.as_view()),
    path('api/boxscore/<int:pk>', views.BoxScoreDetail.as_view()),
]
