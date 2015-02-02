# RSI_TakeABreak
# This program will remind you every 90 minutes to take a break
#
import time
import webbrowser

num = 1
while(num <= 3):
    time.sleep(5400)
    webbrowser.open("https://www.youtube.com/watch?v=yPYZpwSpKmA&spfreload=10")
    num = num + 1

print("Thank you for using TAKE A BREAK")
