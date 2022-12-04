from filereader import filerdl

def comparer(lista):
    array = []
    for i in lista:
        array.append(i.split("-"))

    #Om första rangen är större
    if int(array[0][0]) == int(array[1][0]):
        return True
    
    if int(array[0][1]) == int(array[1][1]):
        return True

    if int(array[0][0]) <= int(array[1][0]):
        if int(array[0][1]) >= int(array[1][1]):
            return True
    
    if int(array[0][0]) >= int(array[1][0]):
        if int(array[0][1]) <= int(array[1][1]):
            return True

def comparer2(lista):
    array = []
    for i in lista:
        array.append(i.split("-"))

    if int(array[0][1]) >= int(array[1][0]):
        if int(array[0][0]) <= int(array[1][0]):
            return True

    if int(array[1][1]) >= int(array[0][0]):
        if int(array[1][0]) <= int(array[0][1]):
            return True 

def main(text):
    temp = []
    counter = 0
    for i in text:
        temp.append(i.split(','))

    for i in range(len(temp)):
       if comparer2(temp[i]):
            print(temp[i])
            counter += 1

    return counter



print(main(filerdl("input.txt")))
        