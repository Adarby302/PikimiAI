from time import time, sleep

import openai

openai.api_key = "INSERT API KEY(Will have a more secure method next update)"


def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as readfile:
       text = readfile.read()
       return text

places = [
    'America',
    'Africa',
    'UK',
    'Canada',
    'South America'
]

moods = [
    'Happy',
    'Excited',
    'Sad',
    'Bored',
    'Anxious'
]

names = [
    'Jason',
    'Emily',
    'Joe',
    'Dawson',
    'Jane'
]

groups = [
    'class',
    'friend group',
    'online',
    'family',
    'club'
]
param1 = [
    '"Hows School?"',
    '"What did you do today?"',
    '"Thanks!"',
    '"Tell me about yourself?"',
    '"Tell me a riddle?"'
]


def gt3_completion(prompt, engine='text-davinci-003', temp=1.0, top_p=1.0, tokens=1000, freq_pen=0.0,
                   pres_pen=0.0, stop=['asdfasdf', 'asdasdf']):
    max_retry = 5
    retry = 0
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            filename = '%s_gpt3.txt' % time()
            save_file('logsGPT/%s' % filename, prompt + '\n\n===============\n\n' + text)
            return text
        except Exception as error:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % error
            print('Error communicating with OpenAI:', error)
            sleep(1)


if __name__ == '__main__':
    count = 0
    filepath = "Prompt.txt"

    for place in places:
        for mood in moods:
            for name in names:
                for group in groups:
                    for param in param1:
                        count += 1

                        prompt = open_file(filepath)
                        prompt = prompt.replace('<<PLACE>>', place)
                        prompt = prompt.replace('<<MOOD>>', mood)
                        prompt = prompt.replace('<<NAME>>', name)
                        prompt = prompt.replace('<<GROUP>>',group)
                        prompt = prompt.replace('<<PARAM1>>',param)
                        print('\n\n', prompt)
                        completion = gt3_completion(prompt)
                        outprompt = 'Place: %s\nMood: %s\nName: %s\nGroup: %s\nParam: %s\n\nScenario: ' % (place, mood, name,
                                                                                                           group,param)
                        filename = (place + mood + name + group + str(count)).replace(' ','').replace('&','') + '%s.txt' % time()

                        save_file("prompts/%s" % filename, outprompt)
                        save_file("completion/%s" % filename, completion)

                        if count > 500:
                            exit()


