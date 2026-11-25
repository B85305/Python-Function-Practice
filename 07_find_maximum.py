
def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [10, 25, 5, 40, 15]

print("Maximum number:", find_max(numbers))
