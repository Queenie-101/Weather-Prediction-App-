from flask import Flask, render_template, request
import json #build the response
import urllib.request #fetch data from URL
#name the app
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def weather():
    if request.method=='POST':
        #get city from form
        city=request.form['city']
    else:
        city='Texas'
    #api key
    api_key="3af7d864821fa0857b093ba8506360c9"
    #generate the rsponse
    try:
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key)
        #load the data
        data=json.load(source)
        #parse the data (read the tenperature)
        temperature=data['main']['temp']
        description=data['weather'][0]['description']
        return render_template('indext.html',city=city.upper(),temperature=temperature,description=description)
    except:
        return render_template('index.html',city='City Not Found')
if __name__=='__main__':
    app.run(debug=True)