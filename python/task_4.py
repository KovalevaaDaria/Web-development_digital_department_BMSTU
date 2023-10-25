if __name__ == '__main__':
    string = input()
    substring = input()

    words = string.split()
    
    foundwords = []

    for word in words:
        if substring.lower() in word.lower():
            foundwords.append(word)

    if foundwords:
        for word in foundwords:
            print(word)