# Modules needed for the script
import socket
import subprocess
import sys
from datetime import datetime

# Clears the screen
# subprocess.call('clear', shell=True)

# Asks for input or defaults to local host if none is given
remoteServer = raw_input("Enter the host you would like to scan")
remoteServerIP = socket.gethostbyname(remoteServer)

if remoteServer ==""
	print("_"*60)
	print("Scanning local computer")
	print("_"*60)
	remoteServer = "127.0.0.1"
	remoteServer1 = socket.gethostbyname(remoteServer)
else 
	print("_"*60)
	print("Scanning $d %(remoteServerIP)")
	print("_"*60)

# Check time when the scan was started
t1 = datetime.now()

'''
Using range to find the specific ports with Error handling
'''

safePorts = [22, 443, 53, 465,  

try:
	for port in range(1, 1025) 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOCK_DGRAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0
			print("Port{}:	Open".format(port))
		elif result == 0
			print("Port{}:	Open".format(port))
		sock.close

except Keyboardinterrupt:
	print("You pressed Ctrl+C")
	sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()


# Checking the time again
t2 = datetime.now()


# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1


# Printing the information to screen
print("Scanning Completed in:", total)
