#prompt question
answer = ""

while not answer == "yes":
    # This could be written as: 'while answer == "no":'
    # The difference would be how it treats other words, besides yes and no
    answer = input("May I have a piece of candy? ")

print ("Thank you.")


