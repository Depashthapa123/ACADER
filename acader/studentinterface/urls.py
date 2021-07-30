from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('course_content/', views.course_content, name='course_content'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_marks/', views.student_marks, name='student_marks'),
    path('search_marks/', views.search_marks, name='search_marks'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('do_logout2/', views.do_logout2, name='do_logout2'),
    path('predict/', views.predict, name='predict'),
    path('predict/result', views.result, name='result'),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)