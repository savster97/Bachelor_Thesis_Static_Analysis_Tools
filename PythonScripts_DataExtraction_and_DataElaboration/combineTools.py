import pandas as pd
import os
import glob

mainPath = "/Users/lujan/PycharmProjects/combining_files/combined_results/"
os.chdir(mainPath)

fileName = "classesMonsterFile.csv"

projectNames = []
classNames = []
coverityScan = []
sonarQube = []
betterCodeHub = []
startLines = []
endLines = []

numberOfCSIssues = 0

for file in glob.glob("*.csv"):

    filePath = mainPath + file
    data = pd.read_csv(filePath)

    projectName = file.replace('_combined_results.csv', '')

    numRows = len(data['Issue'])
    print(numRows)
    index = 0

    while index < numRows:
        function = data['Function'][index]

        className = str(function)

        if className.find(".") != -1:
            splitString = function.split(".")
            className = splitString[0]

        startLine = data['startLine'][index]
        endLine = data['endLine'][index]
        tool = data['Tool'][index]
        issue = data['Issue'][index]

        if tool == "CoverityScan":
            projectNames.append(projectName)
            classNames.append(className)
            coverityScan.append(issue)
            sonarQube.append("")
            betterCodeHub.append("")
            startLines.append(startLine)
            endLines.append(endLine)

            numberOfCSIssues += 1

        elif tool == "SonarQube":
            projectNames.append(projectName)
            classNames.append(className)
            coverityScan.append("")
            sonarQube.append(issue)
            betterCodeHub.append("")
            startLines.append(startLine)
            endLines.append(endLine)

        elif tool == "BetterCodeHub":
            projectNames.append(projectName)
            classNames.append(className)
            coverityScan.append("")
            sonarQube.append("")
            betterCodeHub.append(issue)
            startLines.append(startLine)
            endLines.append(endLine)

        else:
            print("Error in naming")

        index += 1

print("Number of Coverity Issues in Total: " + str(numberOfCSIssues))

mainDictionary = {'projectName': projectNames, 'className': classNames, 'coverityScan': coverityScan, 'sonarQube': sonarQube,
                  'betterCodeHub': betterCodeHub, 'startLines': startLines, 'endLines': endLines}
table = pd.DataFrame(mainDictionary)

table = table[['projectName', 'className', 'coverityScan', 'sonarQube', 'betterCodeHub', 'startLines', 'endLines']]
table.sort_values("className", axis = 0, ascending = True,
                 inplace = True, na_position ='last')

numOfCSIssuesArray = 0
for object in coverityScan:
    if object != "":
        numOfCSIssuesArray += 1

print(numOfCSIssuesArray)

os.chdir('/Users/lujan/PycharmProjects/combining_files')

table.to_csv(fileName)
