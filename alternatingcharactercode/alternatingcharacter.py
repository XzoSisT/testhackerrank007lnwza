def alternatingCharacters(s):
    chareacter = ''
    result = 0
    for i in s:
        if i != chareacter:
            charecater = str(i)
        elif i == chareacter:
            result += 1
    return result