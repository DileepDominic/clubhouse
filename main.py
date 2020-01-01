
from insertAppDetails import insertAppDetails

#Data Structures
applicantRecords = {}

#Functions

def initializeHash():
    print("initializeHash")
    applicantRecords = {}

def updateAppDetails(ApplicationRecords, name, phone, memRef, status):
    print("updateAppDetails")

def memRef(ApplicationRecords, memID):
    print("memRef")

def appStatus(StudentHashRecords):
    print("appStatus")

def destroyHash(StudentHashRecords):
    print("destroyHash")



def readfile(inputLocation):
    with open(inputLocation) as inputFile:
        for record in inputFile:
            recordAttributes = record.split("/")
            insertAppDetails(applicantRecords,recordAttributes[0],recordAttributes[1],recordAttributes[2],recordAttributes[3])

def main():
    print("Main file")
    readfile("data/inputPS8.txt")
    initializeHash()
    print(applicantRecords.keys())
    for key in applicantRecords.keys():
        print(applicantRecords[key])

main()
