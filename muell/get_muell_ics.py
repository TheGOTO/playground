import requests
from bs4 import BeautifulSoup
from ics import Calendar, Event


url = 'https://tonnenleerung.de/nd-sob/schrobenhausen/hafnerweg/'
response = requests.get(url)

if response.status_code == 200:
    html = response.content

soup = BeautifulSoup(html, 'html.parser')



input_data = soup.find_all("script")[1]

input_data=str(input_data)
input_data=input_data.replace("\"","")

blau="blau"
gelb="gelb"
braun="braun"
grau="grau"
grau4="grau4"


pos_start_blau = input_data.find(blau)
pos_start_gelb = input_data.find(gelb)
pos_start_braun = input_data.find(braun)
pos_start_grau = input_data.find(grau)
pos_start_grau4 = input_data.find(grau4)


pos_end_blau = input_data.find("]",pos_start_blau,len(input_data))
pos_end_gelb = input_data.find("]",pos_start_gelb,len(input_data))
pos_end_braun = input_data.find("]",pos_start_braun,len(input_data))
pos_end_grau = input_data.find("]",pos_start_grau,len(input_data))
pos_end_grau4 = input_data.find("]",pos_start_grau4,len(input_data))

str_blau=input_data[pos_start_blau+len(blau)+7:pos_end_blau]
str_gelb=input_data[pos_start_gelb+len(gelb)+7:pos_end_gelb]
str_braun=input_data[pos_start_braun+len(braun)+7:pos_end_braun]
str_grau=input_data[pos_start_grau+len(grau)+7:pos_end_grau]
str_grau4=input_data[pos_start_grau4+len(grau4)+7:pos_end_grau4]


array_blau=str_blau.split(",")
array_gelb=str_gelb.split(",")
array_braun=str_braun.split(",")
array_grau=str_grau.split(",")
array_grau4=str_grau4.split(",")



def add_events(c,elements,name):

	for element in elements:

		e = Event()
		e.name = name
		e.begin = element
		e.make_all_day()
		c.events.add(e)
	return c

c = Calendar()

c=add_events(c,array_blau,"blau Tonne")
c=add_events(c,array_gelb,"gelbe Tonne")
c=add_events(c,array_braun,"bio Tonne")
c=add_events(c,array_grau,"schwarze Tonne")

#print(c.events)


with open('muell.ics', 'w') as f:
    f.writelines(c.serialize_iter())
# And it's done !

# iCalendar-formatted data is also available in a string
c.serialize()

