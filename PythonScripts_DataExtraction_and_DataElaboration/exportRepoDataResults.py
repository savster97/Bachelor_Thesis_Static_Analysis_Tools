import pandas as pd
import math
import os

data = pd.read_json('jqc_redacted.json')

repos = data['repo']

index1 = 0

NORMAL_ISSUES = {'AUTOMATE_TESTS', 'COUPLE_ARCHITECTURE_COMPONENTS_LOOSELY', 'SEPARATE_CONCERNS_IN_MODULES', 'SMALL_UNIT_INTERFACES', 'WRITE_SIMPLE_UNITS', 'WRITE_SHORT_UNITS'}
RANGE_ISSUES = {'WRITE_CLEAN_CODE'}
LOCATIONS_ISSUES = {'WRITE_CODE_ONCE'}

while index1 < len(repos):
    if data['status'][index1] == "Analysis done.":

        # Creating Combined Table for Project
        Tool = []
        Issue = []
        Severity = []
        Function = []
        startLine = []
        endLine = []

        dict = {'Tool': Tool, 'Issue': Issue, 'Severity/Impact': Severity, 'Function': Function, 'startLine': startLine,
                'endLine': endLine}
        table = pd.DataFrame(dict)

        repoName = data['repo'][index1]
        filePath = os.getcwd() + '/work_copy/bettercodehub_results/' + repoName + 'results.csv'

        results = pd.DataFrame(data['analysisResults'][index1])
        refactoringCandidates = results['refactoringCandidates']

        index2 = 0

        while index2 < len(refactoringCandidates):
            if isinstance(refactoringCandidates[index2], list):
                issue = results['guideline'][index2]
                tool = 'BetterCodeHub'

                rc = refactoringCandidates[index2]
                index3 = 0

                while index3 < len(rc):
                    sub_rc = rc[index3]

                    if issue in NORMAL_ISSUES:
                        function = sub_rc['name']
                        severity = sub_rc['severity']
                        startLine = sub_rc['startLine']
                        endLine = sub_rc['endLine']

                        table = table.append(
                            {'Tool': tool, 'Issue': issue, 'Severity/Impact': severity,
                             'Function': function,
                             'startLine': startLine,
                             'endLine': endLine}, ignore_index=True)

                    elif issue in RANGE_ISSUES:
                        function = sub_rc['name']
                        severity = sub_rc['severity']
                        lineRanges = sub_rc['lineRanges']

                        for lineRange in lineRanges:
                            startLine = lineRange['startLine']
                            endLine = lineRange['endLine']

                            table = table.append(
                                {'Tool': tool, 'Issue': issue, 'Severity/Impact': severity,
                                 'Function': function,
                                 'startLine': startLine,
                                 'endLine': endLine}, ignore_index=True)

                    elif issue in LOCATIONS_ISSUES:
                        locations = sub_rc['locations']
                        for location in locations:
                            function = location['name']
                            severity = location['severity']
                            startLine = location['startLine']
                            endLine = location['endLine']

                            table = table.append(
                                {'Tool': tool, 'Issue': issue, 'Severity/Impact': severity,
                                 'Function': function,
                                 'startLine': startLine,
                                 'endLine': endLine}, ignore_index=True)


                    index3 += 1

            index2 += 1
        table.to_csv(filePath, index=None, header=True)
    index1 += 1