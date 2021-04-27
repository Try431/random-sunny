from flask import Flask, render_template
import random_sunny

app = Flask(__name__,static_folder='static')

@app.route('/')
def home_page():
    random_sunny.cleanup()
    return render_template('landing.html')

@app.route('/sunny/<duration>')
def sunny(duration):
    if int(duration) > 60:
        return render_template('too_big.html')
    random_sunny.cleanup()
    output_filename = random_sunny.trim(duration)
    return render_template('sunny.html', output_file = "videos/"+output_filename)