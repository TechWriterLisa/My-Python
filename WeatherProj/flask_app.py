import requests
from flask import Flask, render_template, request

app = Flask(__name__)
api_key = '58654466206badc3e5327616988bb48c'

@app.route('/', methods=['GET','POST'])
def index():
    weather_data = {}
    city = 'Dallas'
    if request.method == 'POST':
        city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data['temp'] = data['main']['temp']
        weather_data['desc'] = data['weather'][0]['description']
        #print(f'Temperature: {temp} K')
        #print(f'Description: {desc}')
    else:
        print('Error fetching weather data')    
    # Pass the data to the template
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)