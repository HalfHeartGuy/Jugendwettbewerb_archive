import  datetime
import time
start = datetime.datetime.now()


print(datetime.datetime.now() - start)

for i in range(10):
    time.sleep(1)
    print((datetime.datetime.now() - start).seconds)