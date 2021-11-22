def swapFileData():
    file1= input("Filename 1: ")
    file2 = input("Filename 2: ")

    readDataA = open(file1, 'r')
    data_a = readDataA.read()

    readDataB = open(file2, 'r')
    data_b = readDataB.read()

    writeFile1 = open(file1, 'w')
    writeFile1.write(data_b)

    writeFile2 = open(file2, 'w')
    writeFile2.write(data_a)

swapFileData()

