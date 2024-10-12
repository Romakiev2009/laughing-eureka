import random
import sys
import json
import os
from colorama import init, Fore

init(autoreset=True)

inventory = []
player = {
    'name': '',
    'race': '',
    'class': '',
    'hp': 100,
    'attack': 10,
    'defense': 5,
    'level': 1,
    'experience': 0,
    'quests_completed': []
}
game_file = 'savegame.json'

# Функції збереження та завантаження гри
def save_game():
    with open(game_file, 'w') as f:
        json.dump(player, f)
    print(Fore.GREEN + "Гра збережена успішно!")

def load_game():
    global player
    if os.path.exists(game_file):
        with open(game_file, 'r') as f:
            player = json.load(f)
        print(Fore.GREEN + "Гра завантажена успішно!")
        return True
    else:
        print(Fore.RED + "Файл збереження не знайдено.")
        return False

# Створення персонажа
def create_character():
    print(Fore.CYAN + "Ласкаво просимо до світу Ельдорадо!\n")
    player['name'] = input(Fore.GREEN + "Введіть ім'я вашого персонажа: ").strip()
    print(Fore.YELLOW + f"Привіт, {player['name']}!\n")

    races = ['Людина', 'Ельф', 'Дворф', 'Гном']
    print(Fore.CYAN + "Виберіть расу:")
    for idx, race in enumerate(races, 1):
        print(f"{Fore.CYAN}{idx}. {race}")
    while True:
        choice = input(Fore.GREEN + "Ваш вибір (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            player['race'] = races[int(choice)-1]
            break
        else:
            print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")
    print(Fore.YELLOW + f"Ви обрали расу: {player['race']}\n")

    classes = ['Воїн', 'Маг', 'Лучник', 'Злодій']
    print(Fore.CYAN + "Виберіть клас:")
    for idx, cls in enumerate(classes, 1):
        print(f"{Fore.CYAN}{idx}. {cls}")
    while True:
        choice = input(Fore.GREEN + "Ваш вибір (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            player['class'] = classes[int(choice)-1]
            break
        else:
            print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")
    print(Fore.YELLOW + f"Ви обрали клас: {player['class']}\n")

    if player['class'] == 'Воїн':
        player['attack'] += 5
        player['defense'] += 3
    elif player['class'] == 'Маг':
        player['attack'] += 7
        player['defense'] += 1
    elif player['class'] == 'Лучник':
        player['attack'] += 4
        player['defense'] += 2
    elif player['class'] == 'Злодій':
        player['attack'] += 6
        player['defense'] += 2

    display_stats()

# Відображення характеристик
def display_stats():
    print(Fore.GREEN + f"\nХарактеристики {player['name']}:")
    print(f"{Fore.GREEN}HP: {player['hp']}")
    print(f"{Fore.GREEN}Атака: {player['attack']}")
    print(f"{Fore.GREEN}Захист: {player['defense']}")
    print(f"{Fore.GREEN}Рівень: {player['level']}")
    print(f"{Fore.GREEN}Досвід: {player['experience']}\n")

# Головне меню
def main_menu():
    print(Fore.CYAN + "Головне меню:")
    print("1. Почати подорож")
    print("2. Переглянути інвентар")
    print("3. Зберегти гру")
    print("4. Завантажити гру")
    print("5. Вийти з гри")
    print("6. Переглянути характеристики")
    choice = input(Fore.GREEN + "Ваш вибір: ").strip()
    if choice == '1':
        world_map()
    elif choice == '2':
        show_inventory()
    elif choice == '3':
        save_game()
        main_menu()
    elif choice == '4':
        if load_game():
            main_menu()
        else:
            main_menu()
    elif choice == '5':
        print(Fore.YELLOW + "Дякуємо за гру! До зустрічі!")
        sys.exit()
    elif choice == '6':
        display_stats()
        main_menu()
    else:
        print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")
        main_menu()

# Перегляд інвентарю
def show_inventory():
    print(Fore.BLUE + "\nВаш інвентар:")
    if inventory:
        for item in inventory:
            print(f"{Fore.BLUE}- {item}")
    else:
        print(Fore.BLUE + "Інвентар порожній.")
    print("")
    main_menu()

# Карта світу
def world_map():
    print(Fore.CYAN + "\nВи стоїте на центральній площі Ельдорадо. Перед вами кілька шляхів:")
    print("1. Ліс")
    print("2. Гори")
    print("3. Печери")
    print("4. Місто")
    print("5. Переглянути характеристики")
    print("6. Переглянути інвентар")
    print("7. Повернутися до головного меню")
    choice = input(Fore.GREEN + "Куди ви хочете піти? (1-7): ").strip()
    if choice == '1':
        forest()
    elif choice == '2':
        mountains()
    elif choice == '3':
        caves()
    elif choice == '4':
        city()
    elif choice == '5':
        display_stats()
        world_map()
    elif choice == '6':
        show_inventory()
    elif choice == '7':
        main_menu()
    else:
        print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")
        world_map()

# Локація: Ліс
def forest():
    print(Fore.GREEN + "\nВи входите до густого лісу. Птахи співають, а сонячні промені пробиваються крізь крони дерев.")
    print("Ви бачите трьох шляхів:")
    print("1. Шлях до старого дуба")
    print("2. Стежка до водоспаду")
    print("3. Лісова поляна")
    print("4. Переглянути характеристики")
    print("5. Переглянути інвентар")
    print("6. Повернутися до карти світу")
    choice = input(Fore.GREEN + "Куди ви хочете піти? (1-6): ").strip()
    if choice == '1':
        old_oak()
    elif choice == '2':
        waterfall()
    elif choice == '3':
        forest_clearing()
    elif choice == '4':
        display_stats()
        forest()
    elif choice == '5':
        show_inventory()
    elif choice == '6':
        world_map()
    else:
        print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")
        forest()

# Локація: Старий дуб
def old_oak():
    print(Fore.YELLOW + "\nВи підходите до старого дуба. На дереві висить загадкова амулет.")
    print("1. Взяти амулет")
    print("2. Ігнорувати та йти далі")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Повернутися до лісу")
    choice = input(Fore.GREEN + "Ваш вибір: (1-5): ").strip()
    if choice == '1':
        if "Амулет сили" not in inventory:
            inventory.append("Амулет сили")
            player['attack'] += 2
            print(Fore.CYAN + "Ви взяли Амулет сили. Ваш атака збільшилася!")
        else:
            print(Fore.YELLOW + "У вас вже є цей амулет.")
    elif choice == '2':
        print(Fore.YELLOW + "Ви вирішили ігнорувати амулет і йти далі.")
    elif choice == '3':
        display_stats()
        old_oak()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        forest()
    else:
        print(Fore.RED + "Невірний вибір.")
        old_oak()
    forest()

# Локація: Водоспад
def waterfall():
    print(Fore.BLUE + "\nВи доходите до водоспаду. На його краю сидить мудрий старець.")
    print("Старець каже: 'Відповідай на моє запитання, і я надам тобі нагороду.'")
    riddle = "Що має серце, але не має крові?"
    print(Fore.CYAN + f"Загадка: {riddle}")
    answer = input(Fore.GREEN + "Твоя відповідь: ").strip().lower()
    if answer == 'серце':
        print(Fore.YELLOW + "Старець задоволений твоєю відповіддю і дарує тобі зілля здоров'я.")
        inventory.append("Зілля здоров'я")
    else:
        print(Fore.RED + "Неправильна відповідь. Старець іде геть.")
    print("\nДодаткові опції:")
    print("1. Повернутися до лісу")
    print("2. Переглянути характеристики")
    print("3. Переглянути інвентар")
    choice = input(Fore.GREEN + "Ваш вибір: (1-3): ").strip()
    if choice == '1':
        forest()
    elif choice == '2':
        display_stats()
        waterfall()
    elif choice == '3':
        show_inventory()
        waterfall()
    else:
        print(Fore.RED + "Невірний вибір.")
        waterfall()

# Локація: Лісова поляна
def forest_clearing():
    print(Fore.MAGENTA + "\nВи заходите на лісову поляну і бачите групу бандитів.")
    engage_battle("Бандитів", 30, 8)
    if "Амулет сили" in inventory and "Загублена лампа" in inventory and "Магічний кристал" in inventory:
        print(Fore.CYAN + "\nВи відчуваєте, що готові до фінальної битви!")
        final_challenge()
    else:
        print(Fore.CYAN + "\nВи повертаєтесь до лісу.")
        forest()

# Локація: Гори
def mountains():
    print(Fore.GREEN + "\nВи піднімаєтесь у гори. Повітря стає холоднішим, а краєвид захоплює дух.")
    print("Ви бачите дві стежки:")
    print("1. Стежка до вершини гори")
    print("2. Стежка до печери дракона")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Повернутися до карти світу")
    choice = input(Fore.GREEN + "Куди ви хочете піти? (1-5): ").strip()
    if choice == '1':
        mountain_peak()
    elif choice == '2':
        dragon_cave()
    elif choice == '3':
        display_stats()
        mountains()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        world_map()
    else:
        print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")
        mountains()

# Локація: Вершина гори
def mountain_peak():
    print(Fore.YELLOW + "\nВи досягаєте вершини гори і бачите прекрасний краєвид.")
    print("На вершині ви знаходите рідкісний артефакт.")
    if "Кристал мудрості" not in inventory:
        inventory.append("Кристал мудрості")
        player['experience'] += 50
        print(Fore.CYAN + "Ви взяли Кристал мудрості. Ваш досвід збільшився!")
    else:
        print(Fore.YELLOW + "У вас вже є цей артефакт.")
    print("\nДодаткові опції:")
    print("1. Повернутися до гір")
    print("2. Переглянути характеристики")
    print("3. Переглянути інвентар")
    choice = input(Fore.GREEN + "Ваш вибір: (1-3): ").strip()
    if choice == '1':
        mountains()
    elif choice == '2':
        display_stats()
        mountain_peak()
    elif choice == '3':
        show_inventory()
        mountain_peak()
    else:
        print(Fore.RED + "Невірний вибір.")
        mountain_peak()

# Локація: Печера дракона
def dragon_cave():
    print(Fore.RED + "\nВи входите до печери дракона. Дракон спить, але ви чуєте його важке дихання.")
    print("1. Спробувати красти скарби")
    print("2. Тихо відступити")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Повернутися до гір")
    choice = input(Fore.GREEN + "Ваш вибір: (1-5): ").strip()
    if choice == '1':
        if random.random() < 0.5:
            print(Fore.RED + "Дракон прокинувся і атакує вас!")
            engage_battle("Дракон", 100, 20)
            if player['hp'] > 0:
                inventory.append("Драконів скарб")
                player['experience'] += 50
                print(Fore.CYAN + "Ви отримали Драконів скарб та 50 досвіду.")
        else:
            print(Fore.YELLOW + "Ви змогли вкрасти частину скарбів без пробудження дракона.")
            inventory.append("Драконів скарб")
    elif choice == '2':
        print(Fore.YELLOW + "Ви вирішили уникнути конфлікту і повернулися назад.")
    elif choice == '3':
        display_stats()
        dragon_cave()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        mountains()
    else:
        print(Fore.RED + "Невірний вибір.")
        dragon_cave()
    mountains()

# Локація: Печери
def caves():
    print(Fore.GREEN + "\nВи входите до темних печер. Світло факела мерехтить на стінах.")
    print("Ви бачите дві тунелі:")
    print("1. Тунель до підземного озера")
    print("2. Тунель до лабіринту")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Повернутися до карти світу")
    choice = input(Fore.GREEN + "Куди ви хочете піти? (1-5): ").strip()
    if choice == '1':
        underground_lake()
    elif choice == '2':
        labyrinth()
    elif choice == '3':
        display_stats()
        caves()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        world_map()
    else:
        print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")
        caves()

# Локація: Підземне озеро
def underground_lake():
    print(Fore.BLUE + "\nВи знаходите підземне озеро зі світлими кристалами.")
    print("На березі ви бачите чарівну рибу.")
    print("1. Спробувати впіймати рибу")
    print("2. Ігнорувати і йти далі")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Повернутися до печер")
    choice = input(Fore.GREEN + "Ваш вибір: (1-5): ").strip()
    if choice == '1':
        if random.random() < 0.5:
            print(Fore.YELLOW + "Ви впіймали чарівну рибу, яка дарує вам зілля здоров'я.")
            inventory.append("Зілля здоров'я")
        else:
            print(Fore.RED + "Риба втікла, і ви не отримали нічого.")
    elif choice == '2':
        print(Fore.YELLOW + "Ви вирішили ігнорувати рибу і йти далі.")
    elif choice == '3':
        display_stats()
        underground_lake()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        caves()
    else:
        print(Fore.RED + "Невірний вибір.")
        underground_lake()
    caves()

# Локація: Лабіринт
def labyrinth():
    print(Fore.MAGENTA + "\nВи заходите до лабіринту. Тут темно і складно орієнтуватися.")
    print("Ви натрапляєте на ворота з таємним кодом.")
    code = "1234"
    attempts = 3
    while attempts > 0:
        guess = input(Fore.GREEN + "Введіть код: ").strip()
        if guess == code:
            print(Fore.YELLOW + "Ви розгадали код і відкрили ворота. Залишає вас безпечним.")
            break
        else:
            attempts -= 1
            print(Fore.RED + f"Невірний код. Залишилось спроб: {attempts}")
    if attempts == 0:
        print(Fore.RED + "Ви не змогли розгадати код і застрягли в лабіринті.")
    print("\nДодаткові опції:")
    print("1. Повернутися до печер")
    print("2. Переглянути характеристики")
    print("3. Переглянути інвентар")
    choice = input(Fore.GREEN + "Ваш вибір: (1-3): ").strip()
    if choice == '1':
        caves()
    elif choice == '2':
        display_stats()
        labyrinth()
    elif choice == '3':
        show_inventory()
        labyrinth()
    else:
        print(Fore.RED + "Невірний вибір.")
        labyrinth()

# Локація: Місто
def city():
    print(Fore.CYAN + "\nВи приходите до міста Ельдорадо. Тут кипить життя, і є багато можливостей.")
    print("Ви бачите кілька місць:")
    print("1. Крамниця")
    print("2. Гільдія воїнів")
    print("3. Маяк")
    print("4. Магічний університет")
    print("5. Переглянути характеристики")
    print("6. Переглянути інвентар")
    print("7. Повернутися до карти світу")
    choice = input(Fore.GREEN + "Куди ви хочете піти? (1-7): ").strip()
    if choice == '1':
        shop()
    elif choice == '2':
        guild()
    elif choice == '3':
        lighthouse()
    elif choice == '4':
        magic_university()
    elif choice == '5':
        display_stats()
        city()
    elif choice == '6':
        show_inventory()
    elif choice == '7':
        world_map()
    else:
        print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")
        city()

# Локація: Крамниця
def shop():
    print(Fore.YELLOW + "\nВи заходите до крамниці. Тут продають різні предмети.")
    print("1. Купити зілля здоров'я (50 золотих)")
    print("2. Купити меч (100 золотих)")
    print("3. Купити щит (80 золотих)")
    print("4. Переглянути характеристики")
    print("5. Переглянути інвентар")
    print("6. Вийти з крамниці")
    choice = input(Fore.GREEN + "Ваш вибір: (1-6): ").strip()
    if choice == '1':
        print(Fore.YELLOW + "Ви купили зілля здоров'я.")
        inventory.append("Зілля здоров'я")
    elif choice == '2':
        print(Fore.YELLOW + "Ви купили меч. Ваш атака збільшилася.")
        player['attack'] += 5
    elif choice == '3':
        print(Fore.YELLOW + "Ви купили щит. Ваш захист збільшився.")
        player['defense'] += 5
    elif choice == '4':
        display_stats()
        shop()
    elif choice == '5':
        show_inventory()
    elif choice == '6':
        print(Fore.YELLOW + "Ви вийшли з крамниці.")
        city()
    else:
        print(Fore.RED + "Невірний вибір.")
        shop()
    city()

# Локація: Гільдія воїнів
def guild():
    print(Fore.BLUE + "\nВи заходите до Гільдії воїнів. Тут можна взяти квести або тренуватися.")
    print("1. Взяти квест")
    print("2. Тренуватися")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Вийти з гільдії")
    choice = input(Fore.GREEN + "Ваш вибір: (1-5): ").strip()
    if choice == '1':
        take_quest()
    elif choice == '2':
        train()
    elif choice == '3':
        display_stats()
        guild()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        print(Fore.YELLOW + "Ви вийшли з гільдії.")
        city()
    else:
        print(Fore.RED + "Невірний вибір.")
        guild()
    city()

# Взяти квест
def take_quest():
    print(Fore.CYAN + "\nГільдія воїнів просить вас знищити групу гоблінів, що тероризують околиці.")
    print("1. Прийняти квест")
    print("2. Відмовитися")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    choice = input(Fore.GREEN + "Ваш вибір: (1-4): ").strip()
    if choice == '1':
        if "Гоблінів" not in player['quests_completed']:
            print(Fore.YELLOW + "Ви вирушаєте на пошуки гоблінів.")
            engage_battle("Гоблінів", 40, 10)
            if player['hp'] > 0:
                player['experience'] += 20
                player['quests_completed'].append("Гоблінів")
                print(Fore.CYAN + "Ви отримали 20 досвіду за перемогу.")
                check_final_challenge()
        else:
            print(Fore.YELLOW + "Ви вже виконали цей квест.")
    elif choice == '2':
        print(Fore.YELLOW + "Ви відмовились від квесту.")
    elif choice == '3':
        display_stats()
        take_quest()
    elif choice == '4':
        show_inventory()
    else:
        print(Fore.RED + "Невірний вибір.")
        take_quest()
    guild()

# Тренування
def train():
    print(Fore.YELLOW + "\nВи проводите тренування і підвищуєте свої навички.")
    player['attack'] += 2
    player['defense'] += 1
    player['experience'] += 10
    print(Fore.CYAN + "Ваш атака та захист збільшилися. Ви отримали 10 досвіду.")
    guild()

# Локація: Маяк
def lighthouse():
    print(Fore.MAGENTA + "\nВи підходите до маяка. Тут живе старий маячник.")
    print("Маячник просить вас допомогти знайти загублену лампу.")
    print("1. Прийняти завдання")
    print("2. Відмовитися")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Повернутися до міста")
    choice = input(Fore.GREEN + "Ваш вибір: (1-5): ").strip()
    if choice == '1':
        find_lamp()
    elif choice == '2':
        print(Fore.YELLOW + "Ви відмовились від завдання.")
    elif choice == '3':
        display_stats()
        lighthouse()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        city()
    else:
        print(Fore.RED + "Невірний вибір.")
        lighthouse()
    city()

# Знайти лампу
def find_lamp():
    print(Fore.GREEN + "\nВи вирушаєте на пошуки загубленої лампи.")
    print("Ви знаходите її у старій печері, але там охороняє її кам'яний голем.")
    engage_battle("Кам'яного голема", 60, 15)
    if player['hp'] > 0:
        if "Загублена лампа" not in inventory:
            print(Fore.YELLOW + "Ви забрали лампу і повернулися до маяка.")
            inventory.append("Загублена лампа")
            player['experience'] += 30
            print(Fore.CYAN + "Ви отримали 30 досвіду за виконання завдання.")
            check_final_challenge()
        else:
            print(Fore.YELLOW + "Ви вже маєте загублену лампу.")
    lighthouse()
    city()

# Локація: Магічний університет
def magic_university():
    print(Fore.MAGENTA + "\nВи заходите до Магічного університету. Тут можна вивчати магію або брати магічні квести.")
    print("1. Вивчати магію")
    print("2. Взяти магічний квест")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Повернутися до міста")
    choice = input(Fore.GREEN + "Ваш вибір: (1-5): ").strip()
    if choice == '1':
        study_magic()
    elif choice == '2':
        magic_quest()
    elif choice == '3':
        display_stats()
        magic_university()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        city()
    else:
        print(Fore.RED + "Невірний вибір.")
        magic_university()
    magic_university()

# Вивчати магію
def study_magic():
    print(Fore.CYAN + "\nВи проводите час у навчанні магії.")
    player['attack'] += 3
    player['defense'] += 2
    player['experience'] += 30
    print(Fore.CYAN + "Ваші магічні навички покращилися. Ви отримали 30 досвіду.")
    magic_university()

# Магічний квест
def magic_quest():
    print(Fore.CYAN + "\nМагічний університет просить вас знайти зниклий магічний кристал.")
    print("1. Прийняти квест")
    print("2. Відмовитися")
    print("3. Переглянути характеристики")
    print("4. Переглянути інвентар")
    print("5. Повернутися до університету")
    choice = input(Fore.GREEN + "Ваш вибір: (1-5): ").strip()
    if choice == '1':
        if "Магічного стража" not in player['quests_completed']:
            print(Fore.YELLOW + "Ви вирушаєте на пошуки магічного кристала.")
            engage_battle("Магічного стража", 50, 12)
            if player['hp'] > 0:
                inventory.append("Магічний кристал")
                player['experience'] += 40
                player['quests_completed'].append("Магічного стража")
                print(Fore.CYAN + "Ви знайшли Магічний кристал та отримали 40 досвіду.")
                check_final_challenge()
        else:
            print(Fore.YELLOW + "Ви вже виконали цей магічний квест.")
    elif choice == '2':
        print(Fore.YELLOW + "Ви відмовились від магічного квесту.")
    elif choice == '3':
        display_stats()
        magic_quest()
    elif choice == '4':
        show_inventory()
    elif choice == '5':
        magic_university()
    else:
        print(Fore.RED + "Невірний вибір.")
        magic_quest()
    magic_university()

# Локація: Фінальна битва
def final_challenge():
    print(Fore.CYAN + "\nВи досягаєте кінцевої точки вашої подорожі.")
    print("Перед вами вибір:")
    print("1. Залишитися героєм Ельдорадо")
    print("2. Повернутися додому")
    choice = input(Fore.GREEN + "Ваш вибір: (1/2): ").strip()
    if choice == '1':
        print(Fore.YELLOW + "Ви залишаєтеся героєм Ельдорадо, захищаючи його від загроз.")
        print(Fore.CYAN + "Вітаємо! Ви завершили гру з перемогою.")
    elif choice == '2':
        print(Fore.YELLOW + "Ви вирішили повернутися додому з багатим досвідом та скарбами.")
        print(Fore.CYAN + "Вітаємо! Ви завершили гру з успіхом.")
    else:
        print(Fore.RED + "Невірний вибір.")
        final_challenge()
    sys.exit()

# Бої
def engage_battle(enemy, enemy_hp, enemy_attack):
    print(Fore.RED + f"\nБитва з {enemy} почалася!")
    while enemy_hp > 0 and player['hp'] > 0:
        print(Fore.CYAN + f"\nВаші HP: {player['hp']}")
        print(Fore.CYAN + f"HP {enemy}: {enemy_hp}")
        print("1. Атакувати")
        print("2. Використати зілля")
        print("3. Втекти")
        print("4. Переглянути характеристики")
        print("5. Переглянути інвентар")
        choice = input(Fore.GREEN + "Ваш вибір: (1-5): ").strip()
        if choice == '1':
            damage = player['attack'] - random.randint(0, enemy_attack//2)
            damage = max(damage, 0)
            enemy_hp -= damage
            print(Fore.YELLOW + f"Ви нанесли {damage} шкоди {enemy}.")
        elif choice == '2':
            if "Зілля здоров'я" in inventory:
                player['hp'] += 30
                inventory.remove("Зілля здоров'я")
                print(Fore.YELLOW + "Ви використали зілля здоров'я. Ваші HP відновлено на 30.")
            else:
                print(Fore.RED + "У вас немає зілля здоров'я.")
                continue
        elif choice == '3':
            if random.random() < 0.5:
                print(Fore.YELLOW + "Ви успішно втекли від битви.")
                return
            else:
                print(Fore.RED + "Втеча не вдалася. Битва продовжується.")
        elif choice == '4':
            display_stats()
            continue
        elif choice == '5':
            show_inventory()
            continue
        else:
            print(Fore.RED + "Невірний вибір.")
            continue

        if enemy_hp > 0:
            enemy_damage = enemy_attack - player['defense']
            enemy_damage = max(enemy_damage, 0)
            player['hp'] -= enemy_damage
            print(Fore.RED + f"{enemy} наніс вам {enemy_damage} шкоди.")

    if player['hp'] > 0:
        print(Fore.GREEN + f"Ви перемогли {enemy}!")
    else:
        print(Fore.RED + "Ви загинули. Гра закінчена.")
        sys.exit()

# Перевірка умов для фінальної битви
def check_final_challenge():
    # Вимога: Виконати два квести та зібрати ключові предмети
    required_quests = ["Гоблінів", "Магічного стража"]
    required_items = ["Амулет сили", "Загублена лампа", "Магічний кристал"]
    if all(quest in player['quests_completed'] for quest in required_quests) and all(item in inventory for item in required_items):
        print(Fore.CYAN + "\nВи відчуваєте, що готові до фінальної битви!")
        final_challenge()

# Перевірка рівня
def check_level_up():
    level_up_experience = player['level'] * 100
    if player['experience'] >= level_up_experience:
        player['level'] += 1
        player['experience'] -= level_up_experience
        player['hp'] += 20
        player['attack'] += 5
        player['defense'] += 3
        print(Fore.GREEN + f"\nВітаємо! Ви досягли рівня {player['level']}!")
        display_stats()

# Головна функція гри
def main():
    if os.path.exists(game_file):
        load = input(Fore.GREEN + "Ви хочете завантажити останнє збереження? (так/ні): ").strip().lower()
        if load == 'так':
            if not load_game():
                create_character()
        else:
            create_character()
    else:
        create_character()
    while True:
        check_level_up()
        main_menu()

if __name__ == "__main__":
    main()
