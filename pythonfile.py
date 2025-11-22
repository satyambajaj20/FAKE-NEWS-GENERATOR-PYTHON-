# import the random module 
import random

#create subjects 
subjects = ["steve jobs", "robert doney jr", "dehradun" , "elon musk", "jeff bezos" , "a group of ginue pigs"]
actions = ["invented", "discovered", "built", "created", "designed", "developed"]
places_or_things = ["a time machine", "a new app", "a flying car", "a cure for cancer", "a new planet", "a robot that can think"]

#headline generation loop 

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" NEWS OF THE DAY : {subject} {action} {place_or_thing}!"

    print("\n" + headline)

    users_choice = input("Do you want to generate another headline? (yes/no): ") .strip()
    if users_choice.lower() != "yes":
        print("Thank you for using the Fake News Generator!")
        break