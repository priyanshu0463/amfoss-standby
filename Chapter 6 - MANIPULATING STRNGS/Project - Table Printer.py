tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


def printTable(Table):
    colWidths = [0] * len(tableData)
    
    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i], key=len))
        # print(colWidths[i])

    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end='    ')
        
        print('')
printTable(tableData)