from asyncore import loop
from fileinput import filename


def wordsfromfile():
    filename=input("Enter the file name: ")
    numberofwords=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print(numberofwords)
wordsfromfile()