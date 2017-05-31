"""
    A program to remind user to take a break at defined interval.
    The program opens users favourite youtube video in the browser.
    Any one can customize their own break time and youtube link.
"""

# import time for time functions
import time
# import webbrowser for functions opening url in webbrowser
import webbrowser

# get current time and other variable declarations
current_time = time.ctime() # time function
# initialize total number of breaks
total_breaks = 6
# initialize break counter
break_count = 0

# main code
print ("This program started on = " + current_time)
# loop to open web browser every 30 minute
while (break_count < total_breaks):
    # break time
    time.sleep(10) # time functions 80
    # youtube link
    url="https://youtu.be/PaBwPRa__ic"
    # open link saved in url variable
    webbrowser.open(url)
    # display log
    print("Played video @ " + time.ctime())
    # increment break counter
    break_count = break_count + 1
