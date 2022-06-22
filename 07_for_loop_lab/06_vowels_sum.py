# 6 Vowels Sum
inp_text = input()
total = 0

for i in range(0, len(inp_text)):
    if inp_text[i] == "a":
        total += 1
    if inp_text[i] == "e":
        total += 2
    if inp_text[i] == "i":
        total += 3
    if inp_text[i] == "o":
        total += 4
    if inp_text[i] == "u":
        total += 5
print(total)
