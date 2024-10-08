
from django.conf.urls import url, include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from administrator import views

administrator_patterns = [
    path('update-hours/<user_id>/', views.update_hours, name='update_hours'),
    path('update-hours/', views.update_hours, name='update_hours'),
    path('admin_main', views.admin_main,name="admin_main"),
    #flujo usuarios
    path('users_main', views.users_main,name="users_main"),
    path('new_user/',views.new_user, name='new_user'),

    path('user_block/<user_id>/',views.user_block, name='user_block'),
    path('user_activate/<user_id>',views.user_activate, name='user_activate'),
    path('user_delete/<user_id>',views.user_delete, name='user_delete'),
    
    path('edit_user/<user_id>/',views.edit_user, name='edit_user'),
    
    path('list_main2/',views.list_main2, name='list_main2'),     
    
    path('list_user_active2/',views.list_user_active2, name='list_user_active2'),     
    path('list_user_active2/<groups>/<page>/',views.list_user_active2, name='list_user_active2'),     
    path('list_user_block2/',views.list_user_block2, name='list_user_block2'),     
    path('list_user_block2/<groups>/<page>/',views.list_user_block2, name='list_user_block2'), 
    
    path('carga_masiva/',views.carga_masiva,name="carga_masiva"),# administrador_carga_masiva
    path('carga_masiva_save/',views.carga_masiva_save,name="carga_masiva_save"),#administrador_carga_masiva_save
    path('import_administrator/',views.import_administrator,name="import_administrator"),#administrador
    path('administrator/carga_masiva/',views.carga_masiva,name="carga_masiva"),#administrador
    path('admin_dashboard/',views.admin_dashboard,name="admin_dashboard"),
    #BORRAR
    path('ejemplo_query_set/',views.ejemplo_query_set, name='ejemplo_query_set'),  
    ]  
