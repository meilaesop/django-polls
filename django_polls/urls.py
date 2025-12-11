from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # 原有的投票URL - 保持原样
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    # 🔥 新增用户认证URL
    # 注册
    path('register/', views.register, name='register'),
    # 登录
    path('login/', views.custom_login, name='login'),
    # 退出
    path('logout/', views.custom_logout, name='logout'),
    # 个人资料
    path('profile/', views.profile, name='profile'),
]
