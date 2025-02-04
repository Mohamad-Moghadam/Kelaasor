"""def weird_sequence(num):
    sequence = [sum(range(i + 1)) for i in range(num)]
    print(sequence)
    return 1 if (num * (num - 1)) // 2 in sequence.index() else 0


n = int(input())
n -= 1
print(weird_sequence(n))
"""


def weird_sequence(n):
    if n < 0:  # بررسی مقدار نامعتبر
        return 0

    # حل معادله معکوس عدد مثلثی: n = i * (i - 1) / 2 → حل برای i
    i = int(((1 + (1 + 8 * (n - 1)) ** 0.5) / 2))  # حل معادله درجه 2

    # بررسی اینکه (i * (i - 1)) / 2 برابر با n-1 هست یا نه
    return 1 if (i * (i - 1)) // 2 == (n - 1) else 0


# دریافت مقدار از کاربر
desired_number = int(input())
print(weird_sequence(desired_number))
