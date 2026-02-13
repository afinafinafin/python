def multiplication_table(num):
    print(f"\nMultiplication Table of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

number = int(input("\nEnter a number for multiplication table: "))
multiplication_table(number)