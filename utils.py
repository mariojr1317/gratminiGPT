def print_header():
    print("=" * 50)
    print("          MI CHATBOT IA")
    print("=" * 50)
    print()


def print_help():
    print()
    print("Comandos disponibles:")
    print()
    print("/help   - Mostrar esta ayuda")
    print("/clear  - Borrar la conversación")
    print("/count  - Ver cantidad de mensajes")
    print("/exit   - Salir")
    print()


def clean_text(text):
    return text.strip()


def is_command(text):
    return text.startswith("/")


def get_command(text):
    return text.lower().strip()
