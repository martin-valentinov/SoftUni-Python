username = input()
password = input()
check = input()

while check != password:
    check = input()

print(f'Welcome {username}!')