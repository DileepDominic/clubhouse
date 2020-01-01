
from insertAppDetails import insertAppDetails
import hashlib

#Data Structures
applicantRecords = {}

#Functions

def initializeHash():
    print("initializeHash")

def updateAppDetails(ApplicationRecords, name, phone, memRef, status):
    print("updateAppDetails")

def memRef(ApplicationRecords, memID):
    print("memRef")

def appStatus(StudentHashRecords):
    print("appStatus")

def destroyHash(StudentHashRecords):
    print("destroyHash")

def HashId(applicantName):
    hashvalue = int(hashlib.sha256(applicantName.encode('utf-8')).hexdigest(), 16) % 10**8
    return hashvalue


def readfile(inputLocation):
    with open(inputLocation) as inputFile:
        for record in inputFile:
            recordAttributes = record.split("/")
            l = [recordAttributes[0],recordAttributes[1],recordAttributes[2],recordAttributes[3]]
            d = {'name': recordAttributes[0],'phone':recordAttributes[1],'memRef':recordAttributes[2],'status':recordAttributes[3]}
            hashvalue = HashId(recordAttributes[0])
            applicantRecords[hashvalue] = l
            #dic = {recordAttributes[0]:l}
            #applicantRecords.add(dic)


def main():
    print("Main file")
    readfile("data/inputPS8.txt")
    print(applicantRecords.keys())
   # for i in applicantRecords:
       # print("record")
   #     print(i)


main()
