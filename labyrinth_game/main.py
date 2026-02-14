from constants import COMMANDS
from utils import describe_current_room, solve_puzzle, show_help, attempt_open_treasure
from player_actions import get_input, move_player, take_item, show_inventory, use_item


def process_command(game_state, command_line):
    parts = command_line.strip().split()
    if not parts:
        return

    command, *args = parts
    command = command.lower()
    arg = " ".join(args).lower()

    match command:

        case "look":
            describe_current_room(game_state)

        case "inventory":
            show_inventory(game_state)

        case "go":
            if arg:
                move_player(game_state, arg)
            else:
                print("Укажите направление.")

        case "north" | "south" | "east" | "west":
            move_player(game_state, command)

        case "take":
            if arg:
                take_item(game_state, arg)
            else:
                print("Укажите предмет.")

        case "use":
            if arg:
                use_item(game_state, arg)
            else:
                print("Укажите предмет.")

        case "solve":
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state, get_input)
            else:
                solve_puzzle(game_state, get_input)

        case "help":
            show_help(COMMANDS)

        case "quit" | "exit":
            game_state['game_over'] = True

        case _:
            print("Неизвестная команда. Введите 'help'.")


def main():
    game_state = {
        'player_inventory': [],
        'current_room': 'entrance',
        'game_over': False,
        'steps_taken': 0
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while not game_state['game_over']:
        command = get_input("> ")
        process_command(game_state, command)


if __name__ == "__main__":
    main()
