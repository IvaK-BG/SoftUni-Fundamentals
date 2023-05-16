age = int(input())
person_type = ""
drink = ""
if age <= 14:
    drink = "drink toddy"
elif age <= 18:
    drink = "drink coke"
elif age <= 21:
    drink = "drink beer"
else:
    drink = "drink whisky"
print(drink)
