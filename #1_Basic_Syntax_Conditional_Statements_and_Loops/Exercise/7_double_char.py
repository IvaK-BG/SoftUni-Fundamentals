command = input()
while command != "End":
    current_string = command
    double_char = ""
    if current_string != "SoftUni":
        for _ in range(len(current_string)):
            double_char += current_string[_] * 2
        print(double_char)
    command = input()

