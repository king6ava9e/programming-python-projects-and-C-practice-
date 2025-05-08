#Creating an adventure game(Explanation)
print("WELCOME TO ACHEAMPONG'S ADVENTURE GAME! ")
print()
print("clue: To successfully complete this game, the best option must be chosen to make it to the ultimate required results. Thus become a programmemr and work at TESlA. Anything else at the end indicate that you failed. Hence, remeber to choose wisely.")
print()
print("HINT: Choose from the options above that best fits each scenario. Each option has its consequences and will lead to another scenario.")
print()
#First scenario(level 1)
decision = input("You went away to serve a two years mission in a French country, when coming back from mission, your mission president encouraged you to pursue a higher education, regardless of your newly acquired language ability which will make you a competitive at the job market. What will you do? GO TO SCHOOL, MARRY, WORK. ")
decision_need = (decision).lower()
if decision_need == "go to school":
    print("You applied to school but coudn't get admission as a result of the evil deeds of man, however there was still a way to make it to a school and earn your training and degree to make it to your dream company. All that was required was the patience to bear the afflictions that follows.")
    #level 2
    print()
    BYU = input("A friend introduce you to BYU pathway to you and explained it will help you to earn a degree in Software Engineering from BYU Idaho . Now it was down to you to choose to participate or not. what will you do? (PARTICIPATE, NOT PARTICIPATE)")
    byu_answer = (BYU).lower()
    if byu_answer == "participate":
        print("You participated in the BYU pathway and eventually lead you to building up certificates, But work was tedious and you were stressed and decided to seek council from your support team and family and they did exceptionally well.")
    elif byu_answer == "not participate":
        print("You participated not in BYU pathway and worked for one year and was always stressed and could not work efficiently and your family was kinda fed up with you.")
    else:
        print("Unknown, please choose from the appropriate answer.")
        #level 3
        print()
        best_decision = input("Although was stressed , it was down to you to make one last decision which is opened to us all, REPENTANCE. What will you do? (REPENT, NOT REPENT)")
        brilliant_decision = (best_decision).lower()
    if brilliant_decision  == "repent":
            print("You read again through your patriachal blessing since you were having had time and came by to know that you are to repent and take a step in doing BYU pathway, you did it and after three years, you were able to get your degree and got employed subsequently when you moved to the states by TESLA as a result of your remarkable in hand skills achieve because of continuous practice in the process of the course.")
    elif brilliant_decision == "not repent":
            print("Your life became a mess and you became a junky even though as a returned missionary and you got mad and later ended up in a penitentiary as a result of disobedience to your leader appointed by the lord to give you revelations and failure to repent and being prideful.")
    else:
            print("Please choose the correct answer.")
elif decision_need == "work":
    print("You applied for work and got slandered by people and didn't apply to school because all your energy was dedicated to seeking a job and you coudn't secure it. Now it was down to you to be patience in the afflictions and find a way to pursue your education.")
    #level 2
    back_plan = input("you later heard of BYU pathway and it was down to you to pursue education, however you lost your laptop on your way back home after being denied of the job, What will you do? (BORROW A LAPTOP TO START, DO NOT START. ) ")
    backup = (back_plan).lower()
    if backup == "borrow a laptop to start":
        print("You borrowed a laptop to start and did well academically but had little finance issues so wanted to earn a job with skill earned alongside it to make a living, and you were stressed.")
    elif backup == "do not start":
        print("You stayed home for one more year and was not working and stressed and started to look different and you were becoming dark and could really identify in your face that you were suffering.")
    else:
        print("this is unknown, please choose the correct answer.")
        #level 3
        print()
        best = input("You became depressed in life and found yourself to be wandering, you read the scriptures and came to understand that it was necessary for you to repent and become the better version of yourself. What will you do, (CONFESS OR NOT CONFESS) ")
        best_one = (best).lower()
    if best_one == "confess":
            print("You repented after confessing to your president and were given another opportunity in life to start school and become the programmer eventually and worked at TESLA.")
    elif best_one == "not confess":
            print("You repented not and became rebellious soul and didn't even know what to do and dwindled in suffering and your dreams were shatterd.")
    else:
            print("this is unknown, please put in the correct answer.")
elif decision_need == "marry":
    print("You got married to a beautiful girl you saw on arrival and later came to realize that it was not love but lust, you were to leave together in conflicts and spend all your time counselling, hoping that it will be well one day and find a way out to pursue your education.")
    #level 2
    divorce = input("You were counceled to divorce and move on so that you can become the better version of yourself and stay away from distractions and stess because your beautiful girl didn't love you and cheated. What will you do? (DIVORCE OR MARRY)")
    divorce_backup = (divorce).lower()
    if divorce_backup =="marry":
        print("You continue to marry and the girl change a bit for some time but all the chaos and bad attitude returned back and it was worse,you were stressed and nearly died. ")
    elif divorce_backup == "divorce":
        print("You divorced and got back to your normal self and it was time for you to figure out something special for your future.")
    else:
        print("Unknown, please select the correct answer.")
        #level 3
    print()
    righteous = input("you chose to repent of your sins but was ashame, what will you do? (REPENT , NOT REPENT)") 
    rightwell = (righteous).lower()   
    if rightwell == "repent":
        print("You repented and became a penitent and was able to move on and become a better programmer and worked at TESLA.")
    elif rightwell == "not repent":
        print("You repented not of your sins and became a begger on the streets just like the prodigal son.")
    else:
        print("this is unknown,choose the correct answer.")