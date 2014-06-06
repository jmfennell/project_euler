from itertools import count
from functools import lru_cache

max = 4000000
@lru_cache(maxsize=None)
def fib(i):
    if (i <= 2):
        return i
    return fib(i-1)+fib(i-2)

num = 0
for i in count():
    if (fib(i) > max):
        break
    if fib(i)%2==0:
        num += fib(i)

print(num)