def counter():
    dna = open("rosalind_dna.txt", "r")
    sequence = dna.read()
    countA = 0
    countT = 0
    countC = 0
    countG = 0
    for base in sequence:
        if (base == "A"):
            countA += 1
        elif (base == "T"):
            countT += 1
        elif (base == "C"):
            countC += 1
        elif (base == "G"):
            countG += 1
    print(countA, countC, countG, countT)

counter()
