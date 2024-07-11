from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import renderers
from dishes.views import  IngredientViewSet
from rest_framework.authtoken import views as v


ingredient_list = IngredientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
ingredient_detail = IngredientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('api/cooks/', views.CookList.as_view()),
    path('api/cooks/<int:pk>/', views.CookDetail.as_view()),
    path('api/dishes/', views.DishList.as_view()),
    path('api/dishes/<int:pk>/', views.DishDetail.as_view()),
    path('api/ingredients/', ingredient_list, name='ingredient-list'),
    path('api/ingredients/<int:pk>/', ingredient_detail, name='ingredient-detail'),
    path('api-token-auth/', v.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls'))

]

