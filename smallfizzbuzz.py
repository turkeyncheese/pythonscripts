fizzbuzz=lambda f,b,s:[i%f//2*"Fizz"+i%b//4*"Buzz"or-~i for i in range(s)]
#I believe this may or may not be the smallest solution but I may be wrong, I haven't checked because I was just messing around.
#Cool thing about this solution is that you can change the variables for what number you divide by for 'Fizz' and 'Buzz'.
#For example instead of 3 and 5 you can do 12 and 15.

fizzBuzz=lambda n:'Fizz'*(n%3<1)+'Buzz'*(n%5<1)or"%d"%n
#Nevermind this is the shortest one. And damn that's awesome.
