from django.urls import path
from .views import user_login,dashboard,register
## Djnago build in logout login 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = 'account'

urlpatterns = [
    #path('login/',user_login,name= 'login'),
    path('register/',register,name='register'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    ##password changes
    path('password/change/',
    auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')),
    name='password_change'),

    path('password/change/done',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

    # reset password urls
    path('password_reset/',auth_views.PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done')),
    name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')),
    name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete'),

]