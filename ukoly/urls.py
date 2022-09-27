from django.urls import path
from . import views

#/seznam - ukolu/
#/detail-ukolu/100/

app_name = "ukoly"

urlpatterns = [
    path("",views.ukoly_index, name="ukoly_index"),
    path("login",views.ukoly_login, name="ukoly_login"),
    path("kontakty",views.ukoly_kontakty, name="ukoly_kontakty"),
    path("seznam-ukolu/", views.seznam_ukolu, name="seznam_ukolu"),
    path("detail-ukolu/<int:index_ukolu>/", views.detail_ukolu, name="detail_ukolu"),
]