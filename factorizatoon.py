print("find the factors of a number")
num = int(input("enter the number"))
print(f"\n finding factors of {num}...\n")
factor = []
for i in range(1,num + 1):
    if num % i == 0:
        factor.append(i)
        print(f"{i}is a factor")

