import serial 
import pyrebase
import time
import os
#======================================================================
#firebase part start
#======================================================================
config = {
	"apiKey":"AIzaSyBblQpJtEIKQXX8ju4aLhomzjtwztf0u7g",
	"authDomain":"noqstore-2a96a.firebaseapp.com",
	"databaseURL":"https://noqstore-2a96a.firebaseio.com",
	"storageBucket":"noqstore-2a96a.appspot.com",
	"serviceAccount":"/var/www/html/noQstore-48c9c414792e.json"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("akul753@gmail.com","noQstore123")
db = firebase.database()
#======================================================================
#firebase part end
#======================================================================
#hardware section
#======================================================================
os.system("sudo chmod 777 /dev/ttyACM0")
ser = serial.Serial('/dev/ttyACM0',9600)
print "\t\t\tWELCOME TO THE NOQStore\n"
time.sleep(2)
print "\t\tTHE SYSTEM WILL CALIBRATE THE SENSORS FIRST\n"
print "\t\tSYSTEM IS ONLINE\n\n"
while True:
	
	str = ser.readline()
	print str
	if len(str)<=6:
		print "CALIBRATION COMPLETE"
		time.sleep(0.5)
		print "PRODUCT READY TO WORK"
		time.sleep(0.5)
		print "REMOVE WEIGHT WITHIN 5 SEC FOR ACCURATE RESULTS\n\n"
		time.sleep(0.5)
	while len(str)<= 6:
		weight_present = ser.readline()
		x = long(weight_present)
		print "\t\t========================="
		print "\t\tPresent weight: ",x
		print "\t\t--------------------------"
		time.sleep(2)
		weight_next = ser.readline()
		y = long(weight_next)
		print "\t\tNext reading: ",y
		print "\t\t--------------------------"
		print "\t\tDifference in weight: ",x-y
		print "\t\t--------------------------"
		if x-y>=20:
			print "\t\tITEM SOLD"
			db.child("events").update({"item_id": "0"}, user['idToken']) #firebase update on sale
			print "\t\t=========================\n\n"	
			break
		elif y<0:
			print "\t\ti am pissed off"
			print "\t\t=========================\n\n"	
		else :
			print "\t\tyou saved my ass"
			print "\t\t=========================\n\n"	
		
		time.sleep(2)
#==============================================================
#end of code
#==============================================================
