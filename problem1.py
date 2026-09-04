a = input("enter your name:")
math= int(input("enter your MATH subject number:"))
ict = int(input("enter your ICT subject number:"))
bangla = int(input("enter your BANGLA subject number:"))
print()
print(f"Student name:{a}")
print()
total_mark=math+ict+bangla
print(f"Total mark:{total_mark}")
print()

avg=total_mark/3
print(f"Average:{avg:.2f}")
print()

if 80<= avg <=100:
    print("Grade:A+")
elif  70<= avg <=79:
    print("Grade:A")  
elif 60<= avg <=69:
    print("Grade:B")
elif 50<= avg <=59:
    print("Grade:C")
else:
    print("Grade:F") 