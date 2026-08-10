numbers = [1, 2, 3, 4]
result = []

for i in range(len(numbers)):
    product = 1

    for num in numbers:
        if num != numbers[i]:
            product = product * num

    result.append(product)

print(result)