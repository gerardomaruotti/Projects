import time
from mqtt_client import Temperature_Manager

if __name__ == "__main__":
	test = Temperature_Manager("/tiot/devices/1234","/tiot/devices/1234",'localhost')
	a = 0
	isConnectionStarted = 1
	statisticsReceived = []
	
	while (True):
		option = input("Please enter a value:\n- 1 to start the program\n- 0 to exit\n")
		if option == "1":
			if isConnectionStarted == False:
				test.start()
				isConnectionStarted = True
			option = input("Choose the duration for the connection (in seconds): ")
			while (a < int(option)):
				a += 1
				time.sleep(1)
		if option == "0":
			test.stop()
			option = input("Would you like to see the statistics collected? (y/n) ")
			if option == "y":
				print(statisticsReceived)
			break
		a = 0

	print("Program ended succesfully!\n")