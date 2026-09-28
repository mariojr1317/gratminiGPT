import os

from dotenv import load_dotenv


load_dotenv()


def get_provider():
    return os.getenv("AI_PROVIDER", "openai").lower()


def get_openai_key():
    return os.getenv("OPENAI_API_KEY")


def get_gemini_key():
    return os.getenv("GEMINI_API_KEY")


def get_xai_key():
    return os.getenv("XAI_API_KEY")


def get_openai_model():
    return "gpt-5.5"


def get_gemini_model():
    return "gemini-3.8-flash"


def get_grok_model():
    return "grok-4.7"
