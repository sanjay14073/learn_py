## example for a simple decorator

def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@mydecorator
def my_function(x, y):
    print("Inside the function")
    return x + y

result = my_function(5, 10)
print("Result:", result)