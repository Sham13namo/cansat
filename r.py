x = 0 
z = 0
start = input()
print(start)
while True:
    name = input()
    if  x == 11 or z == 11:
        break
    if name == "Антон":
        x += 1
    elif name == "Алиса":
        z+=1
    print(x, z)
if start == "Антон":
    print(start)
    print(x," ",z)   
elif start == "Алиса":
    print(start)
    print(z," ",x)   