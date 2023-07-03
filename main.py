encrypt = input("Do you want to encrypt or decrypt?\n")
encrypt = str(encrypt)
key = input("What is the key?\n")
keyLength = len(key)
k = 0
newwordList = []

def toWord(stringArray):
    return ' '.join(stringArray)

Input = input("What do you want to convert?\n")
Input = str(Input)
Input = Input.lower()
Length = len(Input)
wordList = Input.split()

if (encrypt == "encrypt"):
    for String in wordList:
        newWord = ""
        for i in range(0,len(String)):
            if String[i].isalpha():
                valChar = ord(String[i])
                valKey = ord(key[k%keyLength])
                keyChar = ''
                if (valKey >= valChar):
                    keyChar = chr(valChar - valKey + 122)
                else:
                    keyChar = chr(valChar - valKey + 96)
                newWord += str(keyChar)
                k += 1
            else:
                newWord += String[i]
        newwordList.append(newWord)
    print(toWord(newwordList))
else:
    i = 0
    k = 0
    newnewwordlist = []
    def isinRange(num):
        if ((num > 96) and (num < 123)):
            return True
        else:
            return False
    for j in range(0,len(wordList)):
        newWord = ""
        String = wordList[j]
        for i in range(0, len(String)):
            if String[i].isalpha():
                valChar = ord(String[i])
                valKey = ord(key[k%keyLength])
                keyChar = ''
                constraint = -1*valKey + 96
                if (isinRange(valChar + valKey - 122)):
                    keyChar = chr(valChar + valKey - 122)
                else:
                    keyChar = chr(valChar + valKey - 96)
                newWord += str(keyChar)
                k += 1
            else:
                newWord += String[i]
        newnewwordlist.append(newWord)
    print(toWord(newnewwordlist))
