a= input("enter your name:")

b=input("enter the 1strahum product name:")
c=int(input("price:"))

x=input("enter the 2nd product name:")
y=int(input("price:"))

p=input("enter the 3rd product name:")
z=int(input("price:"))


print(f"Customer Name:{a}")

print(f"product 1:{b}")
print(f"price:{c}")

print(f"product 1:{x}")
print(f"price:{y}")

print(f"product 1:{p}")
print(f"price:{z}")

total=c+y+z
print(f"Subtotal:{total}")

if total>=5000:
    f=total*0.2
    g=total-f
    print(f"Discount:{f:.2f}")
    print(f"Final Total:{g:.2f}")
elif 3000<= total <=4999:
    h=total*0.1
    j=total-h
    print(f"Discount:{h:.2f}")
    print(f"Final Total:{j:.2f}")
elif 1000<= total <=2999:
    k=total*0.05
    l=total-k
    print(f"Discount:{k:.2f}")
    print(f"Final Total:{l:.2f}")
else:
    print(f"NO DISCOUNT")