from django.urls import path

from my_app import views
from my_app.my_views import category_views
from my_app.my_views import student_views
from my_app.my_views import subject_views
from my_app.my_views import teacher_views

urlpatterns = [
    path('', views.home, name='home'),
    path('find_by_id/<id>', views.find_by_id),
    path('content/', views.contact, name='content'),
    #-----------Router category--------------
    path('category/index/', category_views.index, name='category_index'),
    path('category/show/', category_views.show, name='category_show'),
    path('category/create/', category_views.create , name='category_create'),
    path('category/delete_by_id/<id>', category_views.delete_by_id , name='category_delete_by_id'),
    path('category/edit_by_id/<id>', category_views.edit_by_id , name='category_edit_by_id'),
    path('category/update_by_id/<id>', category_views.update_by_id, name='category_update_by_id'),
    #-----------Router Student--------------
    path('student/index/', student_views.index, name='Student_index'),
    path('student/show/', student_views.show, name='Student_show'),
    path('student/create/', student_views.create, name='Student_create'),
    path('student/delete_by_id/<int:id>/', student_views.delete_by_id , name='Student_delete_by_id'),
    path('student/edit_by_id/<int:id>/', student_views.edit_by_id, name='Student_edit_by_id'),
    path('student/update_by_id/<int:id>/', student_views.update_by_id, name='Student_update_by_id'),

    # -----------Router Subject--------------
    # Subject URLs
    path('subject/index/', subject_views.index, name='Subject_index'),
    path('subject/show/', subject_views.show, name='Subject_show'),
    path('subject/create/', subject_views.create, name='Subject_create'),
    path('subject/edit_by_id/<int:id>/', subject_views.edit_by_id, name='Subject_edit_by_id'),
    path('subject/update_by_id/<int:id>/', subject_views.update_by_id, name='Subject_update_by_id'),
    path('subject/delete_by_id/<int:id>/', subject_views.delete_by_id, name='Subject_delete_by_id'),

    # -----------Router teacher--------------
    path('teacher/index/', teacher_views.index, name='teacher_index'),
    path('teacher/show/', teacher_views.show, name='teacher_show'),
    path('teacher/create/', teacher_views.create, name='teacher_create'),
    path('teacher/delete_by_id/<int:id>/', teacher_views.delete_by_id, name='teacher_delete_by_id'),
    path('teacher/edit_by_id/<int:id>/', teacher_views.edit_by_id, name='teacher_edit_by_id'),
    path('teacher/update_by_id/<int:id>/', teacher_views.update_by_id, name='teacher_update_by_id'),

]


