from django.urls import path

from . import views

urlpatterns = [
    path("create-user/", views.RegisterUserView().as_view(),
         name="create-user"),

    path("send-money/", views.TransactionView().as_view(), name="send-money"),
]
