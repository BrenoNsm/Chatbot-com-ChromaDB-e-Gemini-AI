from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Importando os módulos do chatbot
from chatbot.chatbot_code.config import Config
from chatbot.chatbot_code.database import Database
from chatbot.chatbot_code.embeddings import Embeddings
from chatbot.chatbot_code.chatbot import Chatbot
import os
from dotenv import load_dotenv
load_dotenv()

# Configuração inicial
api_key = os.getenv("API_GEMINI_KEY")
API_KEY = api_key
config = Config(api_key=API_KEY)
database = Database(config)
embeddings = Embeddings(config)
chatbot = Chatbot(config, database, embeddings)

from django.shortcuts import render

def chatbot_interface(request):
    return render(request, "index.html")


@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        try:
            # 🛠 Se a requisição for POST, pega os dados do JSON
            data = json.loads(request.body)
            user_message = data.get("message", "").strip()
            user_id = data.get("user_id", "default")

        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato de JSON inválido"}, status=400)

    elif request.method == "GET":
        # 🛠 Se a requisição for GET, pega a mensagem da query string (?message=oi)
        user_message = request.GET.get("message", "").strip()
        user_id = request.GET.get("user_id", "default")

    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)

    # 🔍 Verifica se a mensagem não está vazia
    if not user_message:
        return JsonResponse({"error": "Mensagem vazia"}, status=400)

    # 🚀 Processa a resposta do chatbot
    bot_response = chatbot.get_response(user_message, user_id)

    return JsonResponse({"response": bot_response})
