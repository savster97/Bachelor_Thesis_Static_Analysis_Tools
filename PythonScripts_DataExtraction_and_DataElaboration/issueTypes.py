import pandas as pd

# Creating Combined Issue
sonarQubeIssue = []
coverityScanIssue = []
betterCodeHubIssue = []

filePath = '/Users/lujan/PycharmProjects/combining_files/allProjectResultsCombined.csv'
data = pd.read_csv(filePath)

projects = []

numRows = len(data['Issue'])
index = 0

while index < numRows:
    tool = data['Tool'][index]
    issue = data['Issue'][index]
    name = data['projectName'][index]

    if name not in projects:
        projects.append(name)

    if tool == "SonarQube":
        if issue not in sonarQubeIssue:
            sonarQubeIssue.append(issue)

    elif tool == "CoverityScan":
        if issue not in coverityScanIssue:
            coverityScanIssue.append(issue)

    elif tool == "BetterCodeHub":
        if issue not in betterCodeHubIssue:
            betterCodeHubIssue.append(issue)

    index += 1

print(len(projects))

dictOne = {'sonarQubeIssue': sonarQubeIssue}
dictTwo = {'coverityScanIssue': coverityScanIssue}
dictThree = {'betterCodeHubIssue': betterCodeHubIssue}

tableOne = pd.DataFrame(dictOne)
tableTwo = pd.DataFrame(dictTwo)
tableThree = pd.DataFrame(dictThree)

fileNameOne = 'issueTableSonarQube.csv'
fileNameTwo = 'issueTableCoverityScan.csv'
fileNameThree = 'issueTableBetterCodeHub.csv'

tableOne.to_csv(fileNameOne)
tableTwo.to_csv(fileNameTwo)
tableThree.to_csv(fileNameThree)
