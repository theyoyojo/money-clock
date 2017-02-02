import time
import math

#[system specific functions]

#dynamic print function
def prn(string):
	print string

#dynamic input function
def inp(prompt):
	return raw_input(prompt)

#debug notifications
def notify(string):
	prn(string)

#loop exit condition
def checkForExitCondition():
	#TODO
	#detect some kind of key press
	#return True if pressed
	#else False
	return False

#prompt for hourly wage
def getWage():
	wage = inp('What is your hourly wage?\n>>')
	try:
		float(wage)
	except ValueError:
		notify("Incorrect use of getWage()")
		prn("Please enter a number.\n")
		return getWage()
	else:
		return float(wage)

#pretty sure this one is universal but not certain
def getTime():
	return time.time()

#display in console
def display (money, dSeconds):
	hours,minutes,seconds = splitTime(dSeconds)
	prn("Money made: %.2f\tWorked:\
%.2f Hours %.2f Minutes %.2f Seconds" % (money,hours,minutes,seconds))


#[system generic functions]


#check if a string is really a string
def isString(str):
	try:
		str + ''
	except TypeError:
		return False
	else:
		return True

#check if a float is really a float
def isFloat(flo):
	try:
		flo + 1.1
	except TypeError:
		return False
	else:
		return True


#Convert from one time format to another
#Key s = seconds, m = minutes, h = hours
def convert(time,frm,to):
	badUse = "Incorrect use of convert()"

	#make sure inputs are in the proper format
	if not isString(frm) or not isString(to) or not isFloat(time):
		notify(badUse)
		return -1

	#If the input is in hours:
	if frm == 'h':
		if to == 's':
			return time * 3600.0
		elif to == 'm':
			return time * 60.0
		elif to == 'h':
			return time
		#for improper use
		else:
			nofify(badUse)
			return -1
	#if the input is in minutes
	if frm == 'm':
		if to == 's':
			return time * 60.0
		elif to == 'm':
			return time
		elif to == 'h':
			return time / 60.0
		#for improper use
		else:
			nofify(badUse)
			return -1
	#if the input is in seconds
	if frm == 's':
		if to == 's':
			return time
		elif to == 'm':
			return time / 60.0
		elif to == 'h': 
			return time / 3600.0
		#for improper use
		else:
			nofify(badUse)
			return -1
	else:
		notify(badUse)
		return -1

#get time elapsed. D = delta. Make sure the units are the same!
def getDTime(start, now):
	return now - start

def getDTime(start):
	return math.floor(getTime()) - start

#calculate money earned up to that point
def calcMoney(hWage,dSeconds):
	hSeconds = convert(dSeconds,'s','h')
	return hSeconds * hWage


#turn an amount of elapsed time from raw hours into hours,minutes,seconds
#first letter, in this case 's', designates units.
#the actual name of the variable is what that varible represents 
def splitTime(sInput):
	sHours = sInput - (sInput % 3600)
	sMinutes = sInput - sHours - (sInput % 60)
	seconds = sInput - sHours - sMinutes

	return convert(sHours,'s','h'),convert(sMinutes,'s','m'),seconds

#main event loop
def eventLoop(start,wage):
	exitCondition = False
	while exitCondition == False:
		
		#get elapsed time in seconds
		dSeconds = getDTime(start)

		#calculate money earned
		money = calcMoney(wage,dSeconds)
		
		#update display
		display(money,dSeconds)

		#check for exit condition
		exitCondition = checkForExitCondition()

		#wait 1 second
		time.sleep(1)

		#repeat
	return

#function to test convert()
#delete the # to switch function off
#'''
def convertTest():
	prn('Testing convert().')
	
	time = float(inp("\ninput time\n>>>"))
	frm = str(inp("\nfrom?\n>>>"))
	to = str(inp('\nto?\n>>>'))

	prn('Output: %.3f' % convert(time,frm,to))
	return
#'''

#debug loop to test functions

def testLoop():
	loop = True
	while loop == True:
		convertTest()
		loop = exitCondition()
	return

#probably self explanatory
def main():
	wage = getWage()
	start = math.floor(getTime())
	eventLoop(start,wage)
	return 1


#testLoop()
#initialization
main()

#print splitTime(6.2)

