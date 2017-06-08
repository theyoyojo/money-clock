import time
import math

#[system specific functions]

#dynamic print function
def prn(string):
	print(string)

#dynamic input function
def inp(prompt):
	return input(prompt)

#debug notifications
def notify(string):
	prn(string)

#welcome message for basic console loop
def getWelcomeMessage(option):
	if option == 'basicConsole':
		message = "=========================================================\
\nWelcome to the Money Clock. Press Ctrl+C to save and exit.\n\
========================================================="
	return message

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

#display in console
def display(money, dSeconds):
	hours,minutes,seconds = splitTime(dSeconds)
	prn("Money made: %.2f\tWorked: \
%.0f Hours %.0f Minutes %.0f Seconds" % (money,hours,minutes,seconds))

#get name of save file (or name file to create)
def getSaveName():
	name = inp("Name of save file?\n>")
	return name

def save(name, money, wage, start, end):
	hours,minutes,seconds = splitTime(end-start)
	sDate = time.strftime("%A, %d %B %Y",time.localtime(start))
	sTime = time.strftime("%I:%M:%S %p", time.localtime(start))
	eDate = time.strftime("%A, %d %B %Y",time.localtime(end))
	eTime = time.strftime("%I:%M:%S %p",time.localtime(end))
	target = open(name,'a')
	target.write("\n\
On %s, you began working at %s.\n\
You worked for %.0f hours, %.0f minutes, and %.0f seconds.\n\
You made %.2f at %.2f per hour in your local currency.\n\
You finished working on %s, at %s.\n\n----------\n"\
% (sDate,sTime,hours,minutes,seconds,money,wage,eDate,eTime))
	return

#pretty sure this one is universal but not certain
def getTime():
	return math.floor(time.time())

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
def convert(time, frm, to):
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
def calcMoney(hWage, dSeconds):
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

#basic console event loop
def basicConsoleLoop(wage, start):
	while True:
		try:	
			#get elapsed time in seconds
			dSeconds = getDTime(start)

			#calculate money earned
			money = calcMoney(wage,dSeconds)
			
			#update display
			display(money,dSeconds)

			#wait 1 second
			time.sleep(1)

			#repeat
		except KeyboardInterrupt:
			break
	end = getTime()
	save(getSaveName(),money,wage,start,end)
	return 1

#main event loop (not in use, todo: detect specific exit condition, clean)
def eventLoop(wage, start):
	exitCondition = False
	while exitCondition == False:
		try:	
			#get elapsed time in seconds
			dSeconds = getDTime(start)

			#calculate money earned
			money = calcMoney(wage,dSeconds)
			
			#update display
			display(money,dSeconds)

			#update file
			#TODO?

			#check for exit condition
			exitCondition = checkForExitCondition()

			#wait 1 second
			time.sleep(1)

			#repeat
		except KeyboardInterrupt:
			break
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
	print(getWelcomeMessage("basicConsole"))
	wage = getWage()
	start = getTime()
	basicConsoleLoop(wage,start)
	return 1


#testLoop()
#initialization
main()

