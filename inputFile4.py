def greet(name):
	"""
    This function greets to
	the person passed in as
	parameter
    """
	print("Hello, " + name + ". Good morning!")
while(True):
    name = input("input your name : ")
    if (name != ""):
        greet(name)
    else:
        break