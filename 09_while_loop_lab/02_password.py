# 2 Password
name = input()
password = input()

while True:
    data = input()
    if data != password:
        continue
    elif data == password:
        print(f'Welcome {name}!')
        break
