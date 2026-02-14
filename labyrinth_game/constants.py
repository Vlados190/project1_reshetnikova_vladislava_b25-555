ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число после девяти". Введите ответ цифрой или словом.', '10'),
        'reward': 'golden_coin'
    },
    'trap_room': {
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг'),
        'reward': 'trap_pass'
    },
    'library': {
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс'),
        'reward': 'ancient_scroll'
    },
    'armory': {
        'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library', 'north': 'secret_room'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None
    },
    'secret_room': {
        'description': 'Тайная комната за старым шкафом. Здесь тихо и пусто, но видно мерцающее свечение.',
        'exits': {'south': 'armory'},
        'items': ['treasure_key'],
        'puzzle': None
    },
    'treasure_room': {
        'description': 'Комната с большим сундуком. Дверь заперта — нужен особый ключ.',
        'exits': {'south': 'hall'},
        'items': ['treasure_chest'],
        'puzzle': ('Дверь защищена кодом. Введите код (подсказка: 2*5=?)', '10'),
        'reward': 'treasure_gem'
    },
    'underground_lake': {
        'description': 'Подземное озеро с темной водой. На берегу лежит серебряный ключ.',
        'exits': {'west': 'armory'},
        'items': ['silver_key'],
        'puzzle': ('Чтобы достать ключ, ответьте: сколько букв в слове "вода"?', '4'),
        'reward': 'silver_key_reward'
    }
}

COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "north/south/east/west": "быстрое перемещение без слова go",
    "look": "осмотреть комнату",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет",
    "inventory": "показать инвентарь",
    "solve": "решить загадку",
    "help": "показать список команд",
    "quit": "выйти из игры"
}

EVENT_PROBABILITY = 10      # вероятность наступления случайного события (1 из 10)
NUM_RANDOM_EVENTS = 3       # количество возможных случайных событий
