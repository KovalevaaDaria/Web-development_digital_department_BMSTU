def inputstring():
    str = input()
    str = str.lower()
    words = str.split(", ")
    words = list(set(words))
    sortedwords = sorted(words)
    return ', '.join(sortedwords)


if __name__ == '__main__':
    str1 = inputstring()
    print(str1)