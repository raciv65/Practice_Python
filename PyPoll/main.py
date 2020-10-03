import csv
import os

fileData=os.path.join("Resources","02-Homeworks_03-Python_Instructions_PyPoll_Resources_election_data.csv")

CandidateData=[]
with open(fileData, "r", encoding="UTF-8") as csvfile:
    cvsreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(cvsreader)
    for row in cvsreader:
        CandidateData.append(row[2])

total=len(CandidateData)
Candidates=[]
Votes=[]
for candidate in set(CandidateData):
    Candidates.append(candidate)
    Votes.append(CandidateData.count(candidate))

zipped=zip(Candidates, Votes)
data={candidato:número for candidato, número in zipped}
lista=sorted(data.items(), key=lambda x:x[1], reverse=True)
print(lista)