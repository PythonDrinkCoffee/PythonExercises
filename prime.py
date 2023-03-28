# Obliczanie liczb pierwszych
def check_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False

    if prime:
        return f"{number} Is a prime number"
    else:
        return f"{number} Not a prime number"
    
for i in range(2,20):
    print(check_prime(i))