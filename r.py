import random
mn = input('請決定最小數字')
mn = int(mn)
mx = input('請決定最大數字')
mx = int(mx)
r = random.randint(mn, mx)
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
    if i < mn or i > mx:
        print('請輸入', mn, '到', mx, '的數字')
    print('猜了第', x, '次')