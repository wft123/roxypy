def check_word(str):
    if str[-1] == 1:
        return False

    pre_char = 0
    for i in range(len(str)):
        tmp = str[i]
        if tmp != 1 and tmp != 2:
            return False

        if pre_char == 1:
            if tmp != 2:
                return False

        pre_char = tmp
    return True


user_input = input()
print(check_word(user_input))
