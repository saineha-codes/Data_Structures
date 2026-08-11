numbers = [10, 20, 30, 40, 50]

reverse = []

for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])

print("Reversed array:", reverse)
