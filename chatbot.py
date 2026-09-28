from providers.openai_provider import OpenAIProvider
from providers.gemini_provider import GeminiProvider
from providers.grok_provider import GrokProvider

from history import ChatHistory
from config import get_provider


class Chatbot:

    def __init__(self):

        self.history = ChatHistory()

        provider_name = get_provider()

        if provider_name == "openai":

            self.provider = OpenAIProvider()

        elif provider_name == "gemini":

            self.provider = GeminiProvider()

        elif provider_name == "grok":

            self.provider = GrokProvider()

        else:

            raise ValueError(
                f"Proveedor desconocido: {provider_name}"
            )

    def send_message(self, message):

        self.history.add_user_message(message)

        try:

            response = self.provider.send_message(
                self.history.get_messages()
            )

            self.history.add_assistant_message(response)

            return response

        except Exception:

            # Si la API falla, quitamos el mensaje
            # que acabamos de guardar.

            self.history.messages.pop()

            raise

    def clear_history(self):

        self.history.clear()

    def message_count(self):

        return self.history.count()
