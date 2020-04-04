import pandas as pd
import os
import glob

filePath = "/Users/lujan/PycharmProjects/combining_files/combined_results"
os.chdir(filePath)

fileName = "issueSeveritiesMonsterFile.csv"

# Project scope
projectNames = []
totalClasses = []
totalMethods = []

# CoverityScan
# ['High', 'Low', 'Medium']
totalCoverityScanIssues = []
numLowCoverityScanIssues = []
numMediumCoverityScanIssues = []
numHighCoverityScanIssues = []

# SonarQube
# ['MINOR', 'INFO', 'MAJOR', 'CRITICAL', 'BLOCKER']
totalSonarQubeIssues = []
numMinorSonarQubeIssues = []
numMajorSonarQubeIssues = []
numCriticalSonarQubeIssues = []
numInfoSonarQubeIssues = []
numBlockerSonarQubeIssues = []

# ['CODE_SMELL', 'BUG', 'VULNERABILITY']
numCodeSmellsSonarQube = []
numBugsSonarQube = []
numVulnerabilitiesSonarQube = []

# ['VERY_HIGH', 'HIGH', 'MEDIUM']
totalBCHIssues = []
numMediumBCHIssues = []
numHighBCHIssues = []
numVeryHighBCHIssues = []

for file in glob.glob("*.csv"):
    data = pd.read_csv(file)

    projectName = file.replace('_combined_results.csv', '')

    if projectName not in projectNames:
        projectNames.append(projectName)

    # Project scope
    totalSubClasses = 0
    totalSubMethods = 0
    allClassesInProject = []
    allMethodsInProject = []

    # CoverityScan
    totalCS = 0
    numLowCS = 0
    numMediumCS = 0
    numHighCS = 0

    # SonarQube
    totalSQ = 0
    numMinorSQ = 0
    numMajorSQ = 0
    numCriticalSQ = 0
    numInfoSQ = 0
    numBlockerSQ = 0

    numCodeSmells = 0
    numBugs = 0
    numVulnerabilities = 0

    # BCH
    totalBCH = 0
    numMediumBCH = 0
    numHighBCH = 0
    numVeryHighBCH = 0

    index = 0

    while index < len(data['Severity/Impact']):
        tool = data['Tool'][index]
        type = data['Type'][index]
        severity = data['Severity/Impact'][index]
        function = data['Function'][index]

        className = str(function)

        if className.find(".") != -1:
            splitString = function.split(".")
            className = splitString[0]

        if className not in allClassesInProject:
            allClassesInProject.append(className)
            totalSubClasses += 1

        if str(function) not in allMethodsInProject:
            allMethodsInProject.append(str(function))
            totalSubMethods += 1

        if tool == 'CoverityScan':
            totalCS += 1

            if severity == 'Low':
                numLowCS += 1

            elif severity == 'Medium':
                numMediumCS += 1

            elif severity == 'High':
                numHighCS += 1

        elif tool == 'SonarQube':
            totalSQ += 1

            # Severity types
            if severity == 'MINOR':
                numMinorSQ += 1

            elif severity == 'INFO':
                numInfoSQ += 1

            elif severity == 'MAJOR':
                numMajorSQ += 1

            elif severity == 'CRITICAL':
                numCriticalSQ += 1

            elif severity == 'BLOCKER':
                numBlockerSQ += 1

            # Issue types
            if type == 'CODE_SMELL':
                numCodeSmells += 1

            elif type == 'BUG':
                numBugs += 1

            elif type == 'VULNERABILITY':
                numVulnerabilities += 1

            else:
                print('There is a fourth code type')

        elif tool == 'BetterCodeHub':
            totalBCH += 1

            if severity == 'VERY_HIGH':
                numVeryHighBCH += 1

            elif severity == 'HIGH':
                numHighBCH += 1

            elif severity == 'MEDIUM':
                numMediumBCH += 1

        index += 1

    totalClasses.append(totalSubClasses)

    totalMethods.append(totalSubMethods)

    totalCoverityScanIssues.append(totalCS)
    numLowCoverityScanIssues.append(numLowCS)
    numMediumCoverityScanIssues.append(numMediumCS)
    numHighCoverityScanIssues.append(numHighCS)

    totalSonarQubeIssues.append(totalSQ)
    numMinorSonarQubeIssues.append(numMinorSQ)
    numMajorSonarQubeIssues.append(numMajorSQ)
    numCriticalSonarQubeIssues.append(numCriticalSQ)
    numInfoSonarQubeIssues.append(numInfoSQ)
    numBlockerSonarQubeIssues.append(numBlockerSQ)
    numCodeSmellsSonarQube.append(numCodeSmells)
    numBugsSonarQube.append(numBugs)
    numVulnerabilitiesSonarQube.append(numVulnerabilities)

    totalBCHIssues.append(totalBCH)
    numMediumBCHIssues.append(numMediumBCH)
    numHighBCHIssues.append(numHighBCH)
    numVeryHighBCHIssues.append(numVeryHighBCH)

mainDict = {'projectName': projectNames, 'totalClasses': totalClasses, 'totalMethods': totalMethods, 'totalCoverityScan': totalCoverityScanIssues,
         'numLowCoverityScan': numLowCoverityScanIssues, 'numMediumCoverityScan': numMediumCoverityScanIssues,
         'numHighCoverityScan': numHighCoverityScanIssues, 'totalSonarQube': totalSonarQubeIssues,
         'numMinorSonarQube': numMinorSonarQubeIssues, 'numMajorSonarQube': numMajorSonarQubeIssues,
         'numCriticalSonarQube': numCriticalSonarQubeIssues, 'numInfoSonarQube': numInfoSonarQubeIssues,
         'numBlockerSonarQube': numBlockerSonarQubeIssues, 'numCodeSmells': numCodeSmellsSonarQube,'numBugs': numBugsSonarQube, 'numVulnerabilities': numVulnerabilitiesSonarQube, 'totalBCH': totalBCHIssues, 'numMediumBCH': numMediumBCHIssues,
         'numHighBCH': numHighBCHIssues, 'numVeryHighBCH': numVeryHighBCHIssues}

table = pd.DataFrame(mainDict)

table = table[['projectName', 'totalClasses', 'totalMethods', 'totalCoverityScan', 'numLowCoverityScan', 'numMediumCoverityScan',
'numHighCoverityScan', 'totalSonarQube', 'numMinorSonarQube', 'numMajorSonarQube', 'numCriticalSonarQube',
'numInfoSonarQube', 'numBlockerSonarQube', 'numCodeSmells', 'numBugs', 'numVulnerabilities', 'totalBCH', 'numMediumBCH', 'numHighBCH', 'numVeryHighBCH']]
os.chdir("/Users/lujan/PycharmProjects/combining_files")

table.sort_values("projectName", axis = 0, ascending = True,
                 inplace = True, na_position ='last')

table.to_csv(fileName)
print(len(projectNames))