from filereader import filerdl

"""def sum_cal(list):
    new_list = []
    new_item = 0
    for i in list:
        if i == "":
            new_list.append(new_item)
            new_item = 0
            continue
        new_item = new_item + int(i)
    
    new_list.sort(reverse=True)
    return new_list[0]"""

def sum_cal2(list):
    new_list = []
    new_item = 0
    for i in list:
        if i == "":
            new_list.append(new_item)
            new_item = 0
            continue
        new_item = new_item + int(i)
    
    new_list.sort(reverse=True)
    
    output = new_list[0] + new_list[1] + new_list[2]
    return output

print(sum_cal2(filerdl("input.txt")))
            