def input_number():
    list = []
    for numbers in range(1, 6):
        numbers = input()
        if str(numbers) == "":
            break
        if int(numbers) > 0:
            list.append(int(numbers))
    return list


if __name__ == '__main__':
    new_list = input_number()
    numbers = list(map(int, new_list))
    numbers.sort(reverse=True)
    for number in numbers:
        print(number)