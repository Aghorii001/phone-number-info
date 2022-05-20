import os
import sys
import phonenumbers

from phone_iso3166.country import phone_country
from phonenumbers import geocoder
from phonenumbers import carrier

os.system('clear')

print ("+===================================+")
print ("|        Phone Number Info          |")
print ("+===================================+")
print ("| Author : Ravi                     |")
print ("| Github : github.com/Aghorii001    |")
print ("+===================================+")
print
phone_number=raw_input("Enter a phone number(Ex:880)            :")
country_name=raw_input("Enter a country name(Ex:BD,US,UK etc :) :")
number = phonenumbers.parse(phone_number,country_name)
print ("Country                                 :"+ geocoder.description_for_number(number,"en"))
number2 = phonenumbers.parse(phone_number,country_name)
print ("Sim Company/Carrier                     :"+ carrier.name_for_number(number2,"en"))
