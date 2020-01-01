
from hashid import HashId

def insertAppDetails(ApplicationRecords, name, phone, memRef, status):
    l = [name, phone, memRef, status]
    hashvalue = HashId(name)
    ApplicationRecords[hashvalue] = l