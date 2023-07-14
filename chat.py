import openai
import os
'''
memorization of a person? seperate json files? essentially next time figure out file strucutre? 
key method where the name is the key.
or seperate json files as the name.

Post request 
Setup -> sets up the name, mood, and place of pikmi for prompt 
-> calls json adding 

->chat will call upon existing json.

after setup*




'''
#global variables

openai.api_key = "open ai key"
conversation = []



def setup_prompt():
    '''
    Insert where prompt completion for the start of a.i lives.
    Pikmi is trained to have a:
    Location
    mood
    name
    group
    and param

    Shorten this to:
    location
    mood
    name
    '''
    print("Enter in the prompt details")
    locationVar = input("What location are you in? ")
    #confine this to a drop down in the future
    moodVar = input("mood you would like pimki? ")
    nameVar = input("What is your name ")



def jsonadding(locationVar, moodVar, nameVar):
    global conversation
    #insert filepath here
    filepath = 'conversation.json'

