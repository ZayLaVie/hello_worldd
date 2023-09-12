total = 0
for i in range(1,6):
    while True:
        try:
            user_input = int(input(f"Enter int #{i}:"))
            total +=user_input
            break
        except ValueError:
            print("Invalid input. Please enter an int")
    
print(f"Your sum is {total}")
