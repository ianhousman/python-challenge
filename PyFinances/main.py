import csv
import os

months = 0
total = 0
changes = []
g_max = 0
increase = 0
increase_month = None
g_min = 0
decrease = 0
decrease_month = None

budget_data = os.path.join("..", "PyFinances", "Resources", "budget_data.csv")

with open(budget_data) as dFile:
    reader = csv.reader(dFile)
    next(reader)

    prev_row = 0
    for row in reader:
        months += 1
        total += int(row[0])
        change = int(row[0]) - prev_row
        prev_row = int(row[0])
        changes.append(change)

        

        if int(row[0]) > g_max:
            g_max = int(row[0])
            increase_month = row[1]
            increase = change
        if int(row[0]) < g_min:
            g_min = int(row[0])
            decrease_month = row[1]
            decrease = change

average = sum(changes)/len(changes)

print("""Financial Analysis
----------------------
Total Months: """ + str(months) + """
Total: """ + str('${}'.format(total)) + """
Average Change: """ + str('${:,.2f}'.format(average)) + """
Greatest Increase in Profits: """ + increase_month + " (" + str('${}'.format(increase)) + """)
Greatest Decrease in Profits: """ + decrease_month + " (" + str('${}'.format(decrease)) + ")")

Analysis = open('financial_analysis.txt', 'w')
Analysis.write("""Financial Analysis
----------------------
Total Months: """ + str(months) + """
Total: """ + str('${}'.format(total)) + """
Average Change: """ + str('${:,.2f}'.format(average)) + """
Greatest Increase in Profits: """ + increase_month + " (" + str('${}'.format(increase)) + """)
Greatest Decrease in Profits: """ + decrease_month + " (" + str('${}'.format(decrease)) + ")")

Analysis.close()