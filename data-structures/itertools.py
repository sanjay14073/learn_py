from itertools import permutations, combinations,product

## Lets consider the list [1,2,3]

mylist=[1,2,4]

## All size combiantions
for i in range(1,len(mylist)+1):
    for i in combinations(mylist,i):
        print(i)

print('------------------')
## Permutations
for i in permutations(mylist):
    print(i)

print('------------------')

## Product
## Repeat the list
for i in product(mylist,repeat=2):
    print(i)