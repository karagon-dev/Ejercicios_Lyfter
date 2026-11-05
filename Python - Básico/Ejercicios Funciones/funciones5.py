def case_count(my_string):
    letter = ""
    upperCount = 0
    lowerCount = 0
    for index in range(0, len(my_string), 1):
        letter = my_string[index]
        if letter == letter.upper() and letter.isalpha():
            upperCount += 1
        elif letter == letter.lower() and letter.isalpha():
            lowerCount += 1
    print(f"There's {upperCount} upper cases and {lowerCount} lower cases")

case_count(input("Enter a word: "))

#aprendí el built-in isalpha() para omitir caracteres especiales