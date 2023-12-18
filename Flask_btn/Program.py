from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17, GPIO.LOW)

btn_stato = False
stato_int = 0
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    #GPIO.output(17, GPIO.LOW)
    #global btn_stato
    #btn_stato = False
    return render_template('home.html')

@app.route('/Accendi')
def Accendi():
    global btn_stato
    global stato_int
    stato_int = 0
    if btn_stato:
        GPIO.output(17, GPIO.LOW)
        message = "Il led è Spento!"
        print(message)
    else:  
        GPIO.output(17,GPIO.HIGH)
        message = "Il led è Acceso!"
        print(message)  

    btn_stato = not btn_stato
    
    if btn_stato :
        stato_int = 1
    return jsonify({'stato': stato_int})

@app.route('/Setup')
def setup():
    #global btn_stato
    global stato_int
    return jsonify({'stato': stato_int})

if __name__ == '__main__':
    app.run(debug=True, host='10.42.0.1')
