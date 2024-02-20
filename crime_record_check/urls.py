from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('recordentryNID/', views.record_entry_form_NID, name = "record_entry_form_NID"),
    path('recordentryDOB/', views.record_entry_form_DOB, name = "record_entry_form_DOB"),
    path('signup/police/record/manage/', views.signup, name='signup'),
    path('signout/', views.user_logout , name='signout'),
    path('', views.signin, name='signin'),
    path('search/record/NID', views.search_feature_NID, name='search-view'),
    path('search/record/DOB/', views.search_feature_DOB, name='search-view_DOB'),
    path('recordcheckNID/', views.recordcheckNID, name="record_check_NID"),
    path('recordcheckDOB/', views.recordcheckDOB, name="record_check_DOB"),
    
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
