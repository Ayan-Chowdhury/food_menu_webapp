from django.urls import path
from . import views

app_name='food_menu'
urlpatterns = [
    path('',views.index,name='index'),
    path('item/',views.item,name='Item'),
    path('<int:item_id>/',views.detail,name='detail'),
    #add Itmes
    path('add', views.create_item, name='create_item'),
    #edit items
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete item
    path('delete/<int:id>/', views.delete_item,name='delete_item')
]
