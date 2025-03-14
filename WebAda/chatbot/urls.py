from django.urls import path
from .views import chatbot_interface, chat_view  # ⬅ Adicionado chat_view corretamente

urlpatterns = [
    path("", chatbot_interface, name="chatbot_interface"),  # Página web
    path("api/chat/", chat_view, name="chatbot_api"),  # API do chatbot
]
