from _datetime import datetime
import hashlib
import random

def blockchain(previous_hash ,i):
    blockid = input("Enter the blockid = ")
    timestamp = datetime.now()
    date_time = timestamp.strftime("%m/%d/%Y, %H:%M:%S")
    print("time ",timestamp)
    data = input("Enter the data = ")
    nonce = random.randint(1,500)
    print("nonce = ",nonce)
    print("Previous Block Hash =" ,previous_hash)
    text = blockid + str(date_time+data) + str(nonce) + str(previous_hash)
    text1 = hashlib.md5(text.encode('utf-8')).hexdigest()
    print("new hash = ",text1)
    datain = input("\ndo you want to continue for next block y/n ?")
    if(datain=="y"):
        i+1
        blockchain(text1,i)
i=0
previous_hash = str(0)
blockchain(previous_hash,i)