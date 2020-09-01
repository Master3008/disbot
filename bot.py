import discord
import datetime
import os
import psycopg2
client = discord.Client()
@client.event

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

cur.execute('''CREATE TABLE STUDENT
      (ADMISSION INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      COURSE        CHAR(50),
      DEPARTMENT        CHAR(50));''')

async def on_member_update(before, after):
    if str(before.status) == "offline":
        if str(after.status) == "online":
            print("{} is now {}.".format(after.name,after.status)) 
            currentDT = datetime.datetime.now()
            
            cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')");
            conn.commit()
            conn.close()
 
            
    if str(before.status) == "online":
        if str(after.status) == "offline":
            print("{} has gone {}.".format(after.name,after.status))
           
            currentDT = datetime.datetime.now()
            
 
           
         
        
            
client.run(os.getenv('TOKEN'))
