import phonenumbers

from phonenumbers import timezone, geocoder, carrier 


phoneNumber = phonenumbers.parse(input("Phone ?"))

timeZone = timezone.time_zones_for_number(phoneNumber)

Carrier = carrier.name_for_number(phoneNumber, 'en')

Region = geocoder.description_fro_number(phoneNumber, 'en')

print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)

print("coded by natridev\n      github.com/natrixdev")
