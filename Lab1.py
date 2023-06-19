#Given the Dataset of a Bank (Bank.csv). The file has the following properties.
#Values are separated by a semicolon (;)
#The first line is the header row.
#You have to create a menu-driven program with the help of functions to perform the following:
#Without using the help of any libraries, open the given dataset.
#Print the headers in the file.
#Find the count of customers in each category 'marital'.
#Prepare a histogram for age using a print statement.

#solution
#Opening the dataset using open function and naming it ab.
ab = open("/Users/maheshk/Documents/GitHub/22112322_MalavikaNair_BEA372/bank.csv","r")
header=ab.readline()
data=ab.readlines()
#printing the headers in the file 
header = header.replace('"','').split(";")
for item in header:
    print(item)

#finding the count of customers in each category 'marital'
for value in data:
    value = value.replace('"','').split(",")
    print(value)
married=0
single=0
def marital(data):
    married=0
    single=0
    divorced=0

    for item in data:
        count=item.split(";")
        marital=count[2].strip('"')
        if marital=="married":
            married+=1
        elif marital=="single":
            single+=1
        else :
            divorced+=1
    print(married)
    print(single)
    print(divorced)
marital(data)

#creating histogram for age 
def age_histogram(data):
   ages = [] 
   lines = data.readlines()
   for line in lines[1:]:
    age = int(line.split(',')[0])
    ages.append(age)
    
age_histogram(data)
#setting ages into clusters of interval 10
interval_size = 10
#counting the occurrences within each interval
histogram = {}
for age in ages:
    interval = (age // interval_size) * interval_size
    if interval in histogram:
        histogram[interval] += 1
    else:
        histogram[interval] = 1
# Plot the histogram
for interval in sorted(histogram.keys()):
    frequency = histogram[interval]
    bar = '#' * frequency
    print(f'{interval}-{interval+interval_size}: {bar}')