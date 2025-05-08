#info for work
highest_life = 0 
highest_country = ""
highest_year = ""

lowest_life = float("inf")  
lowest_country = ""
lowest_year = ""

years_to_use = []
year_of_interest = input("Enter the year of interest: ").strip()

# Variables for specific calculations
total_life_exp = 0
count = 0
year_highest_life = 0
year_highest_country = ""

year_lowest_life = float("inf")
year_lowest_country = ""

#OPEN THE FILE AND ITERATE
with open("life-expectancy.csv") as data_file:
    next(data_file)
    for data in data_file:
        separation = data.strip().split(",")

       # print(f"Raw value of life expectancy: '{separation[3]}'")

        
       # print(data)
       # data = data.strip()


#SPLIT EACH LINE INTO PARTS
        

        country = separation[0]
        shortened_country = separation[1]
        year = separation[2]
        life_expectancy = (separation[3])
       # life_exp = float(life_expectancy)

        if life_expectancy == "Life expectancy (years)":  
            continue  # Skip the header if it appears

        life_expectancy = float(life_expectancy)

       # years_to_use.appendear)

       # Check for highest life expectancy
        if life_expectancy > highest_life:
            highest_life = life_expectancy
            highest_country = country
            highest_year = year

         # Check for lowest life expectancy
        if life_expectancy < lowest_life:
            lowest_life = life_expectancy
            lowest_country = country
            lowest_year = year   


           # Check for year-specific data
        if year == year_of_interest:
            total_life_exp += life_expectancy
            count += 1

            # Find highest life expectancy for the year
            if life_expectancy > year_highest_life:
                year_highest_life = life_expectancy
                year_highest_country = country

            # Find lowest life expectancy for the year
            if life_expectancy < year_lowest_life:
                year_lowest_life = life_expectancy
                year_lowest_country = country  

# Calculate the average life expectancy for the user-input year
if count > 0:
    avg_life_exp = total_life_exp / count
else:
    avg_life_exp = 0

 # Print the results
print(f"The overall max life expectancy is: {highest_life} from {highest_country} in {highest_year}")
print(f"The overall min life expectancy is: {lowest_life} from {lowest_country} in {lowest_year}")   

# Print year-specific stats
if count > 0:
    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_life_exp:.2f}")
    print(f"The max life expectancy was in {year_highest_country} with {year_highest_life}")
    print(f"The min life expectancy was in {year_lowest_country} with {year_lowest_life}")
else:
    print(f"No data available for the year {year_of_interest}.")


#years_to_use_lists = list(years_to_use)       

#print(years_to_use_lists)
        
        #FIND TH LOWEST VALUE ANF HIGHEST VALUE FOR THE LIFE EXPENTANCY
         

#DISPLAY THE HIGHEST AND LOWEST