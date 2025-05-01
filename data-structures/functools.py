from functools import reduce,lru_cache,partial

@lru_cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print("LRU Cache example")
print(fib(10))

mylist=[1,2,3,4,5]
print("Reduce example")
print(reduce(lambda x,y:x+y,mylist))

print("Partial example")
add=partial(lambda x,y:x+y,10)
print(add(5)) # 10+5=15