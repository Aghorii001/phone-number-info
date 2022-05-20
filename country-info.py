import os
import sys

os.system('clear')

print ('+===================================+')
print ('|         Country Info              |')
print ('+===================================+')
print ('| Author : Ravi                     |')
print ('| Github : github.com/Aghorii001    |')
print ('+===================================+')
print
from phone_iso3166.country import phone_country
phone_number=raw_input("Enter a phone number : ")
print ('Country              :'+ phone_country(phone_number))
