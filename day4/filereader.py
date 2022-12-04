#Lägger hela texten på samma ställe
def filerds(filnamn):
    read_data = []
    with open(filnamn) as f:
        read_data = f.read()
    return read_data

#Delar upp texten efter rad
def filerdl(filnamn):
    read_data = []
    with open(filnamn) as f:
        for line in f:
            read_data.append(line.replace("\n", ""))
    return read_data

#Delar upp efter ord
def filerdsp(filnamn):
    list = []
    read_data = []
    with open(filnamn) as f:
        for i in f:
            list.append(i.replace("\n", "").split(" "))
        for i in list[1:]:
            read_data = list[0] + i
    return read_data

if __name__ == "__main__":
    import sys
    print(filerds(sys.argv[1]))
    print(filerdl(sys.argv[1]))
    print(filerdsp(sys.argv[1]))
    