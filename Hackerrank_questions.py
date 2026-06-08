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

n , m = input().split()
array = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happiness = 0

for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)



N = int(input())
require_set = set()
for i in range(N):
    name = input()
    if name not in require_set:
        require_set.add(name)


print(len(require_set))