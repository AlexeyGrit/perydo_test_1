import random


def roll_dice(num_dice):
    "Иницилизируем указанное количество костей"
    dice = []
    for _ in range(num_dice):
        dice.append(random.randint(1, 6))
    return dice


def make_bet(previous_bet):
    "Делаем ставку и возвращает новую ставку"
    new_bet = input("Сделайте свою ставку (число и номинал): ")
    while True:
        try:
            count, value = new_bet.split()
            count = int(count)
            value = int(value)
            if previous_bet is not None:
                prev_count, prev_value = previous_bet.split()
                prev_count = int(prev_count)
                prev_value = int(prev_value)
                if count < prev_count or (count == prev_count and value <= prev_value):
                    raise ValueError("Некорректная ставка. Попробуйте еще раз.")
            break
        except ValueError:
            print("Некорректный ввод! Попробуйте еще раз.")
            new_bet = input("Сделайте свою ставку (число и номинал): ")

    return new_bet


def play_round(num_dice_1, num_dice_2):
    dice_1 = roll_dice(num_dice_1)
    dice_2 = roll_dice(num_dice_2)
    print("Выпавшие значения костей первого игрока:", dice_1)
    print("Выпавшие значения костей второго игрока:", dice_2)

    bet = make_bet(None)

    while True:
        action = input("Выберите действие (1 - 'не верю', 2 - сделать ставку): ")

        if action == '1':
            # Если не верит
            previous_count, previous_value = bet.split()
            previous_count = int(previous_count)
            previous_value = int(previous_value)
            count_1 = dice_1.count(previous_value)
            count_2 = dice_2.count(previous_value)
            total_count = count_1 + count_2
            if total_count < previous_count:
                print("Первый игрок проиграл!")
                num_dice_1 -= 1
            else:
                print("Второй игрок проиграл!")
                num_dice_2 -= 1
            break
        elif action == '2':
            new_bet = make_bet(bet)
            bet = new_bet
        else:
            print("Некорректный выбор! Попробуйте еще раз.")

    print("Количество кубиков первого игрока:", num_dice_1)
    print("Количество кубиков второго игрока:", num_dice_2)

    # Играем до тех пор, пока у одного из игроков не закончатся кубики
    if num_dice_1 > 0 and num_dice_2 > 0:
        play_round(num_dice_1, num_dice_2)

    # Объявляем победителя
    if num_dice_1 == 0:
        print("Игра окончена. Победил первый игрок!")
    else:
        print("Игра окончена. Победил второй игрок!")


# Иницилизируем количество кубиков
num_dice_1 = 5
num_dice_2 = 5

play_round(num_dice_1, num_dice_2)
#Кирилл красивый