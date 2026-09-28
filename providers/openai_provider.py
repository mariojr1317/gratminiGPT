from openai import OpenAI

from config import get_openai_key, get_openai_model


class OpenAIProvider:

    def __init__(self):
        api_key = get_openai_key()

        if not api_key:
            raise ValueError(
                "No se encontró OPENAI_API_KEY en el archivo .env"
            )

        self.client = OpenAI(api_key=api_key)
        self.model = get_openai_model()

    def send_message(self, messages):

        response = self.client.responses.create(
            model=self.model,
            input=messages
        )

        return response.output_text
