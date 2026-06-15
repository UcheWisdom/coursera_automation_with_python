
# def convert_seconds(second):
#    hours = second // 3600
 #   minutes = (second - hours * 3600 ) // 60
  #  remaining_seconds = (second - hours * 3600 - minutes * 60)
   # return hours, minutes, remaining_seconds

#hours, minutes, remaining_seconds = convert_seconds(5000)
#print(hours, minutes, remaining_seconds)


#def lucky_number(name):
#    number = len(name) * 9
 #   print("Hello " + name + ". Your lucky number is " + str(number))

#lucky_number("wisdom")

#def caluclated(d):
 #   q= 3.14
  #  z = q * (d**2)
   # print(z)

#caluclated(5)

#def circle_area(radius):
 #   pi=3.14
  #  area = pi * (radius ** 2)
   # print(area)

#circle_area(5) 

#def hint_username(username):
 #   if len(username) <3:
  #      print("Invalid username. Must be at least 3 characters long")
   # else:
    #    print("Valid username")

#hint_username("hey")

#def is_even(number):
 #   if number % 2 == 0:
  #      return True
   # return False
#This code has no output

#is_even(5)



def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
         print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")

hint_username("Wisdompreciousdelight")

number = 10
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)