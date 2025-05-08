numbers =[]

#creating the loops
while True:
     number_created = (input("Enter a list of numbers, type 0 when finished"))
     if number_created == "0":
          break
     else:
          number_used = int(number_created)
          numbers.append(number_used)


    

          #doing the computations
total_numbers = ((sum(numbers)))
average_number = total_numbers / len(numbers)
average_correct = ((average_number))
maximum_number = ((max(numbers)))
print()
#displaying
print(f"The sum is : {total_numbers}")
print(f"The average is : {average_number}")
print(f"The largest number is : {maximum_number}")

#sorting the numbers
if numbers:
     numbers.sort()
     print(f"{numbers}")
     

    
     
