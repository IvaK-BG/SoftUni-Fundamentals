number_of_message = int(input())
for current_message in range(number_of_message):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88 and number != [88,86]:
        print("GREAT!")
    else:
        print("Bye.")