import genanki
import pandas as pd
import random
from html import escape

# Prompt for the deck name from user
deck_name = input("Enter the name of the Anki deck: ")

# Define a model for MCQs (radio and checkbox style)
mcq_model = genanki.Model(
  1607392319,
  'MCQ Model with Explanation',
  fields=[
    {'name': 'Question'},
    {'name': 'Options'},
    {'name': 'Explanation'},
  ],
  templates=[
    {
      'name': 'MCQ Card',
      'qfmt': '{{Question}}<br>{{Options}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Explanation}}',
    },
  ])

# Define the Anki deck with user-provided name
mlr_deck = genanki.Deck(
  2059400110,
  deck_name
)

def process_csv(file_path, is_multiple):
    df = pd.read_csv(file_path)
    grouped = df.groupby('Question')

    for question, group in grouped:
        # Shuffle the options
        options = list(group.to_dict('records'))
        random.shuffle(options)

        options_html = []
        explanation_html = []

        for row in options:
            input_type = 'checkbox' if is_multiple else 'radio'
            option_text = escape(str(row['Option']))
            explanation_text = escape(str(row['Explanation']))
            options_html.append(f"<input type='{input_type}'> {option_text}")
            correctness = '✔️' if row['IsCorrect'] else '❌'
            explanation_html.append(f"<b>{correctness} {option_text}</b>: {explanation_text}")

        options_block = '<br>'.join(options_html)
        explanation_block = '<br>'.join(explanation_html)

        note = genanki.Note(
            model=mcq_model,
            fields=[escape(question), options_block, explanation_block],
            guid=int.from_bytes(f'{question}{random.random()}'.encode('utf-8'), 'little') % (2**63)  # force unique ID for each card
        )
        mlr_deck.add_note(note)

# Read single-answer (radio button) questions from CSV
process_csv('single_answer_mcq.csv', is_multiple=False)

# Read multiple-answer (checkbox) questions from CSV
process_csv('multiple_answer_mcq.csv', is_multiple=True)

# Export the deck
genanki.Package(mlr_deck).write_to_file(f'{deck_name.replace(" ", "_").replace("::", "__")}_MCQ.apkg')
