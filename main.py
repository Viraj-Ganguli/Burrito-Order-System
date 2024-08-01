import datetime
import urllib.parse
import csv

#====SUGGESTED GLOBAL VARIABLES====#
#dictionary for locations
locations_dict = {}
#dictionary for burrito types
burrito_dict = {}
#dictionary with toppings
toppings_dict = {}
#declare a Python set of topping choices and add each user selection to it
topping_choices_set = set()
#=========================#


def file_to_dict(file, dict):
  with open(file, 'r') as file:
    csv_reader = csv.DictReader(file, )
    dict = [row for row in csv_reader]
    return dict


locations_dict = file_to_dict('data/locations.csv', locations_dict)
burrito_dict = file_to_dict('data/burrito.csv', burrito_dict)
toppings_dict = file_to_dict('data/toppings.csv', toppings_dict)
price_list = []


def main():

  total_price = 0
  location = get_locations()  # store address in location
  burrito = get_burrito()  # returns string value of selected burrito
  toppings = get_toppings()  # to be stored in topping_choices_set
  for ele in range(0, len(price_list)):
    total_price = total_price + float(price_list[ele])

  print("\nConfirming your choices")
  print(f"You ordered a {burrito} burrito with {', '.join(toppings)}")
  print(f"Your total is ${round(total_price,2)}")
  # print the burrito choice, topping choices and total price

  # calculate pickup time: adjust to EST (-5 hrs), but add 15 for prep time
  pickup_time = datetime.datetime.now() - datetime.timedelta(hours=4,
                                                             minutes=45)
  # print pickup time and provide link to location
  print(f"Please pick up at: {location} at {pickup_time.strftime('%I:%M %p')}")
  print(
      f"Directions: https://www.google.com/search?q={urllib.parse.quote_plus(location)}"
  )


def get_locations():
  #prompt the user for a zip code and list all restaurants in that zip
  zip_request = input("Please enter a zip code to find restaurants near you: ")
  locations = []
  i = 1
  z=0
  for i, sub in enumerate(locations_dict):
    if sub['zip'] == zip_request:
      z += 1
      print(f"{z}) {sub['address']} [{sub['city']}] {sub['state']} {sub['zip']} ")
     

      locations.append(str(f"{sub['address']} [{sub['city']}] {sub['state']} {sub['zip']} "))
      
      

  if not locations:
    print("No restaurants found in the given zip code. Please try again.")
    return get_locations()
  try:
    location_choice = int(
      input("Enter the number of the location you want to order from: "))
    selected_location = locations[location_choice - 1]
    print(f"Pickup at: {selected_location}")
    return selected_location
  except (ValueError, IndexError):
    print("Invalid input. Please try again.")
    return get_locations()


def get_burrito():
  burritos = file_to_dict(
      'data/burrito.csv',
      burrito_dict)  # string variable to store burrito type
  #read in burritos CSV and load dictionary

  #print burrito options menu using burrito_dict

  #prompt user to input valid number selection for burrito they want
  print("\nMENU")
  for i, burritos in enumerate(burritos, start=1):
    print(f"{i}) {burritos['key']} ${burritos['value']}")

  while True:
    try:
      burrito_choice = int(input("Enter the number of the burrito you want: "))
      items = list(burrito_dict)
      selected_burrito = items[burrito_choice - 1]['key']
      price_list.append(items[burrito_choice - 1]['value'])
      print(f"Confirming {selected_burrito}")
      return str(selected_burrito)
    except (ValueError, IndexError):
      print("Invalid option, try again.")


def get_toppings():
  #read in toppings CSV and load toppings_dict

  #print topping options menu using toppings_dict
  toppings = file_to_dict(
      'data/toppings.csv',
      toppings_dict)  # string variable to store burrito type
  #read in toppings CSV and load dictionary

  #print burrito options menu using burrito_dict

  #prompt user to input valid number selection for burrito they want
  print("\nMENU")
  selected_toppings = set()
  for i, toppings in enumerate(toppings, start=1):
    print(f"{i}) {toppings['key']} ${toppings['value']}")
  print(f"{len(toppings_dict)+1}) Remove Last Item")
  print(f"{len(toppings_dict)+2}) Done")
  while True:
    try:
      topping_choice = int(
          input("Enter the number of the toppings you want: "))
      if topping_choice is (len(toppings_dict)+2):
        print("Thank you for ordering!")
        return selected_toppings
      elif len(selected_toppings) != 0 and topping_choice is (len(toppings_dict) + 1):
        selected_toppings.pop()
        print(f"Confirming {', '.join(selected_toppings)}")
        
      else:
        items = list(toppings_dict)
        selected_toppings.add(items[topping_choice - 1]['key'])
        price_list.append(items[topping_choice - 1]['value'])
        print(f"Confirming {', '.join(selected_toppings)}")
    except (ValueError, IndexError):
      print("Invalid option, try again.")

#prompt user to input valid number selection for toppings they want,
#continue to loop and re-prompt user for more toppings until they
#type the menu choice indicating "DONE"

if __name__ == "__main__":
  main()
