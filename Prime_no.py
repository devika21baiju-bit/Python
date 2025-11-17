x=int(input('Enter from which number would u like to check for prime numbers: '))
y=int(input('Enter till which numbers would u like to check for prime numbers: '))
for i in range(x,y+1,1):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i,'is a prime number.')
            break
        
