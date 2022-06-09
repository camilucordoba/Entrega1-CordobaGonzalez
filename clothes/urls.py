from django.urls import path

from clothes.views import List_clothes, Create_clothes, search_clothes, Detail_clothes, Delete_clothes, Update_clothes

urlpatterns =[
    path('', List_clothes.as_view(), name = 'list_clothes'),

    path('create-clothes/', Create_clothes.as_view(), name = 'create_clothes'),
    path('search-clothes/', search_clothes, name = 'search_clothes'),
    path('detail-clothes/<int:pk>/', Detail_clothes.as_view(), name = 'detail_clothes'),
    path('delete-clothes/<int:pk>/', Delete_clothes.as_view(), name = 'delete_clothes'),
    path('update-clothes/<int:pk>/', Update_clothes.as_view(), name = 'update_clothes'),
]