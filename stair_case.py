n = int(input("Enter number of stairs: "))

val1 = 1
val2 = 2
result = 0

if n <= 2:
    print(n)
else:
    for i in range(3, n + 1):
        result = val1 + val2
        val1 = val2
        val2 = result

    print(result)