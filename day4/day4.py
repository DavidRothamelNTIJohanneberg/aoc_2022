from filereader import filerdl

def comparer(pair1, pair2):
    #Gör om helt och hållet
    print(pair1)
    print(pair2)
    if pair1 == pair2:
        return False
    if int(str1) <= int(str2):
        if int(str1) <= int(str2):
            return True
    elif int(pair1[1]) <= int(pair2[1]):
        return True
        
def num_range(lista):
    output = ""
    for i in range(int(lista[0]), int(lista[1]) + 1):
        output += f"{i}"
    return output

def contains(text):
    counter = 0
    lista = []
    temp = []
    for i in text:
       temp.append(i.split(","))
       
    for x in temp:
        for y in x:
            lista.append(y.split("-"))
    
    print(lista)
    
    for i in range(0, len(lista), 2):
        if comparer(num_range(lista[i]), num_range(lista[i + 1])):
            counter += 1
        
    return counter

print(contains(filerdl("input.txt")))