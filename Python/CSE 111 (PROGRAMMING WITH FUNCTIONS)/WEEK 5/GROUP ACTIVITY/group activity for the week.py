import csv

def read_dictionary(filename):

    """Read the contents of a CSV file into a
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
  Return: a dictionary that contains
      the contents of the CSV file.
  """
    with open ("students.csv", mode="r") as filename:
     
     reader = csv.reader(filename)
    next(reader)
    headers = ["I_name", "name"]
    dict_reader = csv.DictReader(filename,fieldnames=headers)

    
#creates a dictionary where I_name is the key and the name as the pair value
    students_dictionary = {row["I_name"]: row["name"] for row in dict_reader}
    return students_dictionary
    
def main ():
   i_number = read_dictionary
   user = input("What is the I number")
   if user != i_number:
      print("no")

main()

      
   
   
      
   
   



   

  
  

  
  

 



    
       
