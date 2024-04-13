#Greeting the person according to the current time in their country
import time
name = input("Enter your name: ")
timestamp_total = time.strftime('%H:%M:%S')
timestamp_hour = int(time.strftime('%H'))
if(timestamp_hour>=12 & timestamp_hour<=16):
    print("Good Afternoon", name)
    print("Current Time is:",timestamp_total)
elif(timestamp_hour>16 & timestamp_hour<=19):
    print("Good Evening", name)
    print("Current Time is:",timestamp_total)
elif(timestamp_hour>19 & timestamp_hour<=4):
    print("Good Night", name)
    print("Current Time is:",timestamp_total)
elif(timestamp_hour>4 & timestamp_hour<12):
    print("Good Morning", name)
    print("Current Time is:",timestamp_total)