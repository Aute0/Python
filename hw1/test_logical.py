

x = int(input(' x =  '))
y = int(input(' y =  '))
z = int(input(' z =  '))

left = not (x or y or z)
right = not x and not y and not z
result = left == right

if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
