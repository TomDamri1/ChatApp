import random
from math import sqrt


# checks if n is prime
from encryption.DH.prime_dict import primes


def isPrime(n):
    # test if n is even
    if n % 2 == 0:
        return False
    # test each odd number from 3 to sqrt(n)
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False
    # n is necessarily prime
    return True



#
def Hellman_keys_generate(p):
    if not isPrime(p):
        raise ValueError('Both numbers should be prime.')


#choose integer in range 2 to p-2
    alpha=random.randrange(2, p-1)


#choose random private key in range 1 to p-1
    a=random.randrange(1,p)
#compute A (kpub A)
    A=((alpha)**a)%p
    #need to be sent to bob


#choose random private key in range 1 to p-1
    b=random.randrange(1,p)
#compute B (kpub B)
    B=((alpha)**b)%p
    #need to be sent to bob


#compute shared key
    alice_side_KAB = (B**a)%p
    bob_side_KAB   = (A**b)%p

    return (alice_side_KAB,bob_side_KAB)

def real_hellman():
    #alex need to generate alpah and p!
    alpha = get_alpha_from_server()
    p = get_p_from_server()


    a = random.randrange(1,p)
    A = (alpha**a)%p

    #alex need to allocate room for A and B
    send_A_to_server()
    B = get_B_from_server()


    #get the key
    comKey = (B**a)%p
    
    return comKey

if __name__ == '__main__':
    
    i = primes[random.randrange(0,len(primes))]
        
    if isPrime(i):
        print(i)
        print(Hellman_keys_generate(i))
