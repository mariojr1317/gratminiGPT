from google import genai

from config import get_gemini_key, get_gemini_model


class GeminiProvider:

    def __init__(self):

        api_key = get_gemini_key()

        if not api_key:
            raise ValueError(
                "No se encontró GEMINI_API_KEY en el archivo .env"
            )

        self.client = genai.Client(api_key=api_key)
        self.model = get_gemini_model()

    def send_message(self, messages):

        conversation = ""

        for message in messages:

            role = message["role"]
            content = message["content"]

            if role == "user":
                conversation += f"Usuario: {content}\n"

            elif role == "assistant":
                conversation += f"Asistente: {content}\n"

        conversation += "Asistente:"

        response = self.client.models.generate_content(
            model=self.model,
            contents=conversation
        )

        return response.text
