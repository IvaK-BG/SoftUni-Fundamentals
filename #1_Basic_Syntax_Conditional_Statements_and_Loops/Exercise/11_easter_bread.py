budget = float(input())
flour_kg_price = float(input())
price_pack_eggs = 0.75 * flour_kg_price
one_l_milk_price = flour_kg_price * 1.25
_250_ml_milk_price = 0.250 * one_l_milk_price
price_per_bread = price_pack_eggs + _250_ml_milk_price + flour_kg_price
number_of_breads = 0
colored_eggs = 0

while budget > price_per_bread:
    budget -= price_per_bread
    number_of_breads += 1
    colored_eggs += 3
    if number_of_breads % 3 == 0:
        colored_eggs -= (number_of_breads - 2)
    if budget < price_per_bread:
        break
money_left = budget
print(f"You made {number_of_breads} loaves of Easter bread! Now you have {colored_eggs} \
eggs and {money_left:.2f}BGN left.")
