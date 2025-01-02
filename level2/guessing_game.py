import random


numbers = range(1, 101)
lucky_num = random.choice(numbers)
print(lucky_num)
inp = input('Enter your lucky number: ')
value = int(inp)

if value < lucky_num:
    print('Too low')
elif value > lucky_num:
    print('Too high')
else:
    print('Congratulations')     