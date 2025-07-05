import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))....takes input from user
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):....phython me && use nhi krte and use krte h aur else if use nhi krte elif krte h
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")
