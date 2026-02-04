price = 100

def increment():
    price = 200
    price += 10

    return price

print(price)

price_2 = increment()
print(price_2)


x = "global"

def externa():
    x = "enclosing"
    def interna():
        x = "local"
        print(x)
    
    interna()

externa()