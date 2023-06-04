from django.urls import path
from Myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('<int:pk>',views.CandidateView.as_view(),name='profile')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)