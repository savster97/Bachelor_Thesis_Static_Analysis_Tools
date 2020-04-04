import pandas as pd
import os
import glob

mainPath = "/Users/lujan/PycharmProjects/combining_files/combined_results/"
os.chdir(mainPath)

# Creating Combined Table for Project
projectName = []
Tool = []
Issue = []
Severity = []
Type = []
Function = []
startLine = []
endLine = []

dict = {'projectName': projectName,'Tool': Tool, 'Issue': Issue, 'Severity/Impact': Severity, 'Type': Type, 'Function': Function, 'startLine': startLine,
        'endLine': endLine}
table = pd.DataFrame(dict)

for file in glob.glob("*.csv"):
    filePath = mainPath + file
    repoName = file.replace('_combined_results.csv', '')

    data = pd.read_csv(filePath)
    numRows = len(data['Issue'])
    index = 0

    while index < numRows:
        projectName = repoName
        tool = data['Tool'][index]
        issue = data['Issue'][index]
        severity = data['Severity/Impact'][index]
        typ = data['Type'][index]
        function = data['Function'][index]
        startLine = data['startLine'][index]
        endLine = data['endLine'][index]

        table = table.append(
            {'projectName': projectName, 'Tool': tool, 'Issue': issue, 'Severity/Impact': severity, 'Type': typ, 'Function': function, 'startLine': startLine,
             'endLine': endLine}, ignore_index=True)

        index += 1

os.chdir("/Users/lujan/PycharmProjects/combining_files")
monsterFileName = 'allProjectResultsCombined.csv'
table.sort_values("Function", axis = 0, ascending = True,
                inplace = True, na_position ='last')
table.to_csv(monsterFileName)


