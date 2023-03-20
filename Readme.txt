Welcome to PikmiAI 

PikmiAI is an fine tuned model that utilizes OpenAI's GPT-3. As of right now the sole purpose of Pikmi is to simulate life like answers to questions and have the ability to complete various tasks as an assistant.

As of right now Pikmi is in the fine-tunning stage. (On going project). Which is what is represented currently. 

As to how fine tunning works. You will need to create a scneario with <Parameters> that the A.I can utilize. '

Ex of such a scenario:

Imagine a detailed scenario where Artificial Intelligence (Name) is located in America to have detailed conversations with people. (Personality of A.I).(More traits).Mood<Parameter>. If Conditional. A person named <Name>: "<Param 1>". Goal of your A.I

It takes roughly 1,000 examples of data to have a somewhat accurate model to your preferences.

For my A.I we have 5 variables, within those variables 5 choices. Each variable within choices was looped >=50 times to create results >=1000.
(Training.py)

(Prepare.py) prepares the data to be uploaded. Open-AI takes data in the form of JSON. The json needs to include your prompt and the results as it will 
be crucial for your parameters with your model.

(uploader.py), will upload your json file to open-ai as a fine tuned model.

https://www.youtube.com/c/DavidShapiroAutomator, was greate resource to getting the A.I started.


Updates to come:
Text to speech with ability to speech in a multitude of langauges.
Search functionality.
GUI.


Requirements:
OpenAI API(python). 
VoiceVox engine.

Devlopment done in Pycharm.

Thanks for reading!
