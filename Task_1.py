# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

def min_flips(coins):
    heads = coins.count("H") + coins.count("h")
    tails = coins.count("T") + coins.count("t")
    return min(heads, tails)


n = int(input("Введите количество монеток: "))
coins_input = input("Введите состояние монеток (H/h для герба, T/t для решки), через пробел или без: ")


coins = ''.join(coins_input.split()).upper()


if len(coins) != n:
    print("Неверный ввод.")
else:
    print(min_flips(coins))

