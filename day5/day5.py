from filereader import filerdl

lista = [["F", "H", "B", "V", "R", "Q", "D", "P"], 
         ["L", "D", "Z", "Q", "W", "V"], 
         ["H", "L", "Z", "Q", "G", "R", "P", "C"],
         ["R", "D", "H", "F", "J", "V", "B"],
         ["Z", "W", "L", "C"],
         ["J", "R", "P", "N", "T", "G", "V", "M"],
         ["J", "R", "L", "V", "M", "B", "S"],
         ["D", "P", "J"],
         ["D", "C", "N", "W", "V"]] 
"""
lista = [["Z", "N"],
         ["M", "C", "D"],
         ["P"]]"""

def get_num(text):
    amount = []
    start = []
    end = []
    
    for i in text:
        if len(i) == 18:
            amount.append(i[5])
            start.append(i[12])
            end.append(i[17])
        if len(i) == 19:
            amount.append(i[5] + i[6])
            start.append(i[13])
            end.append(i[18])
    return amount, start, end
    
def interpreter(amount, start, end, lista):
    for i in range(len(amount)):
        print(lista)
        for x in range(int(amount[i])):
            lista[int(end[i]) - 1].append(lista[int(start[i]) - 1].pop(-1))

    print(lista)
    return lista
    
def interpreter2(amount, start, end, lista):
    for i in range(len(amount)):
        lista[int(end[i]) - 1].extend(lista[int(start[i]) - 1][-int(amount[i]):])
        del lista[int(start[i]) - 1][-int(amount[i]):]
    return lista

def instructor(lista, text):
    output = ""

    storage = interpreter2(get_num(text)[0], get_num(text)[1], get_num(text)[2], lista)
    print(storage)
    for i in storage:
        output += i[-1]
        
    return output
    
        
        
    
print(instructor(lista, filerdl("input copy.txt")))