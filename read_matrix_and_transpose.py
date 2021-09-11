import csv
import sys

mtrx=[]
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      if len(row)==3:
        a=[float(row[0]),float(row[1]),float(row[2])]
        mtrx.append(a)
      else:
        print("!=3")
#for row in mtrx:
#    print(row)
rez = [[mtrx[j][i] for j in range(len(mtrx))] for i in range(len(mtrx[0]))]  #transpose a matrix
print(rez)
