
with open("text.txt","w") as file:
    file.write("Working")

with open("text.txt","r") as file:
    content = file.read()
    print(content)