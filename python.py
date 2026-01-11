num = int(input("Enter a number"))
print("/n")

## if no.is grater than one
if num>1:
    for i in range(2,int(num)+1):
        if (num%i) == 0:
            print(num,"is not a prime number")
            break

    else:
        print(num,"is a prime number")