a=[1,2,3]

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

## Some common operations on list

a.append(4)
a.pop(0)

a.sort()
a.reverse()

a.remove(2)
a.insert(0, 5)
a.extend([6, 7, 8])
a.clear()
a.count(1)