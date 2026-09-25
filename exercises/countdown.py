import time

given_time = int(input("Enter the time (in seconds): "))

for counter in range(given_time, 0, -1):

    seconds = counter % 60 
    #so that 60 vanda dherai seconds diyepaxi format nabigriyos. 
    minutes = int((counter / 60)) % 60 
    #60 vanda dherai seconds diyepaxi minutes ma janxa remaining time. 
    hours = int((counter / 3600)) % 60 
    #60 minutes i.e. 3600 seconds vanda dherai input chai hours ma gayera basxa and at that time minutes is XX:00:XX

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) 
    #every one second gap samma code rests. And this, applied in loop gives effect to a countdown effect. 

print("Time is UP!")