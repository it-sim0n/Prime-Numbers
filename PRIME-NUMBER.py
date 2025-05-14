import math
zzz=1
while zzz==1:
    print("(1)PRIME OR NOT\n(2)N OF PRIME NUMBER\n(3)PRIMES NUMBER")
    x = int(input('ENTER YOUR PORPUSE: '))
    if x == 1:
        number = int(input('number: '))
        a = True
        while a:
            if number <= 1: 
                print('Is not prime...')
                break
            if number <= 3: 
                print('Is prime...')  
                break
            if (number % 2 == 0) or (number % 3 == 0): 
                print('Is not prime...')
                break
            i = 5
            while i * i <= number: 
                if (number % i == 0) or (number % (i + 2) == 0): 
                    print('Is not prime...')
                    break
                i = i + 6
            a = False
            print('Is prime...')    
    elif x == 2:
        x = int(input('x: '))
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        def n_prime(n):
            c = 0
            num = 2
            while True:
                if is_prime(num):
                    c += 1
                    if c == n:
                        return num
                num += 1

        print(n_prime(x))

    else:

        p = int(input('P: '))
        l = []

        for i in range(2, p + 1):
            x = i - 1
            xx = math.factorial(x)
            if (xx + 1) % i != 0:
                l.append(i)

        print(l)
    AG = input('DONE?(Y/N)')
    if AG=='Y':
        zzz=0
    else:
        continue
