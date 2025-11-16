import requests
#leaving my key in because I don't anyone is gonna chief this are they? T_T
key = "5cde8aff4cc84a0597a203303251611"
baseUrl = 'http://api.weatherapi.com/v1'
currentWeather = '/current.json'
#example = http://api.weatherapi.com/v1/current.json?key=<YOUR_API_KEY>&q=London
usrZipCode = input("Enter zipcode:")
while len(usrZipCode) != 5 or not usrZipCode.isdigit():
    print("Invalid zipcode please try again.")
    usrZipCode = input()
response = requests.get(baseUrl+currentWeather+'?key='+key+'&q='+usrZipCode)
if response.status_code != 200:
    print('api error occurred')
data = response.json()
city = data['location']['name']
temp = data['current']['temp_f']
feels = data['current']['feelslike_f']
condition = data['current']['condition']['text']

print(f'City: {city},\ntemp: {temp}, \nfeels like {feels}, \nCondition: {condition}')