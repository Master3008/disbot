import discord
import datetime
client = discord.Client()
@client.event


async def on_member_update(before, after):
    if str(before.status) == "offline":
        if str(after.status) == "online":
            print("{} is now {}.".format(after.name,after.status))
            file = open('log.txt','a') 
            currentDT = datetime.datetime.now()
            
            file.write("{} is now {}.       ".format(after.name,after.status))
            file.write(str(currentDT))
            file.write("\n")
 
            file.close()
    if str(before.status) == "online":
        if str(after.status) == "offline":
            print("{} has gone {}.".format(after.name,after.status))
            file = open('log.txt','a')
            currentDT = datetime.datetime.now()
            
 
            file.write("{} has gone {}.      ".format(after.name,after.status))
            file.write(str(currentDT))

            file.write("\n")
 
            file.close()
         
        
            
client.run(os.getenv('TOKEN'))
