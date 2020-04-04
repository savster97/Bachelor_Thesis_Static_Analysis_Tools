import pandas as pd
import os
import glob

# Figuring out whether results exists for all three tools
def extractResults():
    repos = []

    # Checking BCH
    os.chdir('/Users/lujan/PycharmProjects/combining_files/work_copy/bettercodehub_results/JavaQualitasCorpus')

    for file in glob.glob("*.csv"):
        repoName = file.replace('results.csv', '')
        repos.append(repoName)

    # Checking CoverityScan and SonarQube
    os.chdir('/Users/lujan/PycharmProjects/combining_files/work_copy/coverityscan_results')
    for repo in repos:

        cs_fileName = 'JavaQualitasCorpus-' + repo + '.csv'
        cs_filePath = '/Users/lujan/PycharmProjects/combining_files/work_copy/coverityscan_results/' + cs_fileName

        repoNameSplit = repo.split('-')
        sq_fileName = 'QC-'+ repoNameSplit[0] + '/sonar-issues.csv'
        sq_filePath = '/Users/lujan/PycharmProjects/combining_files/work_copy/sonarqube_results/target/extraction/' + sq_fileName

        bch_fileName = repo + 'results.csv'
        bch_filePath = '/Users/lujan/PycharmProjects/combining_files/work_copy/bettercodehub_results/JavaQualitasCorpus/' + bch_fileName

        if os.path.isfile(cs_filePath) and os.path.isfile(sq_filePath):
            print(repo)
            os.chdir('/Users/lujan/PycharmProjects/combining_files/combined_results')
            combineTools(repo, cs_filePath, sq_filePath, bch_filePath)

def combineTools(repo, csPath, sqPath, bchPath):

    # Creating Combined Table for Project
    Tool = []
    Issue = []
    Type = []
    Severity = []
    Function = []
    startLine = []
    endLine = []

    dict = {'Tool': Tool, 'Issue': Issue, 'Type': Type, 'Severity/Impact': Severity, 'Function': Function, 'startLine': startLine,
            'endLine': endLine}
    table = pd.DataFrame(dict)

    # Collecting Data from CoverityScan
    cs_fileInput = pd.read_csv(csPath)
    numRows = len(cs_fileInput['Type'])
    index = 0

    while index < numRows:
        tool = 'CoverityScan'
        issue = cs_fileInput['Type'][index]
        type = "NaN"
        impact = cs_fileInput['Impact'][index]
        function = cs_fileInput['Function'][index]

        table = table.append(
            {'Tool': tool, 'Issue': issue, 'Type': type,  'Severity/Impact': impact, 'Function': function, 'startLine': 0,
             'endLine': 0}, ignore_index=True)

        index += 1

    # Collecting Data from SonarQube
    sq_fileInput = pd.read_csv(sqPath)
    numRows = len(sq_fileInput['rule'])
    index = 0

    while index < numRows:
        tool = 'SonarQube'
        issue = sq_fileInput['rule'][index]
        type = sq_fileInput['type'][index]
        severity = sq_fileInput['severity'][index]
        functionPath = sq_fileInput['component'][index]
        splitFunctionPath = functionPath.split("/")
        function = splitFunctionPath[len(splitFunctionPath) - 1]

        line1 = sq_fileInput['startLine'][index]
        line2 = sq_fileInput['endLine'][index]

        table = table.append(
            {'Tool': tool, 'Issue': issue, 'Type': type, 'Severity/Impact': severity, 'Function': function, 'startLine': line1,
             'endLine': line2}, ignore_index=True)

        index += 1

    # Collecting Data from BetterCodeHub
    bch_fileInput = pd.read_csv(bchPath)
    numRows = len(bch_fileInput['Issue'])
    index = 0

    while index < numRows:
        tool = bch_fileInput['Tool'][index]
        issue = bch_fileInput['Issue'][index]
        type = "NaN"
        severity = bch_fileInput['Severity/Impact'][index]
        function = bch_fileInput['Function'][index]
        startLine = bch_fileInput['startLine'][index]
        endLine = bch_fileInput['endLine'][index]

        table = table.append(
            {'Tool': tool, 'Issue': issue, 'Type': type, 'Severity/Impact': severity, 'Function': function, 'startLine': startLine,
             'endLine': endLine}, ignore_index=True)

        index += 1

    combineResultsFileName= repo + '_combined_results.csv'
    # table.sort_values("Function", axis = 0, ascending = True,
    #              inplace = True, na_position ='last')
    table.to_csv(combineResultsFileName)
    print(combineResultsFileName)

extractResults()