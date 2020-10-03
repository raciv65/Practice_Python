import os
import csv

RawData=os.path.join("Resources","02-Homeworks_03-Python_Instructions_PyBank_Resources_budget_data.csv")

DateData=[]
GainData=[]

with open(RawData, "r", encoding="utf-8-sig") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    for row in csvreader:
        DateData.append(row[0])
        GainData.append(int(row[1]))

MonthsTotal=int(len(DateData))

GainTotal=0
for gain in GainData:
    GainTotal=GainTotal+gain

Delta=[]
i=0
while i<MonthsTotal-1:
    delta=GainData[i+1]-GainData[i]
    i=i+1
    Delta.append(delta)

def averange(numbers):
    n=len(numbers)
    total=0
    for x in numbers:
        total=total+x
    if n!=0:
        return total/n
    else:
        return 0

DateData.remove(DateData[0]) #To have the same legth of Delta list
DeltaValues=zip(DateData,Delta)
Results=sorted(DeltaValues, key=lambda x:x[1], reverse=True) #Sort by profit to loss

print(f"""Financial Analysis
---------------------------------------------------------------------
Total Months {MonthsTotal}
Total: {GainTotal:,} 
Averange Change: $ {round(averange(Delta),2):,}
Greatest Increase in Profits: {Results[0][0]} ( $ {Results[0][1]:,})
Greatest Decrease in Profits: {Results[len(Results)-1][0]} ( $ {Results[len(Results)-1][1]:,})
""")

SavePath=os.path.join("Analysis","Financial Analysis.txt")

with open(SavePath, "w", newline='', encoding="utf-8-sig") as datafile:
    writer=csv.writer(datafile)
    writer.writerow(['Finacial Analysis'])
    writer.writerow(['-------------------------------------------------------------------'])
    writer.writerow(['Total Months: {:n}'.format(MonthsTotal)])
    writer.writerow(['Total: $ {:n}'.format(GainTotal)])
    writer.writerow(['Average  Change: ${:n}'.format(round(averange(Delta),2))])
    writer.writerow(['Greatest Increase in Profits: '+str(Results[0][0])+' ( $ {:n})'.format(Results[0][1])])
    writer.writerow(['Greatest Decrease in Profits: '+str(Results[len(Results)-1][0])+' ( $ {:n})'.format((Results[len(Results)-1][1]))])
