fizzbuzz = 1
fizzbuzz += int(input("Enter number: "))
for i in range(1,fizzbuzz):
    print("fizz" * (i%3==0) + "buzz" * (i%5==0) or i)
