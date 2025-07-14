from django.urls import path
from . import views

app_name='food_menu'
urlpatterns = [
    path('',views.index,name='index'),
    path('item/',views.item,name='Item'),
    path('<int:item_id>/',views.detail,name='detail'),
    #add Itmes
    path('add', views.create_item, name='create_item')

]
