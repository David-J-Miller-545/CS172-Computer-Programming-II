#	zmq23, djm545
#	David Miller, Zacharia Qaisar
#
#

from spellchecker import spellchecker


def get_file():
    print("Welcome to Text File Spellchecker.")
    validFile = False
    while not validFile:
        validFile = True
        try:
            file = open(input("Enter the name of the file to read:"), "r")
        except:
            print("Could not open file.")
            validFile = False

    return file
    
if __name__ == "__main__":
    SC = spellchecker("english_words.txt")
    f = get_file()
    correct = True
    lineNum = 0
    cWords = 0
    icWords = 0
    for line in f.readlines():
        words = line.split()
        for word in words:
            correct = SC.check(word)
            if not correct:
                print(f"Possible Spelling Error on line {(lineNum + 1)}: {word}")
                icWords += 1
            else:
                cWords += 1
        lineNum += 1
    print(f"{cWords} passed the spell checker.\n{icWords} failed the spell checker.\n{((100*cWords)/(cWords+icWords)):.2f}% of the words passed.")
                
        
