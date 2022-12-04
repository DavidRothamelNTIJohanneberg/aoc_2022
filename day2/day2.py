from filereader import filerdl

"""
def who_wins1(let1, let2):
    output = [0, 0]
    if let1 == "A" and let2 == "X":
        output[0] = 4 
        output[1] = 4
    elif let1 == "A" and let2 == "Y":
        output[0] = 1 
        output[1] = 8
    elif let1 == "A" and let2 == "Z":
        output[0] = 7 
        output[1] = 3
    elif let1 == "B" and let2 == "X":
        output[0] = 8 
        output[1] = 1
    elif let1 == "B" and let2 == "Y":
        output[0] = 5 
        output[1] = 5
    elif let1 == "B" and let2 == "Z":
        output[0] = 2 
        output[1] = 9
    elif let1 == "C" and let2 == "X":
        output[0] = 3 
        output[1] = 7                    
    elif let1 == "C" and let2 == "Y":
        output[0] = 9 
        output[1] = 2
    elif let1 == "C" and let2 == "Z":
        output[0] = 6 
        output[1] = 6
             
    return output
"""
#A = Rock = X 1
#B = Paper = Y 2
#C = Scissor = Z 3

def who_wins2(let1, let2):
    output = [0, 0]
    if let1 == "A" and let2 == "X":
        output[1] = 3
    elif let1 == "A" and let2 == "Y":
        output[1] = 4
    elif let1 == "A" and let2 == "Z":
        output[1] = 8
    elif let1 == "B" and let2 == "X":
        output[1] = 1
    elif let1 == "B" and let2 == "Y":
        output[1] = 5
    elif let1 == "B" and let2 == "Z":
        output[1] = 9
    elif let1 == "C" and let2 == "X":
        output[1] = 2                    
    elif let1 == "C" and let2 == "Y":
        output[1] = 6
    elif let1 == "C" and let2 == "Z":
        output[1] = 7
             
    return output

def points(input):
    player1 = 0
    player2 = 0
    for i in input:
        x,y = i.split(" ")
        player1 += who_wins2(x, y)[0]
        player2 += who_wins2(x, y)[1]
    return player2

print(points(filerdl("input.txt")))
    
