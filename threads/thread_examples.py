### Example of using threading in Python
import threading

def square(n):
    print(n*n)

def quad(n):
    print(n**4)

def power(n):
    print(n**n)

def cube(n):
    print(n*n*n)

t1=threading.Thread(target=square,args=(2,))
t2=threading.Thread(target=quad,args=(2,))
t3=threading.Thread(target=power,args=(2,))
t4=threading.Thread(target=cube,args=(2,))

for i in [t1,t2,t3,t4]:
    i.start()
    i.join()

print("Without joint")
for i in [t1,t2,t3,t4]:
    i.start()
