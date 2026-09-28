import requests

from config import get_xai_key, get_grok_model


class GrokProvider:

    def __init__(self):

        self.api_key = get_xai_key()

        if not self.api_key:
            raise ValueError(
                "No se encontró XAI_API_KEY en el archivo .env"
            )

        self.model = get_grok_model()

        self.url = "https://api.x.ai/v1/chat/completions"

    def send_message(self, messages):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "messages": messages
        }

        response = requests.post(
            self.url,
            headers=headers,
            json=data,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        return result["choices"][0]["message"]["content"]
