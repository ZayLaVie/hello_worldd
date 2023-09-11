user_input = input("Enter a string: ")
lower_case= ""
upper_case= ""

for char in user_input:
    if char.islower():
        lower_case +=char
    elif char.isupper():
        upper_case +=char

result = lower_case+upper_case
print(result)
