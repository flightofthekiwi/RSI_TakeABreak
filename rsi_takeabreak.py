# RSI_TakeABreak
# This program will sleep for an hour and then play a song
#
import time
import webbrowser

num = 1
while(num <= 3):
    time.sleep(5400)
    webbrowser.open("https://www.youtube.com/watch?v=yPYZpwSpKmA&spfreload=10")
    num = num + 1

print("Thank you for using TAKE A BREAK")
