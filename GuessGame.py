import random
chances=1
random_num= random.randint(1,9)

print("Number guessing game")
print("Guess a number (Between 1 and 9)")
number=int(input("Enter your guess:-"))

while chances < 5:
    chances+=1
    if random_num>number:
        print("your guess is too high:","Guess a number lower than",' ',number)

    if random_num<number:
        print("your guess is too low:","Guess a number higher than",' ',number)

    if random_num==number:
        print("Congratulations YOU WON !! ")

    if not chances <5:
        print("YOU LOOSE !!!","The number is"," ", random_num)