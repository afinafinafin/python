def print_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

n = int(input("Enter number of rows: "))
print_pattern(n)