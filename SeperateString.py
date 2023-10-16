s = "hello 123 $!"
number_index = "0123456789"
vowel_index = "aeiouy"
numbers = ""
vowels = ""
everything = ""

for string in s:
    print(string)
    if string in number_index:
        numbers += string
    elif string in vowel_index:
        vowels += string
    else:
        everything += string

print("Numbers:", numbers)
print("Vowels:", vowels)
print("Everything else:", everything)
