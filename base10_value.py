def func(input_string):
    base10_value = []
    for char in input_string:
        if 'a' <= char <= 'z':
            base10_value.append(ord(char) - ord('a') + 10)
    return base10_value

string1 = "hello"
string2 = "world"

base10_value1 = func(string1)
base10_value2 = func(string2)

print(base10_value1)
print(base10_value2)