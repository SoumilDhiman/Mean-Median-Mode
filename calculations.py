import csv
from collections import Counter
with open('SOCR-HeightWeight.csv',newline = '') as d:
    df = csv.reader(d)
    data = list(df)
data.pop(0)
newData = []
for i in range(len(data)):
    num = data[i][1]
    newData.append(float(num))
#mean
number = len(newData)
value = 0
for a in newData:
    value = value+a
mean = value/number
print("Mean is: "+ str(mean))
#median
num = len(newData)
newData.sort()
if num% 2 == 0:
    median1 = float(newData[num//2])
    median2 = float(newData[num//2-1])
    median = (median1+median2)/2
else:
    median = newData[num//2]
print("Median is: "+str(median))
#mode
count = Counter(newData)
range = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurance in count.items():
    if 50<float(height)<60:
        range["50-60"]+=occurance
    elif 60<float(height)<70:
        range["60-70"]+=occurance
    elif 70<float(height)<80:
        range["70-80"]+=occurance
range1,occ1 = 0,0
for mrange,occurance in range.items():
    if occurance>occ1:
        range1,occ1 = [int(mrange.split("-")[0]),int(mrange.split("-")[1])],occurance
        mode = float((range1[0]+range1[1])/2)
print("Mode: "+str(mode))