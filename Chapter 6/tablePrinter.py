tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)

for i in range(0, len(tableData)):
    for j in tableData[i]:
        if len(j) > colWidths[i]:
            colWidths[i] = len(j)

#print(colWidths) # print computed column widths

def printTable():
    for i in range(0, len(tableData[0])):
        print(tableData[0][i].rjust(colWidths[0]) + ' ' + tableData[1][i].rjust(colWidths[1]) + ' ' + tableData[2][i].rjust(colWidths[2]))

printTable()
