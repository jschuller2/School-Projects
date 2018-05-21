
'''
programmer name: Jared Schuller
Program name: hw03.py

'''


def compress( longList ):
    '''
    compresses list
    '''

    newList = []
    i = 0
    while i < len(longList):
        #print i
        curVal = longList[i]
        rep = 1
        while longList[i] == curVal and i < len(longList) - 1:
            #print longList[i], rep
            rep += 1
            i += 1
        if rep > 4:
            newList += ['D', curVal, rep - 1]
        else:
            newList += [curVal]
            i -= rep - 2

    return newList

def decompress( shortList ):
    '''
    decompresses list
    '''

    newList = []
    i = 0
    while i <len(shortList):
        if shortList[i] == 'D':
            j = 0
            while j < shortList[i + 2]:
                newList += [shortList[i + 1]]
                j += 1
            i += 3
        else:
            newList += [shortList[i]]
            i += 1

    return newList

'''
longList = [ 3, 2, 2, 2, 2, 2, 2, 5, 6, 4, 4, 7, 3, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8,\
             8, 7, 9, 1, 1, 1, 1, 4, 2, 2, 2, 0, 0, 2 ]
shortList = []
    
shortList = compress(longList)
deList = decompress(shortList)

print shortList
print deList
'''            
