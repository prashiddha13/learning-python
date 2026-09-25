import time

given_time = int(input("Enter the time (in seconds): "))

for counter in range(given_time, 0, -1):

    seconds = counter % 60 
    #So that the format isn't messed up if input time is more than 60 secs. 
    minutes = int((counter / 60)) % 60 
    #If more than 60 seconds is given as input, remaining time will be stored in minutes (converted) 
    hours = int((counter / 3600)) % 60 
    #Inputs greater than 60 minutes, i.e. 3600 seconds, are converted to hours, and at that time, minutes are in XX:00:XX format.

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) 

print("Time is UP!")