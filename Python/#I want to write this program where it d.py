#I want to write this program where it does somehing fun
#This program is gonna help you make a better career choice.

#part of this program is going to be a function which generates list of random 
#jobs or career paths that you can choose from..

#Another function is going to ask you couple of preferences and then make a decison or choose 
#the best carrer path for you

#this is the main function.
def main ():
    """THis is going to print out the best carrer path for you base on the prefrencees"""
    #I will be back to put in the necessary data



#Creating List of subjects
def create_list_of_subjects():
    """"This is going to help the user make some choices base on likes and dislikes in subjects at high school"""
    things_liked = ["Mathematics","English","Science","Government","Information Communication and Technology","Documentary","History"]
    things_disliked = ["Learning","Talking","Teaching","Reading","Travelling","Memorizing"]
    career_match = {
        ("Mathematic", "Learning") : "Statician",
        ("English", "Travelling") : "Pilot",
        ("Science", "Reading") : "Doctor",
        ("Government", "Reading") : "Lawyer",
        ("Information Communication and Technology","Learning" ) : "Software Engineering",
        ("History", "Talking") : "Historian",
 }

                   
    return things_disliked, things_liked



#Creating List of jobs
def create_list_of_careers():
    """This is going to help us create list of careere paths """    
    carrers = ["Software Engineering","Doctor","Teacher","Staticican","Lawyer","Historian","Journalist","Pilot"]
    return carrers

#Creating an input statements to ask questions for the user preferences
def create_input_statement():

    """THis is going to ask ther user for some input statements and then use the answers to make the decision"""
    subjects_liked= input("Which subject do you like best in School among those in the brackets? (eg; Maths, English, Science, Government, Information Technology, Documentary, History)").lower()
    activities_liked =input("Which activity do you enjoy doing ? (Learning, Talking , Teaching, Reading, Travelling, Memoring) ").lower()
    return subjects_liked, activities_liked
      
#creating If statements to make a decision
def create_if_statements():
    """This is going to help us to create series of if statements to make a decison of our carrer"""
    subjects = create_list_of_subjects
    subects_list = create_list_of_subjects[0]
    activities_liked = create_list_of_subjects[1]
    job = create_list_of_careers
    user_input = create_input_statement
    question1 = create_input_statement[0]
    question2 = create_input_statement[1]
    return create_if_statements

#writing the if statements
    if question1 in subects_list:
    

