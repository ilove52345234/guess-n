import random
r = random.randint(1, 100)
x = 0
while True:
    i = input('請輸入一個數字: ')
    i = int(i)
    x += 1
    if i == r:
        print('終於猜對了!')
        print('猜了第', x, '次')
        break
    elif i < r:
        print('比答案小!')
    elif i > r:
        print('比答案大!')

    print('猜了第', x, '次')