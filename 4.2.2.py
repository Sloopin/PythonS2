def is_prime(number):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if (number % i) == 0:
                # If number % i is 0 then number is not prime
                return False
        # A "else" used under "for" means that after the for loop is done, the else part under it will be executed
        # which in this case means number isn't prime
        else:
            return True
    else:
        return False