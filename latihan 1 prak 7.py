def is_prima ():
    x=int(input("Masukan angkanya: "))
    for i in range(2, x):
        if x % i == 0:
            return ("bukan bilangan prima")
    return ("bilangan prima")
        
p=is_prima()
print(p)