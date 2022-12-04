from filereader import filerdl

def doubles(text):
    temp = set()
    length = int(len(text)/2)
    str1 = text[length:]
    str2 = text[:length]

    for i in str1:
        for x in str2:
            if x == i:
                temp.add(x)
        
    print(temp)
    return temp

def triples(text1, text2, text3):
    for i in text1:
        for j in text2:
            for k in text3:
                if (i == j) and (j == k):
                    return i

def counter(text):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    sum = 0
    for z in text:
        temp = doubles(z)
        
        for i in temp:
            sum += (letters.index(i) + 1)
    return sum


def counter2(text):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    sum = 0
    for i in range(0, len(text), 3):
        sum += (letters.index(triples(text[i], text[i + 1], text[i + 2])) + 1)
        
    return sum


print(counter2(filerdl("input.txt")))