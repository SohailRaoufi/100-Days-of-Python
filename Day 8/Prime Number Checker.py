
def prime_checker(number):
    for i in range(2 , number//2 + 1):
        if number % i == 0:
            print("Number is Not Prime")
            break
    else:
        print("It's a prime Number")
            

n = int(input("Check this number: "))
prime_checker(number=n)