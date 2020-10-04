min_sleep = int(input())
max_sleep = int(input())
current_sleep = int(input())

if current_sleep >= min_sleep:
    if current_sleep <= max_sleep:
        print('Normal')
    else:
        print('Excess')
else:
    print('Deficiency')
