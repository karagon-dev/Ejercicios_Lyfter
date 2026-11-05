def revert_string(my_string):
    reverted_word = ""
    for index in range(len(my_string) - 1, -1, -1):
        reverted_word += my_string[index]
    return reverted_word

print(revert_string(input("Ingrese una palabra:")))