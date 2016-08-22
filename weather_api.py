import urllib2, json

city_names = ['Nairobi', 'Lagos', 'London']
app_key = '2bc3e79bb974a007818864813f53fd35'
url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}&units=metric'

print "City".ljust(15), "Temperature".ljust(15), "Description"
print '='*50  

def get_weather():
	
#loops through city names list and passes it to weather api url. 
#data is opened, read and passed to result.
#json presents the data as a dictionary. Pass this to Postman for easier reading

	for city in city_names:    
		result = urllib2.urlopen(url.format(city, app_key)).read()
		data = json.loads(result) 
		print city.ljust(15), str(data['main']['temp']).ljust(15), data['weather'][0]['description']

			
get_weather()			