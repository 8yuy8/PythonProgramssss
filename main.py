allCharsList = ["0", "1", "2" ,"3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "a",
                "ą", "b", "c", "ć", "d", "e", "ę", "Ą", "Ć", "Ę",
                "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r", "s", "ś",
                "t", "u", "v", "w", "x", "y", "z", "ź", "ż", "G", "H", "I", "J", "K", "K", "Ł", "M",
                "N", "Ń", "O", "Ó", "P", "R", "S", "Ś", "T", "U", "V", "W", "X", "Y", "Z", "Ź", "Ż",
                "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "[",
                "]", "{", "}", "|", "/", "?", "<", ">", ",", ".", ";", ":", "'",]

print("Type a number to convert: ")
textToCipher = input()
print("Type a system it's wrote in: ")
oldSystem = input()
print("Type a system you want to convert at: ")
newSystem = input()

if int(oldSystem) > 106 or int(oldSystem) < 2 or int(newSystem) < 2 or int(newSystem) > 106:
    print("Podaj poprawny system liczbowy od 0 do 106 :)")
    exit
if textToCipher[0] == 0:
    print("Liczba nie może zaczynać się od 0 :)")
    exit

sysInfoList = ["binarnym", "trialnym", "kwartalnym", "pentalnym", "hexalnym", "heptalnym", "oktalnym", "nanonalnym",
               "decynalnym", "wigintalnym"  "trigintalnym", "tetragintalnym", "pentagintalnym", "hexagintalnym", "septagintalnym", "oktagintalnym", "nanogintalnym", "centagintalnym",
               "un", "duo", "tri", "tetra", "penta", "hexa", "septa", "okta", "nano"]

sysInfo = ""

nn = newSystem[0]
n = int(nn)

if int(newSystem) < 10:
    sysInfo = sysInfoList[int(newSystem)-2]
if int(newSystem) >= 10 and int(newSystem) < 100:
    mm = newSystem[1]
    m = int(mm)
    if m != 0:
        sysInfo =sysInfoList[m+16]
    sysInfo += sysInfoList[n+7]
if int(newSystem) >= 100:
    mm = newSystem[2]
    m = int(mm)
    if m != 0:
        sysInfo =sysInfoList[m+16]
    sysInfo+="centaginatlnym"

textToCipherList = []
i = 0
while i < len(textToCipher):
    j = 0
    while j < len(allCharsList):
        if textToCipher[i] == allCharsList[j]:
            textToCipherList.append(j)
        j += 1
    i += 1

while textToCipherList[0] == 0:
    textToCipherList.remove(0)

convertedNumber = []

i = 0
j = len(textToCipherList)
decimalValue = 0

while i < j:
    decimalValue += int(oldSystem) ** (j - i -1) * int(textToCipherList[i])
    i += 1

i = 300
j = 0
a = int(newSystem)
b = int(decimalValue)

while (a-1) * a ** i > b and i >= 0:
    i -= 1
i += 1
while i >= 0:
    while j < a:
        if j * a ** i == b:
            convertedNumber.append(j)
            b = 0
            while i > 0:
                print(i)
                convertedNumber.append(0)
                i -= 1
            i = 0
        if j * a ** i < b and (j+1) * a ** i > b:
            convertedNumber.append(j)
            b -= j*a**i
        j += 1
    i -= 1
    j = 0

while convertedNumber[0] == 0:
    convertedNumber.remove(0)

newConvrtedNumber = []

number = ""
i = 0
j = 0
while i < len(convertedNumber):
    j = 0
    while j < len(allCharsList):
        if convertedNumber[i] == j:
            number += (allCharsList[j])
        j += 1
    i += 1


print("Liczba w systemie dziesiętnym: ", decimalValue)

print("Liczba w systemie",sysInfo,"wynosi:",number)