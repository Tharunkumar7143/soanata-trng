n=int(input("enter a number:"))
reverse_number=n
r=0
while n!=0:
    temp=n%10
    r=r*10+temp
    n=n//10
if(reverse_number==r):
    print("palindrome",r)
else:
    print("not palindrome",r)


