def cwff():
    filename = input("Enter file: ")
    numwords = 0
    file = open(filename,'r')
    for i in file:
        words = i.split(' ')
        numwords = len(words) + numwords
        print("Number of words: "+str(numwords))

cwff()