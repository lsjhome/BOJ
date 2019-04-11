def is_prime(num):

    if num !=1:
        
        for i in range(2, int(num**0.5)+1):           
            if num % i == 0:
                return False
    else:
        return False
    
    return True

def prime_check_list(n, num_list):
    
    num_list = num_list[:n]
    
    return sum([is_prime(i) for i in num_list])

if __name__ == '__main__':

    n = int(input())
    num_list = list(map(int, input().split(' ')))

    print (prime_check_list(n, num_list))
