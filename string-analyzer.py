print("STRING ANALYZER")
sentence = input("Enter a String: \n")

count = 0
print("RESULTS")
print("Original String   :",sentence)
for char in sentence:
    count += 1
print("Characters        :",count)

word = 0
for char in sentence:
    if char == " ":
        word += 1
print("Words             :",word)

vowel = 0
for char in sentence:
    if char in "AEIOUaeiou":
        vowel += 1
print("Vowels            :",vowel)

consonant = 0
for char in sentence:
    if char in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        consonant += 1
print("Consonants        :",consonant)

digit = 0
for dig in sentence:
    if dig in "1234567890":
        digit += 1
print("Digits            :",digit)

space = 0
for spaces in sentence:
    if spaces in " ":
        space += 1
print("Spaces            :",space)

special_char = 0
for special in sentence:
    if special in "!@#$%^&*()?/\|*-+_=":
        special_char += 1
print("Special Chars     :",special_char)

print("\nUppercase         :",sentence.upper())
print("Lowercase         :",sentence.lower())
print("Reversed          :",sentence[::-1])

if sentence == sentence[::-1]:
    print("Palindrome        : Yes")
else:
    print("Palindrome        : No")

print("\nCharacter Frequency")
frequency = {}
for char in sentence:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
for key in frequency:
    print(key, ":", frequency[key])