#Isomorphic String
def Isomorphic(self, s1, s2):

    if len(s1) != len(s2):
        return False
    
    mapST = {}
    mapTS = {}

    for char1, char2 in zip(s1, s2):
        if char1 in mapST:
            if mapST[char1] != char2:
                return False
            
        if char2 in mapTS:
            if mapTS[char2] != char1:
                return False

        mapST[char1] = char2
        mapTS[char2] = char1

    return True

#Number of steps to Reduce a Number
def numSteps(self, s):
    steps = 0
    carry = 0

    for i in range(len(s)-1, 0, -1):
        
        if int(s[i]) + carry == 1:
            steps += 2
            carry = 1
        else:
            carry += 1

    return steps + carry            

         