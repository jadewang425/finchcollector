from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_feeding', views.add_feeding, name='add_feeding'),
    # toy routes
    # index
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    # detail
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    # create
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    # update
    path('toys/<int:toy_id>/update', views.ToyUpdate.as_view(), name='toys_update'),
    # delete
    path('toys/<int:toy_id>/delete', views.ToyDelete.as_view(), name='toys_delete'),
    
    # associate a toy with the cat on the cat detail page
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # unassociate a toy on the cat detail page
    path('finches/<int:finch_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
]