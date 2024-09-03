from django.urls import path
from .views import index, detailed_task, todo_by_status, Todo_list_Category, Createtodo, createCategory, update_task, delete_task, signup, login_view, logout_view, dashboard

urlpatterns = [
    path('', index, name='home'),  # Home page for guests
    path('dashboard/', dashboard, name='dashboard'),  # Dashboard for logged-in users
    path('detailed/<int:id>/', detailed_task, name='detail'),
    path('todo/update/<int:id>/', update_task, name='update-task'),
    path('todo/delete/<int:id>/', delete_task, name='delete-task'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('todos/status/<str:st>/', todo_by_status, name='status'),
    path('todo/category/<int:id>/', Todo_list_Category, name='cattodo'),
    path('todo/create/', Createtodo, name='createtodo'),
    path('category/create/', createCategory, name='createcategory'),
    path('todo/delete/<int:id>/', delete_task, name='delete-task'),

]
