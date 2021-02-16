import random
import time
min = 1
max = 6

while True:
    roll = str(input("Roll the dice? (Yes/No): "))
    i = 1
    while i > 0:
        if roll == "Yes":
            print("Rolling dice...")
            time.sleep(1.4)
            print("The values are:")
            print(random.randint(min, max))
            print(random.randint(min, max))
            roll_again = input("Roll again? (Yes/No): ")
            if roll_again == "Yes":
                continue
            elif roll_again == "No":
                print("Goodbye!")
                time.sleep(1)
                quit()
            else:
                print("Invalid answer. Stopping program.")
                quit()
    else:
        quit()
