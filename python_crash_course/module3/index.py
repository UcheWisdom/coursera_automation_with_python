#x = 0
#while x < 5:
#print("not there yet " + str(x))
#   x = x + 1
#print("x=" + str(x)) 

#def attempts(n):
 #   x = 1
  #  while x < n:
   #     print("Attepts " + str(x))
    #    x += 1
    #print("Done")
#attempts(5)

#x = 1
#sum = 0
#while x < 10:
#    sum = sum + x
#    x = x + 1

#product = 1
#while x < 10:
#    product = product * x
#    x = x + 1

#print( product)
#Ouput 45 1




#def multiplication_table(number):
    # Initialize the appropriate variable
 #   multiplier = 1


    # Complete the while loop condition.
 #   while multiplier <= number:
 #       result = number * multiplier 
  #      if  result > 25:
  #          # Enter the action to take if the result > 25
  #          break
  #      print(str(number) + "x" + str(multiplier) + "=" + str(result))
  #      
  #      # Increment the appropriate variable
  #       multiplier += 1

#input = "Four score and seven years ago"
#for c in input:
#    if c in "aeiouAEIOU":
#        print(c)



#def is_power_of(number, base):
# Base case: when number is smaller than base.
#    if number < base:
#        # If number is equal to 1, it's a power (base**0).
#        return __

#    # Recursive case: keep dividing number by base.
#    return is_power_of(__, ___)


#print(is_power_of(8,2))     # Should be True
#print(is_power_of(64,4))    # Should be True
#print(is_power_of(70,10))   # Should be False





#def count_users(group):
#  count = 0
#  for member in get_members(group):
#    count += 1
#   if is_group(member):
#      count += count_users(member)
#  return count


#print(count_users("sales")) # Should be 3
#print(count_users("engineering")) # Should be 8
#print(count_users("everyone")) # Should be 18






num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

for sum in range(5):
    sum += sum
    print(sum)