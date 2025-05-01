##Example for try/except/finally
try:
    x=1/0
except ZeroDivisionError as e:
    print("Error: ",e)
finally:
    print("This will always execute")
