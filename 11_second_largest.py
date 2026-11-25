
def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return "No second largest number"

    return second


numbers = [10, 25, 5, 40, 15]

print("Second largest:", second_largest(numbers))
