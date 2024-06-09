"""
URL configuration for assisipro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
   
    path('user_login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),

    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),

    # ABOUT SECTION START

    path('st_francis_of_assisi/',views.st_francis_of_assisi,name='st_francis_of_assisi'),
    path('conventuals_in_india/',views.conventuals_in_india,name='conventuals_in_india'),
    path('conventual_charism/',views.conventual_charism,name='conventual_charism'),
    path('history_of_the_order',views.history_of_the_order,name='history_of_the_order'),
    path('st_maximilian_kolbe',views.st_maximilian_kolbe,name='st_maximilian_kolbe'),
    path('franciscan_saints',views.franciscan_saints,name='franciscan_saints'),

    # Administration Start
    path('provinical_administration',views.provinical_administration,name='provinical_administration'),
    path('ap_telengana_delegation',views.ap_telengana_delegation,name='ap_telengana_delegation'),
    path('kolkata_mission',views.kolkata_mission,name='kolkata_mission'),
    path('sri_lankan_mission',views.sri_lankan_mission,name='sri_lankan_mission'),
   
    
    # Vocation start
    path('vocation_1',views.vocation_1,name='vocation_1'),
    path('vocation_2',views.vocation_2,name='vocation_2'),

    path('Friars',views.Friars,name='Friars'),
    

    path('Assisi_shanthi_kendra',views.Assisi_shanthi_kendra,name='Assisi_shanthi_kendra'),
    path('Kolbe_Franciscan_Ashram',views.Kolbe_Franciscan_Ashram,name='Kolbe_Franciscan_Ashram'),
    path('Nirmalaram_Franciscan_Ashram',views.Nirmalaram_Franciscan_Ashram,name='Nirmalaram_Franciscan_Ashram'),
    path('Padua_Franciscan_Ashram',views.Padua_Franciscan_Ashram,name='Padua_Franciscan_Ashram'),
    path('Franciscan_Ashram',views.Franciscan_Ashram,name='Franciscan_Ashram'),
    path('St_Paul_Franciscan_Ashram',views.St_Paul_Franciscan_Ashram,name='St_Paul_Franciscan_Ashram'),

    # FRIARIES  ANDRA start
    path('St_Maximilian_Franciscan_Ashram',views.St_Maximilian_Franciscan_Ashram,name='St_Maximilian_Franciscan_Ashram'),
    path('Bala_Yesu_Franciscan_Ashram',views.Bala_Yesu_Franciscan_Ashram,name='Bala_Yesu_Franciscan_Ashram'),
    path('San_Cupertino_Franciscan_Ashram',views.San_Cupertino_Franciscan_Ashram,name='San_Cupertino_Franciscan_Ashram'),
    path('St_Francis_Friary',views.St_Francis_Friary,name='St_Francis_Friary'),
    path('St_Peter_Franciscan_Ashram',views.St_Peter_Franciscan_Ashram,name='St_Peter_Franciscan_Ashram'),
    path('Assisi_FranciscanAshram',views.Assisi_FranciscanAshram,name='Assisi_FranciscanAshram'),
    path('St_Anthony_Franciscan_Ashram',views.St_Anthony_Franciscan_Ashram,name='St_Anthony_Franciscan_Ashram'),

    # FRIARIES  TAMIL NADU start
    path('Assisi_Snehalaya',views.Assisi_Snehalaya,name='Assisi_Snehalaya'),
    path('Belvedere_Franciscan_Ashram',views.Belvedere_Franciscan_Ashram,name='Belvedere_Franciscan_Ashram'),
    path('Padre_Pio_Shrine',views.Padre_Pio_Shrine,name='Padre_Pio_Shrine'),

    # FRIARIES  SRI LANKA start
    path('Ave_Maria_Franciscan_Friary',views.Ave_Maria_Franciscan_Friary,name='Ave_Maria_Franciscan_Friary'),
    path('Ave_Maria_Franciscan_Friary',views.Ave_Maria_Franciscan_Friary,name='Ave_Maria_Franciscan_Friary'),
    path('St_Joseph_Vaz_Friary',views.St_Joseph_Vaz_Friary,name='St_Joseph_Vaz_Friary'),
    path('St_Anthony_Friary',views.St_Anthony_Friary,name='St_Anthony_Friary'),
    path('St_FrancisFriary',views.St_FrancisFriary,name='St_FrancisFriary'),

    # MINISTRIS START
    path('Vocation_And_Formation_Apostolate',views.Vocation_And_Formation_Apostolate,name='Vocation_And_Formation_Apostolate'),
    path('OFS',views.OFS,name='OFS'),
    path('Militia_Of_The_Immaculata',views.Militia_Of_The_Immaculata,name='Militia_Of_The_Immaculata'),
    path('FCPD',views.FCPD,name='FCPD'),
    path('Franciscan_Centre',views.Franciscan_Centre,name='Franciscan_Centre'),
    path('Gray_Friars_Publications',views.Gray_Friars_Publications,name='Gray_Friars_Publications'),
    path('Kolbe_Communications',views.Kolbe_Communications,name='Kolbe_Communications'),

    path('Franiscan_Reconciliation_Retreat',views.Franiscan_Reconciliation_Retreat,name='Franiscan_Reconciliation_Retreat'),
    path('Retreat_Centers',views.Retreat_Centers,name='Retreat_Centers'),
    path('Tuesday_Devotions',views.Tuesday_Devotions,name='Tuesday_Devotions'),

    path('Social_Apostolate',views.Social_Apostolate,name='Social_Apostolate'),

    path('Greyfriars_Degree_College',views.Greyfriars_Degree_College,name='Greyfriars_Degree_College'),
    path('Greyfriars_Junior_College',views.Greyfriars_Junior_College,name='Greyfriars_Junior_College'),
    path('Oxford_Creativity_School',views.Oxford_Creativity_School,name='Oxford_Creativity_School'),
    path('St_Anthony_School',views.St_Anthony_School,name='St_Anthony_School'),
    path('St_Peter_School',views.St_Peter_School,name='St_Peter_School'),
    path('Vidyaniketan_Junior_College',views.Vidyaniketan_Junior_College,name='Vidyaniketan_Junior_College'),
    path('St_Padre_Pio_Shrine',views.St_Padre_Pio_Shrine,name='St_Padre_Pio_Shrine'),

    path('St_Padre_Pio_Shrine',views.St_Padre_Pio_Shrine,name='St_Padre_Pio_Shrine'),
    path('St_Maximilian_Kolbe_Church',views.St_Maximilian_Kolbe_Church,name='St_Maximilian_Kolbe_Church'),
    path('Bala_Yesu_Shrine',views.Bala_Yesu_Shrine,name='Bala_Yesu_Shrine'),
    path('Green_Park_Pastoral_Community',views.Green_Park_Pastoral_Community,name='Green_Park_Pastoral_Community'),
    path('St_Francis_Of_Assisi_Church',views.St_Francis_Of_Assisi_Church,name='St_Francis_Of_Assisi_Church'),

    path('add_saints',views.add_saints,name='add_saints'),
    path('view_saints',views.view_saints,name='view_saints'),
    path('update_saints/<int:id>',views.update_saints,name='update_saints'),
    path('delete_saints/<int:id>',views.delete_saints,name='delete_saints'),
    

    path('admin_add_Provinical_Administration',views.admin_add_Provinical_Administration,name='admin_add_Provinical_Administration'),
    path('admin_update_Provinical_Administration/<int:id>/',views.admin_update_Provinical_Administration,name='admin_update_Provinical_Administration'),
    # path('admin_delete_Provinical_Administration/<int:id>/',views.admin_delete_pyayer_wall,name='admin_delete_pyayer_wall'),
    path('admin_view_Provinical_Administration',views.admin_view_Provinical_Administration,name='admin_view_Provinical_Administration'),


    path('admin_add_news_category',views.admin_add_news_category,name='admin_add_news_category'),
    path('admin_view_category',views.admin_view_category,name='admin_view_category'),
    path('admin_update_news_category/<int:id>',views.admin_update_news_category,name='admin_update_news_category'),
    path('admin_delete_news_category/<int:id>',views.admin_delete_news_category,name='admin_delete_news_category'),

    path('admin_add_latest_news',views.admin_add_latest_news,name='admin_add_latest_news'),
    path('admin_view_latest_news',views.admin_view_latest_news,name='admin_view_latest_news'),
    path('news_details/<str:news_heading>/',views.news_details,name='news_details'),
    path('admin_update_latest_news/<int:id>/',views.admin_update_latest_news,name='admin_update_latest_news'),
    path('admin_delete_latest_news/<int:id>/',views.admin_delete_latest_news,name='admin_delete_latest_news'),

    path('gallery',views.gallery,name='gallery'),
    path('admin_add_gallery',views.admin_add_gallery,name='admin_add_gallery'),
    path('admin_gallery_view',views.admin_gallery_view,name='admin_gallery_view'),
    path('admin_update_gallery/<int:id>/',views.admin_update_gallery,name='admin_update_gallery'),
    path('admin_delete_gallery/<int:id>/',views.admin_delete_gallery,name='admin_delete_gallery'),

    path('admin_add_event_category',views.admin_add_event_category,name='admin_add_event_category'),
    path('admin_view_event_category',views.admin_view_event_category,name='admin_view_event_category'),
    path('admin_update_event_category/<int:id>/',views.admin_update_event_category,name='admin_update_event_category'),
    path('admin_delete_event_category/<int:id>/',views.admin_delete_event_category,name='admin_delete_event_category'),

    path('friends_of_smk',views.friends_of_smk,name='friends_of_smk'),

    path('admin_add_events',views.admin_add_events,name='admin_add_events'),
    path('admin_view_events',views.admin_view_events,name='admin_view_events'),
    path('admin_update_events/<int:id>/',views.admin_update_events,name='admin_update_events'),
    path('admin_delete_events/<int:id>/',views.admin_delete_events,name='admin_delete_events'),
    path('event_details/<int:id>/',views.event_details,name='event_details'),

    path('admin_view_comments',views.admin_view_comments,name='admin_view_comments'),
    path('admin_delete_comments/<int:id>',views.admin_delete_comments,name='admin_delete_comments'),
    
    path('admin_add_friars',views.admin_add_friars,name='admin_add_friars'),
    path('friars_view', views.friars_view,name='friars_view'),
    path('update_friars/<int:pk>/',views.update_friars,name='update_friars'),
    path('delete_friars/<int:pk>/',views.delete_friars,name='delete_friars'),
    
    path('admin_add_obituary',views.admin_add_obituary,name='admin_add_obituary'),
    path('obituary_view',views.obituary_view,name='obituary_view'),
    path('update_obituary/<int:id>/',views.update_obituary,name='update_obituary'),
    path('delete_obituary/<int:id>/',views.delete_obituary,name='delete_obituary'),

    path('add_provincial_administaration',views.add_provincial_administaration,name='add_provincial_administaration'),
    path('view_provincial_administration',views.view_provincial_administration,name='view_provincial_administration'),
    path('update_provincial_administration/<int:pk>/',views.update_provincial_administration,name='update_provincial_administration'),
    path('delete_provincial_administration/<int:pk>/',views.delete_provincial_administration,name='delete_provincial_administration'),

    path('add_telegana_delegation',views.add_telegana_delegation,name='add_telegana_delegation'),
    path('view_telengana_delegation',views.view_telengana_delegation,name='view_telengana_delegation'),
    path('update_telengana_delegation/<int:pk>/',views.update_telengana_delegation,name='update_telengana_delegation'),
    path('delete_telengana_delegation/<int:pk>/',views.delete_telengana_delegation,name='delete_telengana_delegation'),

    path('add_kolkata_mission',views.add_kolkata_mission,name='add_kolkata_mission'),
    path('view_kolkata_mission',views.view_kolkata_mission,name='view_kolkata_mission'),
    path('update_kolkata_mission/<int:pk>/',views.update_kolkata_mission,name='update_kolkata_mission'),
    path('delete_kolkata_mission/<int:pk>/',views.delete_kolkata_mission,name='delete_kolkata_mission'),

    path('add_srilankan_mission',views.add_srilankan_mission,name='add_srilankan_mission'),
    path('view_srilankan_mission',views.view_srilankan_mission,name='view_srilankan_mission'),
    path('update_srilankan_mission/<int:pk>/',views.update_srilankan_mission,name='update_srilankan_mission'),
    path('delete_srilankan_mission/<int:pk>/',views.delete_srilankan_mission,name='delete_srilankan_mission'),

    path('add_about_video',views.add_about_video,name='add_about_video'),
    path('admin_view_video',views.admin_view_video,name='admin_view_video'),
    path('update_video_link/<int:id>/',views.update_video_link,name='update_video_link'),
    path('delete_video/<int:id>/',views.delete_video,name='delete_video'),

    path('add_video_gallery',views.add_video_gallery,name='add_video_gallery'),
    path('view_video_gallery',views.view_video_gallery,name='view_video_gallery'),
    path('update_video_gallery/<int:id>/',views.update_video_gallery,name='update_video_gallery'),
    path('delete_video_gallery/<int:id>/',views.delete_video_gallery,name='delete_video_gallery'),
    
    path('notice',views.notice,name='notice'),
    path('add_notice', views.add_notice, name='add_notice'),
    path('view_notice', views.view_notice, name='view_notice'),
    path('update_notice/<int:id>/', views.update_notice, name='update_notice'),
    path('delete_notice/<int:id>/', views.delete_notice, name='delete_notice'),
    path('notice_details/<str:heading>/', views.notice_details, name='notice_details'),

    path('wish',views.wish,name='wish'),
    path('event',views.event,name='event'),
    path('Events', views.Events,name='Events'),
    path('Obituary',views.Obituary,name='Obituary'),

    path('add_wishes',views.add_wishes,name='add_wishes'),
    path('wishes_view',views.wishes_view,name='wishes_view'),
    path('update_wishes/<int:id>/',views.update_wishes,name='update_wishes'),
    path('delete_wishes/<int:id>/',views.delete_wishes,name='delete_wishes'),

    path('admin_calendar',views.admin_calendar,name='admin_calendar'),
    path('wishes',views.wishes,name='wishes'),
    path('video_gallery',views.video_gallery,name='video_gallery'),

    
]
