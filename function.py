def counting():
    fileName=input("Enter The File Name: ")
    file=open(fileName,'r')
    numberOfWords=0 
    for line in file:
        words=line.split(" ")
        numberOfWords=numberOfWords+len(words)

    print("Number Of Words: ",numberOfWords) 

counting()