#open file
with open("books.txt") as books:
    for seen in books:
        
        strip_seen = seen.strip()
        
        print(strip_seen)

#open the file and read through it

#strip off the whitespaces

#print the new file