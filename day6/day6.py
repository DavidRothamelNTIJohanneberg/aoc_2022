from filereader import filerds

def unique_four(text):
    counter = 0
    #mjqjpqmgbljsphdztnvjfqwrcgsmlb
    for i in range(len(text)):
        print(text[i + 1: i + 4])
        if text[i] in text[i + 1: i + 4]:
            counter = 0
        else:
            counter += 1
        
        if counter == 3:
            return i + 2

def unique_14(text):
    counter = 0
    for i in range(len(text)):
        if text[i] in text[i + 1: i + 13]:
            counter = 0
        else:
            counter += 1
        
        if counter == 13:
            return i + 12

def unique_142(text):
    print(len(text))
    for i in range(len(text)):
        if text[i] not in text[i + 1: i + 14]:
            for x in range(len(text[i + 1: i + 14])):
                if text[i + x] in text[i + x + 1: i + 14]:
                    break
            else:
                return i + 14


print(unique_142(filerds("input.txt")))
print(filerds("input.txt")[1987 - 14: 1988])