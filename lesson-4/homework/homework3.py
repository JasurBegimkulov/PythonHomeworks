txt = "abcabcdabcdeabcdefabcdefg"
result = ""

for i in range(len(txt)):
    result += txt[i]

    if (i + 1) % 3 == 0 and i < len(txt) - 1:
        result += "_"

    if txt[i] in "aeiou" and i < len(txt) - 1:
        result += "_"

print(result)