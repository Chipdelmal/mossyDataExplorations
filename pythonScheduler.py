# Before running, install the Python library:
#
# pip install schedule
#
# This is modified from their sample program:
import schedule
import time
import os

# import dataMerge_VB

# def job(t):
#     print("I'm working...", t)
#     return
def job():
    print("I'm working...")
    os.system('python3 dataMerge_VB.py')
    print("done")
    return

# schedule.every().day.at("01:00").do(job,'It is 01:00')
#
# schedule.every().monday.at("10:30").do(job)
schedule.every().second.do(job)

while True:
    schedule.run_pending()
    # time.sleep(60) # wait one minute
    time.sleep(1) # wait one minute
