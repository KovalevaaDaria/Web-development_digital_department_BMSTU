def input_string():
    str = input()
    input_str = " ".join(str.split())
    input_str = " ".join(str.split()) + " "
    input_str = input_str.replace(' ', '*')
    return input_str


if __name__ == '__main__':
    str_1 = input_string()
    print(str_1)