from pymongo import MongoClient
from datetime import datetime
from termcolor import colored
cluster = MongoClient("Write Mongo db")
db = cluster["socialmedia"]["messaging"]
all = db.find({})
date = datetime.now().strftime("%x")

for messages in all:
    try:
        if date != messages["date"]:
            print(colored(f"Today - {messages['time']}", 'red'))
        else:
            print(colored(f"{messages['date']} - {messages['time']}", 'red'))
        print(colored("From: ", 'green'), messages['id'])
        print(colored("Message: ", 'green'), messages['message'])
        print("-------------")
    except:
        pass


person = input("Name: ")
message = input("Message: ")

time = datetime.now().strftime("%X")
msg = {"id" : person, "message":message, "date":date, "time":time}
db.insert_one(msg)
