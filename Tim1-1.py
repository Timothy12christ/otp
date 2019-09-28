A=(str(input(print("Which service do you want? Y/N"))))
if A==('otp'):
    print('Ok!Now let me show you the OTP')
    import random
    a=random.randint(100000,999999) 
    a=int(a)
    S=(int(input(print(a))))
    if a==S:
        print('Good job')
    else:
        print('Sorry')