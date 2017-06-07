# 3 main ways to calculate the time consumption in python

# method 1 - datetime
import datetime
start_time = datetime.datetime.now()
a = []
for i in range(10000000, 0, -1):
    a.append(i)
a.sort()
end_time = datetime.datetime.now()
print("{}s".format(end_time - start_time))

# method 2 - time.time()
# to calculate in seconds
import time
start = time.time()
a = []
for i in range(10000000, 0, -1):
    a.append(i)
a.sort()
end = time.time()
print("{}s".format(end - start))

# method 3 - time.clock()
# to calculate in system clock times
import time
start = time.clock()
a = []
for i in range(10000000, 0, -1):
    a.append(i)
a.sort()
end = time.clock()
print("{} clock time".format(end - start))