def transmit_to_space(message):
	"This is the enclosed function"
	def data_transmitter():
		"The nested function"
		print(message)
	
	data_transmitter()
print(transmit_to_space("Test Message"))



def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
	number=3
        print(number)
    printer()
    print(number)

print_msg(9)

