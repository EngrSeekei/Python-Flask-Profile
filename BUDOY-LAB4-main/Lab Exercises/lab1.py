def print_diamond(n):

    if n % 2 == 0:
        return "Please provide an odd integer."

   
    for i in range(1, n // 2 + 2):
        spaces = " " * ((n // 2 + 1) - i)
        asterisks = "*" * (2 * i - 1)
        print(spaces + asterisks)

   
    for i in range(n // 2, 0, -1):
        spaces = " " * ((n // 2 + 1) - i)
        asterisks = "*" * (2 * i - 1)
        print(spaces + asterisks)



n = 5
result = print_diamond(n)
if result == "Please provide an odd integer.":
    print(result)