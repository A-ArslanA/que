from django .urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('views/top/', views.topViews, name='topViews'),
    path('views/all/', views.allViews, name='allViews'),
    path('views/all/filter/<slug:slug>/', views.allViews, name='filterViews'),
    path('view/detail/<int:pk>/', views.viewDetail, name='viewDetail'),
    path('user/sign-up', views.signUp, name='signUp'),
    path('user/login/', views.loginPage, name='login'),
    path('user/logout/', views.logoutUser, name='logoutUser'),
    path('admin/add-genre/', views.addGenre, name='addGenre'),
    path('admin/add-view/', views.addViews, name='addViews'),
]