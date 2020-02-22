import csv
import numpy as np


names = []
count1 = 0
count2 = 0
name1 = None
name2 = None

with open('Resources/houston_election_data.csv', errors = 'ignore') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        names.append(row[0])


BKcount = names.count("Bill King")
BKpercent1 = (BKcount/len(names))
BKpercent = format(BKpercent1, ".2%")
BKinfo = {"name": "Bill King", "count": BKcount, "percent": BKpercent}
if BKcount > count1:
    count1 = BKcount
    name1 = "Bill King"
elif BKcount > count2:
    count2 = BKcount
    name2 = "Bill King"

DScount = names.count("Demetria Smith")
DSpercent1 = (DScount/len(names))
DSpercent = format(DSpercent1, ".2%")
DSinfo = {"name": "Demetria Smith", "count": DScount, "percent": DSpercent}
if DScount > count1:
    count1 = DScount
    name1 = "Demetria Smith"
elif DScount > count2:
    count2 = DScount
    name2 = "Demetria Smith"

DBcount = names.count("Derrick Broze")
DBpercent1 = (DBcount/len(names))
DBpercent = format(DBpercent1, ".2%")
DBinfo = {"name": "Derrick Broze", "count": DBcount, "percent": DBpercent}
if DBcount > count1:
    count1 = DBcount
    name1 = "Derrick Broze"
elif DBcount > count2:
    count2 = DBcount
    name2 = "Derrick Broze"

DABcount = names.count("Dwight A. Boykins")
DABpercent1 = (DABcount/len(names))
DABpercent = format(DABpercent1, ".2%")
DABinfo = {"name": "Dwight A. Boykins", "count": DABcount, "percent": DABpercent}
if DABcount > count1:
    count1 = DABcount
    name1 = "Dwight A. Boykins"
elif BKcount > count2:
    count2 = DABcount
    name2 = "Dwight A. Boykins"

JTcount = names.count('Johnny "J.T." Taylor')
JTpercent1 = (JTcount/len(names))
JTpercent = format(JTpercent1, ".2%")
JTinfo = {"name": 'Johnny "J.T." Taylor', "count": JTcount, "percent": JTpercent}
if JTcount > count1:
    count1 = JTcount
    name1 = 'Johnny "J.T." Taylor'
elif JTcount > count2:
    count2 = JTcount
    name2 = 'Johnny "J.T." Taylor'

KBcount = names.count("Kendall Baker")
KBpercent1 = (KBcount/len(names))
KBpercent = format(KBpercent1, ".2%")
KBinfo = {"name": "Kendall Baker", "count": KBcount, "percent": KBpercent}
if KBcount > count1:
    count1 = KBcount
    name1 = "Kendall Baker"
elif KBcount > count2:
    count2 = KBcount
    name2 = "Kendall Baker"

NHcount = names.count("Naoufal Houjami")
NHpercent1 = (NHcount/len(names))
NHpercent = format(NHpercent1, ".2%")
NHinfo = {"name": "Naoufal Houjami", "count": NHcount, "percent": NHpercent}
if NHcount > count1:
    count1 = NHcount
    name1 = "Naoufal Houjami"
elif NHcount > count2:
    count2 = NHcount
    name2 = "Naoufal Houjami"

RVcount = names.count("Roy J. Vasquez")
RVpercent1 = (RVcount/len(names))
RVpercent = format(RVpercent1, ".2%")
RVinfo = {"name": "Roy J. Vasquez", "count": RVcount, "percent": RVpercent}
if RVcount > count1:
    count1 = RVcount
    name1 = "Roy J. Vasquez"
elif RVcount > count2:
    count2 = RVcount
    name2 = "Roy J. Vasquez"

SLcount = names.count("Sue Lovell")
SLpercent1 = (SLcount/len(names))
SLpercent = format(SLpercent1, ".2%")
SLinfo = {"name": "Sue Lovell", "count": SLcount, "percent": SLpercent}
if SLcount > count1:
    count1 = SLcount
    name1 = "Sue Lovell"
elif SLcount > count2:
    count2 = SLcount
    name2 = "Sue Lovell"

STcount = names.count("Sylvester Turner")
STpercent1 = (STcount/len(names))
STpercent = format(STpercent1, ".2%")
STinfo = {"name": "Sylvester Turner", "count": STcount, "percent": STpercent}
if STcount > count1:
    count1 = STcount
    name1 = "Sylvester Turner"
elif STcount > count2:
    count2 = STcount
    name2 = "Sylvester Turner"

TBcount = names.count("Tony Buzbee")
TBpercent1 = (TBcount/len(names))
TBpercent = format(TBpercent1, ".2%")
TBinfo = {"name": "Tony Buzbee", "count": TBcount, "percent": TBpercent}
if TBcount > count1:
    count1 = TBcount
    name1 = "Tony Buzbee"
elif TBcount > count2:
    count2 = TBcount
    name2 = "Tony Buzbee"

VRcount = names.count("Victoria Romero")
VRpercent1 = (VRcount/len(names))
VRpercent = format(VRpercent1, ".2%")
VRinfo = {"name": "Victoria Romero", "count": VRcount, "percent": VRpercent}
if VRcount > count1:
    count1 = VRcount
    name1 = "Victoria Romero"
elif VRcount > count2:
    count2 = VRcount
    name2 = "Victoria Romero"

print("""
Houston Mayoral Election Results
---------------------------------
Total Votes Cast: """ + str(len(names)) + """
---------------------------------""")
print(f'{STinfo["name"]}: {STinfo["percent"]} ({STinfo["count"]})')
print(f'{TBinfo["name"]}: {TBinfo["percent"]} ({TBinfo["count"]})')
print(f'{BKinfo["name"]}: {BKinfo["percent"]} ({BKinfo["count"]})')
print(f'{DABinfo["name"]}: {DABinfo["percent"]} ({DABinfo["count"]})')
print(f'{VRinfo["name"]}: {VRinfo["percent"]} ({VRinfo["count"]})')
print(f'{SLinfo["name"]}: {SLinfo["percent"]} ({SLinfo["count"]})')
print(f'{DSinfo["name"]}: {DSinfo["percent"]} ({DSinfo["count"]})')
print(f'{RVinfo["name"]}: {RVinfo["percent"]} ({RVinfo["count"]})')
print(f'{KBinfo["name"]}: {KBinfo["percent"]} ({KBinfo["count"]})')
print(f'{DBinfo["name"]}: {DBinfo["percent"]} ({DBinfo["count"]})')
print(f'{NHinfo["name"]}: {NHinfo["percent"]} ({NHinfo["count"]})')
print(f'{JTinfo["name"]}: {JTinfo["percent"]} ({JTinfo["count"]})')
print(f'''---------------------------------
1st Advancing Candidate: {name1}
2nd Advancing Candidate: {name2} 
---------------------------------''')

Results = open('election_results.txt', 'w')
Results.write("""
Houston Mayoral Election Results
---------------------------------
Total Votes Cast: """ + str(len(names)) + """
---------------------------------""" + '\n')
Results.write(f'''{STinfo["name"]}: {STinfo["percent"]} ({STinfo["count"]})
{TBinfo["name"]}: {TBinfo["percent"]} ({TBinfo["count"]})
{BKinfo["name"]}: {BKinfo["percent"]} ({BKinfo["count"]})
{DABinfo["name"]}: {DABinfo["percent"]} ({DABinfo["count"]})
{VRinfo["name"]}: {VRinfo["percent"]} ({VRinfo["count"]})
{SLinfo["name"]}: {SLinfo["percent"]} ({SLinfo["count"]})
{DSinfo["name"]}: {DSinfo["percent"]} ({DSinfo["count"]})
{RVinfo["name"]}: {RVinfo["percent"]} ({RVinfo["count"]})
{KBinfo["name"]}: {KBinfo["percent"]} ({KBinfo["count"]})
{DBinfo["name"]}: {DBinfo["percent"]} ({DBinfo["count"]})
{NHinfo["name"]}: {NHinfo["percent"]} ({NHinfo["count"]})
{JTinfo["name"]}: {JTinfo["percent"]} ({JTinfo["count"]})
---------------------------------
1st Advancing Candidate: {name1}
2nd Advancing Candidate: {name2} 
---------------------------------''')

Results.close()