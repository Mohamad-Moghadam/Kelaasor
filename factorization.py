def prime_divisors(given_number):
    result = []
    while given_number > 1:
        for number in range(2, given_number + 1):
            if given_number % number == 0:
                result.append(number)
                given_number //= number
                break
    return result


desired_number = int(input())
print(*prime_divisors(desired_number), sep="\n")
