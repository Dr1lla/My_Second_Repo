product_name = input("Введіть назву товару: ")
quantity = int(input("Введіть кількість: "))
price = float(input("Введіть ціну за одиницю: "))
daysCount = int(input("Введіть кількість днів продажів: "))

total_cost = (quantity * price) * daysCount

print(f"Продукт: {product_name}, Кількість: {quantity}, Днів продажів: {daysCount}, Вартість: {total_cost}")