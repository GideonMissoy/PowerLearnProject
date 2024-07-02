from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('reset-password/', PasswordResetRequestView.as_view(), name='reset-password'),
    path('confirm-password-reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='confirm-password-reset'),
    path('set-new-password/', SetNewPassword.as_view(), name='set-new-password'),
    path('logout/', LogoutUserView.as_view(), name='logout')
]

