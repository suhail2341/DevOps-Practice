import smtplib
import requests
from email.mime.text import MIMEText

#getting data from openweathermap and storing it in json format
city = input("Enter City Name (note:write first letter in caps): ")
print("wait a moment...")
api_key='enter your api key here'
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

#checking if city name is valid or not
if data.status_code == 404:
    print("enter valid city name")
    exit()

#extracting data from json file and storing it in variables
jsonf = data.json()
city_name = jsonf['name']
weather = jsonf['weather'][0]['description']
temp = jsonf['main']['temp']-273.15
feels_like = jsonf['main']['feels_like']-273.15
humidity = jsonf['main']['humidity']

#creating a message to be sent in structured format
message = MIMEText(f"City: {city}\nWeather: {weather}\nTemperature: {temp}\nFeels Like: {feels_like}\nHumidity: {humidity}")
message['Subject'] = f"Weather Report of {city_name}"
message['From'] = "sam's email bot"


#sending email using smtplib and gmail
server = smtplib.SMTP('smtp.gmail.com',587)

#starttls() is used to start the connection using TLS encryption
server.starttls()
receiver = input("Enter Receiver's Email: ")

#logging in and sending email
try:
    server.login('your email','your password')
    server.sendmail('your email',receiver,message.as_string())
    server.quit()
    print('\nmail sent')
#exception handling if any error occurs
except:
    print('\nmail not sent')
