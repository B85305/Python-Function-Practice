
def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


num = int(input("Enter a number: "))
print("Sum:", sum_n(num))
