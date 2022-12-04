from filereader import filerdl

def comparer(pair1, pair2):
    if pair1 in pair2:
        return True
    if pair2 in pair1:
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
    #Delar upp varje rad till två ranges
    for i in text:
       temp.append(i.split(","))
    #Delar upp varje objekt i listan till två strings
    for x in temp:
        for y in x:
            lista.append(y.split("-"))
    
    print(len(lista))
    #Kollar om det går att hitta hela den ena rangen i den andra
    for i in range(0, len(lista), 2):
        print(i)
        if comparer(num_range(lista[i]), num_range(lista[i + 1])):
            counter += 1
        
    return counter

print(contains(filerdl("input.txt")))