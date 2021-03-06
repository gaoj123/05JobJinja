import random

def parseCSV(csv, includeFirstLine):
    rows = csv.split("\n")
    if(not includeFirstLine):
        rows = rows[1:]
    valuesByRow = []
    for row in rows:
        row = row.strip()
        if(len(row) > 0):
            columns = [""]
            quote = False
            for c in row:
                if(c == '"' and quote == False):
                    quote = True
                elif(c == '"' and quote == True):
                    quote = False
                elif(c == ',' and quote == False):
                    columns.append("")
                else:
                    columns[-1] += c
            valuesByRow.append(columns)
    return valuesByRow

def makeDictionary(parsedCSV):
    dict = {}
    for row in parsedCSV:
        dict[row[0]] = float(row[1])
    return dict

#Given an integer total and a dictionary where values are 0-100,
#returns a weightedly random job
def randJob(total,dict):
    if total <= 0:
        total = dict.pop("Total") * 10
    count=0;
    ranInt=random.randrange(0,total);
    for item in dict:
        count+=dict[item]*10;
        if(ranInt<count):
            return item;

if __name__ == "__main__":    
    file = open("data/occupations.csv", 'r')
    a = parseCSV(file.read(), False)
    total=float(a[-1][1])*10;
    a = a[:-1]
    dict = makeDictionary(a)
    file.close()
