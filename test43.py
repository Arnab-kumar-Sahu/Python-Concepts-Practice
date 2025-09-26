import datetime
import time

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print("⏰ Current Time:", now, end="\r",flush=True)  # force overwrite Explanation: \r moves cursor back to the start
    time.sleep(1)   #flush=True tells Python:
                    #“Don’t wait — write this output to the console right now.”
                    #Without flush=True, the output might lag, especially inside loops with end="\r" or time.sleep().

