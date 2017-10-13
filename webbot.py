import RPi.GPIO as GPIO
import time

from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Set pin names and numbers
leftfwd = 23
leftrev = 18
rightfwd = 17
rightrev = 22

# Set each pin as an output
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# Set the time (in seconds) that each motor will turn for
turn_time = 0.2

@app.route("/")
def main():
	return render_template('main.html')

# The function below is executed when the "forward" button is pressed
@app.route("/forward")
def forward():
	GPIO.output(leftfwd, True)
	GPIO.output(rightfwd, True)
	# move forward twice as fast as the other directions
	time.sleep(turn_time*2)
	GPIO.output(rightfwd, False)
	GPIO.output(leftfwd, False)
	return "ok"
	
# The function below is executed when the "back" button is pressed
@app.route("/back")
def back():
	GPIO.output(leftrev, True)
	GPIO.output(rightrev, True)
	time.sleep(turn_time)
	GPIO.output(leftrev, False)
	GPIO.output(rightrev, False)
	return "ok"
	
# The function below is executed when the "right" button is pressed
@app.route("/right")
def right():
	GPIO.output(leftfwd, True)
	GPIO.output(rightrev, True)
	time.sleep(turn_time)
	GPIO.output(leftfwd, False)
	GPIO.output(rightrev, False)
	return "ok"	
	
# The function below is executed when the "left" button is pressed
@app.route("/left")
def left():
	GPIO.output(leftrev, True)
	GPIO.output(rightfwd, True)
	time.sleep(turn_time)
	GPIO.output(leftrev, False)
	GPIO.output(rightfwd, False)
	return "ok"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)

