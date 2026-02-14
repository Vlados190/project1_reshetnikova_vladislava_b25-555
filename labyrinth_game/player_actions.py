from constants import ROOMS
from utils import describe_current_room, attempt_open_treasure, random_event


def show_inventory(game_state):
    inventory = game_state['player_inventory']
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь пуст.")


def get_input(prompt="> "):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def move_player(game_state, direction):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    exits = room_data['exits']

    if direction not in exits:
        print("Нельзя пойти в этом направлении.")
        return

    next_room = exits[direction]

    if next_room == 'treasure_room':
        if 'rusty_key' in game_state['player_inventory']:
            print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")
        else:
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
            return

    game_state['current_room'] = next_room
    game_state['steps_taken'] += 1

    describe_current_room(game_state)

    random_event(game_state)


def take_item(game_state, item_name):
    room_data = ROOMS[game_state['current_room']]

    if item_name in room_data['items']:
        game_state['player_inventory'].append(item_name)
        room_data['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


def use_item(game_state, item_name):
    if item_name not in game_state['player_inventory']:
        print("У вас нет такого предмета.")
        return

    if item_name == 'torch':
        print("Вы зажгли факел. Стало светлее вокруг.")

    elif item_name == 'sword':
        print("Вы держите меч уверенно в руках.")

    elif item_name == 'bronze_box':
        print("Вы открыли бронзовую шкатулку.")
        if 'rusty_key' not in game_state['player_inventory']:
            game_state['player_inventory'].append('rusty_key')
            print("Вы нашли внутри: rusty_key")

    elif item_name == 'treasure_chest':
        attempt_open_treasure(game_state, get_input)

    else:
        print("Вы не знаете, как использовать этот предмет.")
