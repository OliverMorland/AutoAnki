#! python3
import genanki, os, openpyxl, random, logging

#Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

#Get Spreadsheet with new vocab
logging.debug('current dir is: ' + os.getcwd())
os.chdir(r'C:\Users\omorland\PythonProjects\AutoAnki\autoAnkiFiles')
logging.debug('changed current dir to: ' + os.getcwd())
workbook = openpyxl.load_workbook('AnkiVocab.xlsx')
sheet = workbook['Sheet1']

#Create Anki Deck
deckId = random.randrange(1 << 30, 1 << 31)
logging.debug('Deck Id is ' + str(deckId))
deck = genanki.Deck(
    deckId,
    'New Auto Generated Vocab')

#Create Anki Model
modelId = random.randrange(1 << 30, 1 << 31)
logging.debug('Model Id is ' + str(modelId))
model = genanki.Model(
    modelId,
    'Vocab Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'MyMedia'},
        ],
    templates=[
        {
            'name':'Card 1',
            'qfmt':'{{Question}}<br>{{MyMedia}}',
            'afmt':'{{FrontSide}}<hr id="answer">{{Answer}}'
        },
    ])
        

#Add note to deck for each row in spreadsheet
for i in range(2,12):
    korean = sheet['A'+str(i)].value
    sound = '[sound:ATone.mp3]'
    english = sheet['B'+str(i)].value
    note = genanki.Note(
        model=model,
        fields=[korean, english, sound])
    deck.add_note(note)

#Save media to package
package = genanki.Package(deck)
package.media_files = ['ATone.mp3']

#Save .akpg file
package.write_to_file('autoGeneratedDeck.apkg')
logging.debug('Created new deck')



