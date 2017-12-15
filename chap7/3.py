def is_prime(n):
    for i in range(2, n):
        if i % n:
            print("maybe be multiply")
            return False