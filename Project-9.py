# Pool of questions 
question={"The first country in the world to use postcards was the United States of America. ":"Yes",
        "Black is the most commonly used colour in all national flags around the world.":"No",
        " Mice have more bones than humans.":"Yes",
        "The first product with a bar code was chewing gum.":"Yes",
        "Quidditch is the most popular sport among witches and wizards in “Harry Potter”.":"Yes",
        "The star is the most common symbol used in all national flags around the world.":"Yes",
        "The capital of Australia is Sydney.":"No",
        "The World War II began in 1939 when Germany invaded Poland.":"Yes",
        "The FIFA World Cup 2022 will take place in Iran.":"No",
        "AB- is the rarest type of blood in humans.":"Yes",
        "A cube has 16 straight edges in total.":"No"}
import random

questionlist=[]

while(len(questionlist)!=5):                            # List of 5 questions
    i=random.choice(list(question.keys()))              # Choose Random question from question pool and make a list of it
    if  i not in questionlist :
        questionlist.append(i)                          # Make a list of random qustions 
        
score=0
for i in questionlist:       
    print("\n"+i)
    a=input("\nEnter Yes or No: ")
    if(a==question[i]):
        print("\nRight answer! +5 points")
        score+=5
    else:
        print("\nWrong answer!")
print("\nTotal Score is :",score)
