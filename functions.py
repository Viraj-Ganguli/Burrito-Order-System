import requests
import json

def get_locations(zip):
	my_dict = {}
	try:
		receive = requests.get('https://api.abaxterfcps.repl.co/cmg/' + zip, timeout=10)
		my_dict = json.loads(receive.text)
	except requests.exceptions.RequestException:
		f = open.json("json/22030.json")
		my_dict = json.load(f)
	return my_dict