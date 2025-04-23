print("Вітаємо у калькуляторі витрат на подорож!")

while True:
    while True:
        try:
            distance = int(input("Введіть відстань до пункту призначення (км): "))
            if distance > 0:
                break
            else:
                print("Некоректне значення")
        except ValueError:
            print("Помилка: введіть ціле число")

    while True:
        try:
            fuel_vytraty = float(input("Введіть середню витрату пального (л/100 км): "))
            if fuel_vytraty > 0:
                break
            else:
                print("Некоректне значення")
        except ValueError:
            print("Помилка: введіть число з комою або ціле")

    while True:
        try:
            fuel_price = float(input("Середня ціна одного літра пального (грн): "))
            if fuel_price > 0:
                break
            else:
                print("Некоректне значення")
        except ValueError:
            print("Помилка: введіть число з комою або ціле")

    while True:
        try:
            passengers = int(input("Кількість пасажирів: "))
            if passengers >= 0:
                break
            else:
                print("Некоректне значення")
        except ValueError:
            print("Помилка: введіть ціле число")

    total_fuel = (distance / 100) * fuel_vytraty
    total_cost = total_fuel * fuel_price

    if passengers > 0:
        cost_per_passenger = total_cost / passengers
    else:
        cost_per_passenger = total_cost

    print("\nРезультати розрахунку:")
    print("Загальна кількість пального:", round(total_fuel, 2), "л")
    print("Загальна вартість подорожі:", round(total_cost, 2), "грн")
    if passengers > 0:
        print("Вартість на одного пасажира:", round(cost_per_passenger, 2), "грн")
    else:
        print("Пасажирів не вказано (тільки водій). Вартість подорожі розрахована на одну особу.")

    repeat = input("Бажаєте розрахувати ще раз? (так/ні): ").strip().lower()
    if repeat != "так":
        print("Дякуємо за користування калькулятором!")
        break
