import math
from constants import EVENT_PROBABILITY, NUM_RANDOM_EVENTS, ROOMS, COMMANDS

def pseudo_random(seed, modulo):
    x = math.sin(seed * 12.9898) * 43758.5453
    fractional = x - math.floor(x)
    return int(fractional * modulo)


def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")

    inventory = game_state['player_inventory']

    if inventory:
        index = pseudo_random(game_state['steps_taken'], len(inventory))
        lost_item = inventory.pop(index)
        print(f"Вы потеряли предмет: {lost_item}")
    else:
        damage = pseudo_random(game_state['steps_taken'], 10)
        if damage < 3:
            print("Вы получили смертельный урон. Игра окончена.")
            game_state['game_over'] = True
        else:
            print("Вы едва уцелели!")


def random_event(game_state):
    if pseudo_random(game_state['steps_taken'], EVENT_PROBABILITY) != 0:
        return

    event_type = pseudo_random(game_state['steps_taken'] + 1, NUM_RANDOM_EVENTS)

    if event_type == 0:
        print("Вы нашли на полу монетку.")
        ROOMS[game_state['current_room']]['items'].append('coin')

    elif event_type == 1:
        print("Вы слышите странный шорох...")
        if 'sword' in game_state['player_inventory']:
            print("Вы достаете меч и отпугиваете существо.")

    elif event_type == 2:
        if (game_state['current_room'] == 'trap_room' and
                'torch' not in game_state['player_inventory']):
            print("В темноте что-то активировалось...")
            trigger_trap(game_state)


def describe_current_room(game_state):
    room = ROOMS[game_state['current_room']]

    print(f"\n== {game_state['current_room'].upper()} ==")
    print(room['description'])

    if room['items']:
        print("Заметные предметы:", ", ".join(room['items']))

    print("Выходы:", ", ".join(room['exits'].keys()))

    if room['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state, get_input_func):
    room = ROOMS[game_state['current_room']]

    if not room['puzzle']:
        print("Загадок здесь нет.")
        return

    question, answer = room['puzzle']
    print(question)

    user_answer = get_input_func("Ваш ответ: ").strip().lower()

    valid_answers = [answer.lower()]
    if answer == "10": 
        valid_answers.append("десять")

    if user_answer in valid_answers:
        print("Верно! Вы решили загадку.")
        room['puzzle'] = None 

        if 'reward' in room:
            reward = room['reward']
            game_state['player_inventory'].append(reward)
            print(f"Вы получили: {reward}")
    else:
        print("Неверно.")
        if game_state['current_room'] == 'trap_room':
            trigger_trap(game_state)


def attempt_open_treasure(game_state, get_input_func):
    room = ROOMS[game_state['current_room']]

    if 'treasure_chest' not in room['items']:
        print("Сундук отсутствует.")
        return

    if 'rusty_key' in game_state['player_inventory']:
        print("Вы используете найденный ключ, чтобы открыть сундук.")
        room['items'].remove('treasure_chest')
        print("Вы победили!")
        game_state['game_over'] = True
    else:
        print("Сундук заперт.")


def show_help(commands):
    print("\nДоступные команды:")
    for cmd, desc in commands.items():
        print(f"  {cmd:<16} - {desc}")

