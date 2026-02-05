from flask import Flask, render_template, request
from clima import get_weather

app = Flask(__name__)   

@app.route('/')
def index():
    return render_template('index.html')

@app.route(rule='/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = get_weather(city)

    if weather_data:
        return render_template(template_name_or_list= 'weather.html', weather=weather_data, city=city)
    else:
        return render_template(template_name_or_list= 'index.html', error="Ciudad no encontrada") 

if __name__ == '__main__':
    app.run(debug=True)
