number_of_orders = int(input())
total = 0
for number in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    price_order = price_per_capsule * days * capsules_needed_per_day
    total += price_order
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        print(f"The price for the coffee is: ${price_order:.2f}")
print(f"Total: ${total:.2f}")

