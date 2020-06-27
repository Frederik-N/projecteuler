# Problem 22 - Names Scores
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
#  begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
#  by its alphabetical position in the list to obtain a name score.
#
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 
# 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

datastring = ""
listofnames = []
total = 0

def firstNames():
    # Open the file and put it into a string
    datafile = open('p022_names.txt',"r")
    if(datafile.mode == 'r'):
        global datastring
        datastring = datafile.read()

    # Scan the datastring and put each name into a list
    while(len(datastring) > 0):
        nameStart = datastring.index('"')
        nameEnd = datastring[nameStart+1::].index('"')
        name = ''.join(datastring[nameStart+1:nameEnd+1:])
        datastring = datastring[nameEnd+3::len(datastring[0])]
        global listofnames
        listofnames.append(name)

    # use sorted() to sort the list
    listofnames = sorted(listofnames)

    # Calculate the value for each name and add it to the total value

    multiplier = 0
    for x in listofnames:
        multiplier = multiplier + 1

        #iterate each character in the name and give it value
        numbersInX = []
        for y in x:
            numbersInX.append(ord(y)-64)
        print(numbersInX)
        
        
        value = sum(numbersInX) * multiplier
        global total
        total = total + value
firstNames()
print(total)
