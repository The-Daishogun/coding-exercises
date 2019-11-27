def count_vowels(text):
    text = text.lower()
    vowels = ["a", "e", "u", "o", "i"]
    number_of_vowels = []
    for vowel in vowels:
        counter = 0
        for char in text:
            if vowel == char:
                counter += 1
        number_of_vowels.append(counter)
    return number_of_vowels

n = input("type in the text\n")

a = count_vowels(n)

output = "Total Number of Vowels: {0}\nNumber of A:{1}\nNumber of E:{2}\nNumber of U:{3}\nNumber of O:{4}\nNumber of I:{5} ".format(sum(a), a[0], a[1], a[2], a[3], a[4])

print(output)