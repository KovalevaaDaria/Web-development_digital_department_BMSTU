if __name__ == '__main__':
    sum = 0
    while True:
        value = input()
        if str(value) == "":
            break
        if int(value) % 2 == 0:
            sum += int(value)
    print(sum)