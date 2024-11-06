# declaring a string variable
str = input("enter the string")
print(str)
k='$'
str2=str[0]+str[1:].replace(str[0],k)
print("Modified string : ",str2)
