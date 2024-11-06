x=int(input("enter number 1:"))
y=int(input("enter number 2:"))
z=int(input("enter number 3:"))
if (x >= y) and (x >= z):
    largest = x
elif (y >= x) and (y >= z):
    largest = y
else:
    largest = z
print(" The largest number is:",largest)
