
from flask import Flask, request, jsonify
from waitress import serve
from selenium_driverless.sync import webdriver
import time
from datetime import datetime

class Color:
    vert = '\033[92m'
    jaune = '\033[93m'
    rouge = '\033[91m'
    gris = '\033[90m'
    bleu = '\033[94m'
    violet = '\033[95m'
    veille = '\033[38;5;56m'
    thales = '\033[38;2;92;120;225m'
    cyan = '\033[96m'
    orange = '\033[38;5;178m'
    marron = '\033[38;2;205;133;63m'

app = Flask(__name__)



@app.route('/generate', methods=['POST'])
def generate_cookie_task():
    starttime = time.time()
    url = request.form["url"]
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--disable-images")
    options.add_argument("--disable-javascript")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless=new")
    timeout = 10 
    try :
        with webdriver.Chrome(options=options) as driver:  
            driver.get(url, timeout=timeout)
            reese = driver.get_cookie('reese84')["value"]
            endtime = time.time() 
            print(f"{Color.vert}{datetime.now()} - Successfully generated Reese cookie - Proccess done in {endtime - starttime} seconds") 
            return jsonify({"status": "done", "cookie": reese})
    except Exception as e:
        print(f"{Color.rouge}{datetime.now()} - Error generating Reese cookie: {str(e)}")
        return jsonify({"status": "failed", "cookie": None})
    
if __name__ == '__main__':
    print(f"{Color.violet}{datetime.now()} - Starting server")
    serve(app, host= "0.0.0.0", port=3000, threads=10)