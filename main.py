from chatbot import Chatbot
from utils import (
    print_header,
    print_help,
    clean_text,
    is_command,
    get_command
)


def process_command(command, chatbot):

    if command == "/help":

        print_help()
        return True

    if command == "/clear":

        chatbot.clear_history()

        print()
        print("Conversación borrada.")
        print()

        return True

    if command == "/count":

        count = chatbot.message_count()

        print()
        print(f"Mensajes guardados: {count}")
        print()

        return True

    if command == "/exit":

        print()
        print("¡Hasta luego!")
        print()

        return False

    print()
    print("Comando desconocido. Usa /help.")
    print()

    return True


def chat_loop(chatbot):

    while True:

        try:

            user_input = input("Tú: ")

        except KeyboardInterrupt:

            print("\n\nSaliendo...")
            break

        user_input = clean_text(user_input)

        if not user_input:
            continue

        if is_command(user_input):

            command = get_command(user_input)

            should_continue = process_command(
                command,
                chatbot
            )

            if not should_continue:
                break

            continue

        try:

            print()
            print("IA: ", end="")

            response = chatbot.send_message(
                user_input
            )

            print(response)
            print()

        except Exception as error:

            print()
            print("❌ Ocurrió un error:")
            print(error)
            print()


def main():

    print_header()

    try:

        chatbot = Chatbot()

    except Exception as error:

        print("❌ No se pudo iniciar el chatbot.")
        print()
        print(error)

        return

    print("Escribe /help para ver los comandos.")
    print()

    chat_loop(chatbot)


if __name__ == "__main__":
    main()
