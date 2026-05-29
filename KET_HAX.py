import random
import os
import time
import sys
import keyboard
import json

def show_logo():
    print("""
esc для пропуска
██╗░░██╗███████╗████████╗░░░░░░░░░██╗░░██╗░█████╗░██╗░░██╗
██║░██╔╝██╔════╝╚══██╔══╝░░░░░░░░░██║░░██║██╔══██╗╚██╗██╔╝
█████╔╝░█████╗░░░░░██║░░░░░░░░░░░░███████║███████║░╚███╔╝░
██╔═██╗░██╔══╝░░░░░██║░░░░░░░░░░░░██║░░██║██╔══██║░██╔██╗░
██║░░██╗███████╗░░░██║░░███████╗░░██║░░██║██║░░██║██║░╚██╗
╚═╝░░╚═╝╚══════╝░░░╚═╝░░╚══════╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
""")

def clear_screen_with_logo():
    os.system("cls")  
    show_logo()

show_logo()

spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧"]

skip_loading = False

for _ in range(15):
    for s in spinner:
        if keyboard.is_pressed('esc'):
            skip_loading = True
            break
        
        sys.stdout.write(f"\r {s} Загрузка {s} ")
        sys.stdout.flush()
        time.sleep(0.05)
        
    if skip_loading: 
        break

print("\n\nГОТОВО!!!")
time.sleep(0.5)
os.system("cls")
lvl = 0
day = 0
count = 0
money = 25000
reputation = 0
cheat_ON = False
utilities_shop = {

    "скрипт-кидди кликер": {
        "money": 1200,
        "atk_bonus": 15,
        "ram_cost": 5
    },
    
    "троян-вымогатель ransomware": {
        "money": 5500,
        "atk_bonus": 60,
        "ram_cost": 30
    },
    
    
    "деструктор логов cc-cleaner": {
        "money": 3000,
        "trace_reduction": 35,
        "ram_cost": 15
    }
}

servers_shop = {
   
    "доп модуль ram (16gb)": {
        "money": 2000,
        "max_ram_bonus": 20,
        "quantity_buy": 0
    },
    
    
    "абузоустойчивый vps": {
        "money": 7000,
        "max_ram_bonus": 50,
        "quantity_buy": 0
    },
    
    
    "процессор katarina-9": {
        "money": 12000,
        "exp_multiplier": 2,
        "quantity_buy": 0 
    }
}

stats_player = {
    'Trace%': 100,
    'RAM': 100
}
VPN = {

    "маск сеть": {
        "money": 500,
        "defense": 10,
        "quantity_buy": 0,
        "time_hacking": 1
    },
    
    
    "VPN": {
        "money": 3500,
        "defense": 45,
        "quantity_buy": 0,
        "time_hacking": 3
    },
    
    
    "собственый днс": {
        "money": 1500,
        "defense": 20,
        "quantity_buy": 0,
        "time_hacking": 5
    },
    

    "собственый прокси сервер": {
        "money": 8000,
        "defense": 70,
        "quantity_buy": 0,
        "time_hacking": 50
    }
}

utilities = {}
def save_load_system(action):
    global lvl, day, money, reputation, cheat_ON, stats_player, utilities, VPN, servers_shop
    file_name = "savegame.json"
    
    if action == "save":
        
        save_data = {
            "lvl": lvl, "day": day, "money": money, "reputation": reputation, "cheat_ON": cheat_ON,
            "stats_player": stats_player, "utilities": utilities, "VPN": VPN, "servers_shop": servers_shop
        }
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(save_data, f, ensure_ascii=False, indent=4)
            print("=== СИСТЕМА: Игра успешно сохранена! ===")
            time.sleep(1.5)
        except Exception as e:
            print(f"Ошибка сохранения: {e}"); time.sleep(2)
            
    elif action == "load":
        if not os.path.exists(file_name):
            print("=== СИСТЕМА: Файл сохранений не найден! ===")
            time.sleep(1.5)
            return False
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            lvl, day, money, reputation, cheat_ON = data["lvl"], data["day"], data["money"], data["reputation"], data["cheat_ON"]
            stats_player, utilities, VPN, servers_shop = data["stats_player"], data["utilities"], data["VPN"], data["servers_shop"]
            print("=== СИСТЕМА: Сохранение успешно загружено! ===")
            time.sleep(1.5)
            return True
        except Exception as e:
            print(f"Ошибка загрузки: {e}"); time.sleep(2)
            return False

def darknet_shop():
    global money, utilities, stats_player
    
    while True:
        os.system("cls")
        print(f"""
======================================
         money: {money}
======================================
1.Утилиты для взлома
2.ВПН
3.Сервера
4.Выйти из Даркнета
""")
        try:
            
            category_choice = int(input("Выберите категорию (1-4): "))
            
            if category_choice == 4:
                break
                
            if category_choice == 1:
                os.system("cls")
                for name, info in utilities_shop.items():
                    print(f"\nИнструмент: {name}")
                    print(f"Стоимость: {info['money']} $")
                    print(f"Жрёт RAM: {info['ram_cost']}")
                    if "atk_bonus" in info:
                        print(f"[ СИСТЕМА АТАКИ ]: Наносит +{info['atk_bonus']} урона по серверу")
                    if "trace_reduction" in info:
                        print(f"[ БЕЗОПАСНОСТЬ ]: Снижает уровень Trace% на {info['trace_reduction']}%")
                
                darknet_input = input("\nЧто хотите купить?\n///  ").lower().strip()
                
                if darknet_input in utilities_shop:
                    try:
                        darknet_input_ = int(input("Сколько хотите купить штук?\n///  "))
                        if darknet_input_ <= 0: continue
                    except ValueError:
                        print("Вводите числами!"); time.sleep(1); continue
                        
                    total = utilities_shop[darknet_input]["money"] * darknet_input_
                    
                    if money >= total:
                        money -= total
                        
                        if darknet_input in utilities:
                            utilities[darknet_input] += darknet_input_
                        else:
                            utilities[darknet_input] = darknet_input_
                        print(f"Вы купили {darknet_input} | Количество: {darknet_input_} | Всего: {total}$")
                        time.sleep(2)
                    else:
                        print("У вас не хватает денег!"); time.sleep(1)
                else:
                    print("Такого софта нет."); time.sleep(1)

            
            elif category_choice == 2:
                os.system("cls")
                count = 0
                for name, info in VPN.items():
                    count += 1
                    print(f"{count}. {name} | Стоимость: {info['money']} | Замедление: {info['time_hacking']} | Куплено ip: {info['quantity_buy']}")
                
                darknet_input = input("\nЧто хотите купить?\n///  ").lower().strip()
                
                if darknet_input in VPN:
                    try:
                        darknet_input_ = int(input("Сколько хотите купить ip адресов?\n///  "))
                        if darknet_input_ <= 0: continue
                    except ValueError:
                        print("Вводите числами!"); time.sleep(1); continue
                        
                    total = VPN[darknet_input]["money"] * darknet_input_
                    
                    if money >= total:
                        money -= total
                        VPN[darknet_input]["quantity_buy"] += darknet_input_
                        print(f"Вы купили {darknet_input} | ip адресов: {darknet_input_} | За {total}$")
                        time.sleep(2)
                    else:
                        print("У вас не хватает денег!"); time.sleep(1)
                else:
                    print("Этого нет."); time.sleep(1)

            elif category_choice == 3:
                os.system("cls")
                print("=== МАГАЗИН ЖЕЛЕЗА И СЕРВЕРОВ ===")
                for name, info in servers_shop.items():
                    print(f"\nКомпонент: {name.upper()}")
                    print(f"Цена: {info['money']} $")
                    print(f"Уже куплено: {info['quantity_buy']} шт.")
                    if "max_ram_bonus" in info:
                        print(f"[ МОДЕРНИЗАЦИЯ ПАМЯТИ ]: Увеличивает максимальный объем RAM на +{info['max_ram_bonus']} ед.")
                    if "exp_multiplier" in info:
                        print(f"[ ВЫЧИСЛИТЕЛЬНАЯ МОЩНОСТЬ ]: Удваивает получаемый опыт (XP x{info['exp_multiplier']})")
                        if info['quantity_buy'] >= 1:
                            print("[ СТАТУС ]: ДАННЫЙ ПРОЦЕССОР УЖЕ УСТАНОВЛЕН В ВАШ ПК")
                            
                darknet_input = input("\nЧто хотите купить?\n///  ").lower().strip()
                
                if darknet_input in servers_shop:
                    item = servers_shop[darknet_input]
                    
                    
                    if "exp_multiplier" in item and item["quantity_buy"] >= 1:
                        print("Вы не можете купить второй процессор!"); time.sleep(2)
                        continue
                        
                    if "exp_multiplier" in item:
                        darknet_input_ = 1
                    else:
                        try:
                            darknet_input_ = int(input("Сколько хотите купить единиц железа?\n///  "))
                            if darknet_input_ <= 0: continue
                        except ValueError:
                            print("Вводите числами!"); time.sleep(1); continue
                            
                    total = item["money"] * darknet_input_
                    
                    if money >= total:
                        money -= total
                        item["quantity_buy"] += darknet_input_
                        print(f"Вы успешно купили {darknet_input} в количестве {darknet_input_} шт. Списано {total}$.")
                        time.sleep(2)
                    else:
                        print("У вас не хватает денег!"); time.sleep(1)
                else:
                    print("Такого компонента нет."); time.sleep(1)
                    
            else:
                print("Число вне диапазона (1-4)"); time.sleep(1)
                
        except ValueError:
            print("Вводите числами!"); time.sleep(1)
            
def menu():
    global stats_player, money
    while True:
        print("""
1.продолжить
2.новая игра
3.читы (доступны после взлома секретного уровня)
4.выйти
""")
        try:
            menu_input = int(input("///"))
        except ValueError:
            print("Вводите числами")
            continue
        if menu_input == 1:
            if save_load_system("load"):
                house()
        elif menu_input == 2:
            print("здраствуйте мы кибергуперковка KET_HAX мы хотим предложить \nвам работу в нашей организации ваши задачи мы раскажим\nесли захотите прейсойдинится? (да, нет, мои сохранения)")
            while True:
                hi_player = input("///  ").lower().strip()
                if hi_player == "да":
                    print("завтра начнём")
                    house()
                elif hi_player == "нет":
                    print("понимаем... ")
                    break
                elif hi_player == "мои сохранения":
                    if save_load_system("load"):
                        house()
                else:
                    print("что? (да, нет, мои сохранения)")
        if menu_input == 3:
            if cheat_ON == True:
                print("""
1.RAM+
2.Trace%+
3.monuy+
""")
                try:
                    cheat_input = int(input("///  "))
                    cheat_input_ = int(input("сколько вы это-го хотите\n///  "))
                except ValueError:
                    print("Вводите числами!!!")
                    continue
                cheat_input_ = int(input("сколько вы это-го хотите\n///  "))
                if cheat_input == 1:
                    stats_player["RAM"] += cheat_input_
                if cheat_input == 2:
                    stats_player["Trace%"] += cheat_input_
                if cheat_input == 3:
                    money += cheat_input_
            else:
                print("пройдите секретный уровень!!!")
        elif menu_input == 4:
            break
                

def trace_scan():
    
    filled = stats_player["Trace%"] // 10
    return f"[ {'░' * (10 - filled)}{'█' * filled} ] {stats_player['Trace%']}%"
    
def gameplay(servers_HP, money_):
    global lvl, money, reputation, stats_player, utilities, VPN
    

    total_defense = 0
    for vpn_name, vpn_info in VPN.items():
        total_defense += vpn_info["defense"] * vpn_info["quantity_buy"]
        
    
    max_ram = 100
    if "доп модуль ram (16gb)" in servers_shop:
        max_ram += servers_shop["доп модуль ram (16gb)"]["quantity_buy"] * 20
    if "абузоустойчивый vps" in servers_shop:
        max_ram += servers_shop["абузоустойчивый vps"]["quantity_buy"] * 50
        
    
    stats_player["RAM"] = max_ram
    stats_player["Trace%"] = 0
    
    is_blocking = False
    is_evading = False
    
    while servers_HP > 0 and stats_player["Trace%"] < 100:
        os.system("cls")
        print(f"""
================================================================
            SERVER HACKING OVERRIDE: {servers_HP} HP                       
================================================================
                                                
================================================================
     Trace%: {trace_scan()} | RAM: {stats_player['RAM']}/{max_ram}      
================================================================
1. Базовая атака    (RAM: 20)  |  5. Использовать утилиты из инвентаря
2. Блокировать порт (RAM: 10)  |  [Блок режет урон сервера на 70%]
3. Прокси-уклонение (RAM: 15)  |  [50% шанс полностью уйти от слежки]
4. Сбросить кэш     (RAM: +30) |  [Пропуск хода, Trace% растет]
0. Разорвать соединение (Экстренный выход)
""")
        action = input("Ввод директивы /// ").strip()
        
        if action == "0":
            print("Соединение разорвано! Логи стёрты. Данные утеряны."); time.sleep(1.5)
            return
            
        
        server_attack = random.randint(12, 22)
        
        server_attack = max(2, server_attack - total_defense)
        
        
        if action == "1":
            if stats_player["RAM"] >= 20:
                stats_player["RAM"] -= 20
                dmg = random.randint(20, 35)
                servers_HP -= dmg
                print(f"-> Нападение успешно! Нанесено {dmg} деструктивного урона серверам.")
            else:
                print("Недостаточно RAM для атаки!"); time.sleep(1.2); continue
                
        elif action == "2":
            if stats_player["RAM"] >= 10:
                stats_player["RAM"] -= 10
                is_blocking = True
                print("-> Запущен брандмауэр. Порты заблокированы для сканеров сервера.")
            else:
                print("Недостаточно RAM для блокировки!"); time.sleep(1.2); continue
                
        elif action == "3":
            if stats_player["RAM"] >= 15:
                stats_player["RAM"] -= 15
                is_evading = True
                print("-> Трафик пущен по ложному следу. Включен режим уклонения.")
            else:
                print("Недостаточно RAM для уклонения!"); time.sleep(1.2); continue
                
        elif action == "4":
            stats_player["RAM"] = min(max_ram, stats_player["RAM"] + 30)
            print("-> Очистка буфера выполнена. Восстановлено +30 единиц RAM.")
            
        elif action == "5":
            if not utilities:
                print("Ваш инвентарь утилит пуст! Купите софт в Даркнете."); time.sleep(1.5); continue
            
            print("\n--- ВАШ ИНВЕНТАРЬ УТИЛИТ ---")
            for idx, (ut_name, ut_count) in enumerate(utilities.items(), 1):
                print(f"{idx}. {ut_name} (В наличии: {ut_count} шт.)")
            print("0. Назад")
            
            try:
                ut_choice = int(input("Какую утилиту активировать? "))
                if ut_choice == 0: continue
                
                
                selected_name = list(utilities.keys())[ut_choice - 1]
                ut_data = utilities_shop[selected_name]
                
                if stats_player["RAM"] >= ut_data["ram_cost"]:
                    stats_player["RAM"] -= ut_data["ram_cost"]
                    
                    
                    if "atk_bonus" in ut_data:
                        servers_HP -= ut_data["atk_bonus"]
                        print(f"Активирован {selected_name}! Нанесено {ut_data['atk_bonus']} урона.")
                    
                    if "trace_reduction" in ut_data:
                        stats_player["Trace%"] = max(0, stats_player["Trace%"] - ut_data["trace_reduction"])
                        print(f"Логи очищены через {selected_name}! Снижено {ut_data['trace_reduction']}% слежки.")
                        
                    
                    utilities[selected_name] -= 1
                    if utilities[selected_name] <= 0:
                        del utilities[selected_name]
                else:
                    print("Не хватает RAM для запуска утилиты!"); time.sleep(1.5); continue
            except:
                print("Ошибка ввода софта!"); time.sleep(1); continue
        else:
            print("Неверная команда терминала."); time.sleep(1); continue
            
        
        if servers_HP > 0:
            if is_blocking:
                server_attack = max(1, int(server_attack * 0.3))
                is_blocking = False
            if is_evading:
                is_evading = False
                if random.random() < 0.5:
                    print("УСПЕХ! Прокси полностью скрыл ваш IP от сканера сервера на этом ходу!"); server_attack = 0
                else:
                    print("ПРОВАЛ! Сервер отследил подмену пакетов.")
                    
            stats_player["Trace%"] += server_attack
            print(f"📡 Агенты кибербезопасности продвинулись в вашем поиске на +{server_attack}%")
            time.sleep(2)

    
    os.system("cls")
    if stats_player["Trace%"] >= 100:
        print("================================================================")
        print("ВАС ВЫЧИСЛИЛИ! Локальные жесткие диски заблокированы ФСБ")
        print("================================================================")
        print("Вы проиграли эту миссию. Штраф за очистку логов: -5,000$")
        money = max(0, money - 5000)
        time.sleep(4)
    elif servers_HP <= 0:
        
        xp_gain = 1
        if "процессор katarina-9" in servers_shop and servers_shop["процессор katarina-9"]["quantity_buy"] >= 1:
            xp_gain = servers_shop["процессор katarina-9"]["exp_multiplier"]
            
        lvl += xp_gain
        money += money_
        reputation += random.randint(5, 15)
        
        print("================================================================")
        print("СЕРВЕР ВЗЛОМАН! Доступ к корневой системе (ROOT) получен!")
        print("================================================================")
        print(f"Награда за контракт: +{money_}\$")
        print(f"Получено опыта: +{xp_gain} LVL | Текущий уровень: {lvl}")
        time.sleep(4)


def quests():
    global cheat_ON
    complexity = ["low","medium","High","impossible"]
    count = 0
    for complexity_ in complexity:
        count += 1
        print(f"{count}. {complexity_}")
    count = 0
    while True:
        try:
            choice_complexity = int(input("///  "))
            if choice_complexity == 1:
                os.system("cls")
                gameplay(100,random.randint(10000,50000))
                break
            elif choice_complexity == 2:
                if lvl == 5:
                    os.system("cls")
                    gameplay(1000,random.randint(100000,750000))
                    break
                else:
                    print("вы слишком малы что-бы взламывать компании")
            elif choice_complexity == 3:
                if lvl == 10:
                    os.system("cls")
                    gameplay(2500,random.randint(1000000,7000000))
                    break
                else:
                    print("вы слишком малы что-бы взламывать большие компании")
            elif choice_complexity == 4:
                if lvl == 20:
                    os.system("cls")
                    gameplay(5000,random.randint(5000000,10000000))
                    break
                else:
                    print("вы слишком малы для правительственных серверов")
            elif choice_complexity == 5 and lvl == 30:
                    os.system("cls")
                    print("поздравляем вы нашли секретный уровень: пк KET_KAT")
                    gameplay(100000,random.randint(100000000,700000000))
                    print("все думали что это невозможно")
                    cheat_ON = True
                    break
            else:
                print("число вне диапозона")
        except ValueError:
            print('Вводите числами!!!')
        
        
    
        
def house():
    global day, reputation
    print(f"""
========================================
день: {day} репутация: {reputation}
========================================
1.залесть в даркнет
2.лечь спать
3.пойти взламовать сервера
9.меню
0.выйти
""")
    while True:
        try:
            house_input = int(input("///  "))
            if house_input == 1:
                darknet_shop()
            elif house_input == 2:
                if day == 0 and money == 25000:
                    print("нет я должен закупится базовым софтом!")
                    darknet_shop()
                else:
                    save_load_system("save")
                    day += 1
                    break
            elif house_input == 3:
                if day == 0 and money != 25000:
                    quests()
                else:
                    print("нет я должен закупится базовым софтом!")
                    darknet_shop()
            elif house_input == 9:
                menu()
            elif house_input == 0:
                break
            else:
                print("число вне диапозона")
        except:
            print("вводите числами")

if __name__ == "__main__":
    menu()