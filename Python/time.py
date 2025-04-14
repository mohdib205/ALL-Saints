

# -------------------- Time module --------------------

# Time module provide various time related functions
# It allows to work with time in python

# Before using, the module is needed to be imported
import time

##print(dir(time))

##print(time.time())
'''
 The function time.time() returns the current system
time in ticks
 since 12:00am, January 1, 1970(epoch)
'''
##print(time.asctime())

##local=time.localtime()
##print("Year" ,local.tm_year)
##print("Month" ,local.tm_mon)
##print("Day" ,local.tm_mday)
##print("hour" ,local.tm_hour)

# The time.sleep() method provides time-lapse or
##delay
# between the execution of the current processes
##or threads.
##time.sleep(4)
##for i in range(1,15):
##    if i%2==0:
##        print(i)
##        time.sleep(2)

##start_time=time.time()
##for i in range(250):
##    if i%2==0:
##        print(i)
##end_time=time.time()
##print("difference_time" , end_time-start_time)


import calendar as cal

print(cal.month(2024,11))
print(cal.calendar(2024))



# To get the current time details in a format of time structure 
##LOCAL = time.localtime()
##print(LOCAL)


# To get time in readable format we use time.asctime()
##print(time.asctime
