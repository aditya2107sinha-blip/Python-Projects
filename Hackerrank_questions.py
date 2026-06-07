T = int(input())
for i in range(T):
    a , b = input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError,ValueError) as e:
        print("Error Code:",e)


import re
t = int(input())
for _ in range(t):
    reg = raw_input()
    try:
        re.compile(reg)
        print(True)
    except re.error:
        print(False)
