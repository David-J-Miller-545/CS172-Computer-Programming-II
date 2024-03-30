# Author: David Miller | djm545
# Date: 5/31/23
# Purpose: Creating a Hash Table of Birthdays

from birthday import Birthday

if __name__ == "__main__":
    while True:
        try:
            filename = input("Enter name of the data file: ")
            f = open(filename)
            break
        except:
            print ("Error: that file does not exist. Try again.")
    
    hashTable = [[], [], [], [], [], [], [], [], [], [], [], []] # 2D List
    
    lineNum = 0
    for line in f.readlines():
        lineNum += 1
        readBD = line.split("/")
        bd = Birthday(int(readBD[0]), int(readBD[1]), int(readBD[2]))
        bdTuple = (bd, lineNum)
        hashTable[hash(bdTuple[0])].append(bdTuple)
    
    print("")
    rowNum = 0
    for row in hashTable:
        print(f"Hash location {rowNum} has {len(row)} elements in it")
        rowNum += 1
        
