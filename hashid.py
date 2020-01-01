
import hashlib
def HashId(applicantName):
    hashvalue = int(hashlib.sha256(applicantName.encode('utf-8')).hexdigest(), 16) % 10**8
    return hashvalue