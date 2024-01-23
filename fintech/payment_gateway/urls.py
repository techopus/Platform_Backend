# payment_gateway/urls.py

from django.urls import path
from .views import transaction_list, make_payment, chat_assistant

urlpatterns = [
    path('transactions/', transaction_list, name='transaction_list'),
    path('make-payment/', make_payment, name='make_payment'),
    path('chat-assistant/', chat_assistant, name='chat_assistant'),
]

#/payments/urls