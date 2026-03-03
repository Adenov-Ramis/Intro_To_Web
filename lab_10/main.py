from flask import Flask
import math
app = Flask(__name__)
@app.route('/')
def home():
    radius = 5
    area = math.pi * math.pow(radius, 2)
    return f'Hello, area that equals to {area}!'

if __name__ == '__main__':
    app.run(debug=True)