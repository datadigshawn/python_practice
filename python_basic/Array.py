from array import *
arr=[]
j=0
for i in range(0,5):
    print i
    j += 1
    
    arr.append([i,j])
    
print arr
WS=int(raw_input("Enter WorkSheet Number:"))
print arr[WS][1]
# Loop over rows.
for row in arr:
    # Loop over columns.
    for column in row:
        print("COL:", column)
    print("row[0]:", row[0])
    print("row[1]:", row[1])
    print("\n")
