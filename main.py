# Import Module RPi.GPIO dan Flask
import RPi.GPIO as GPIO
from flask import Flask, render_template

# Membuat Object Flask dan simpan ke dalam variabel app
app = Flask(__name__, template_folder="template", static_folder="template")

# Pilih mode GPIO Board 
GPIO.setmode(GPIO.BOARD)
# Setting PIN 13 Sebagai Output LED
GPIO.setup(13, GPIO.OUT)


@app.route("/")
def Home():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)

    # Cek Pin 13 Input Aktif / Tidak ( Jika Aktif maka True , Jika tidak maka False)
    check_gpio = GPIO.input(13)
    if check_gpio:
        status = 'Active'
    else:
        status = 'Non Active'
    # Return data ke index.html
    return render_template("index.html", status=status)


@app.route("/action/<state>")
def Action(state):
    # Jika path ( state ) dalam request URL adalah ON
    # Maka LED berstatus TRUE 
    if state == 'ON':
        GPIO.output(13, True)
        return 'LED ON'
    else:
        GPIO.output(13, False)
        return 'LED OFF'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
