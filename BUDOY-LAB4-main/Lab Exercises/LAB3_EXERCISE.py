def vowelsToUpper(input_str):
    vowels = 'aeiouAEIOU'
    result = ''

    for char in input_str:
        if char in vowels:
            result += char.upper()
        else:
            result += char

    return result

output = vowelsToUpper("Hello, World!")
print(output)
