from itertools import count

max = 1000

def multiple(i):
    if (i%3==0 or i%5==0):
        return True
    else:
        return False

num = 0
for i in count():
    if i >= max:
        break;
    if multiple(i):
        num += i

print(num)