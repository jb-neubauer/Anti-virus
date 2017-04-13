# Import time for sleep
import time

# while loop
'''while(True):
	print("looping.....")
	time.sleep(2)'''

count = 0
while (count < 100):
	print("loop number: %d" % (count +1))
	count +=1
import random
while(True):
	num = random.randint(1, 25)
	print(num)

	if(num == 13):
		print("Stopping")
		break
	else:
		print("Still looping")
