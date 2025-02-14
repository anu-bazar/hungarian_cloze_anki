# hungarian_cloze_anki
Hungarian Cloze Anki Deck generator 

The script processes Hungarian-English sentence pairs and a frequency list to generate Anki-compatible CSV files. This is a modified version of the article found here: https://sookocheff.com/post/language/bulk-generating-cloze-deletions-for-learning-a-language-with-anki/

### Features

Converts a TSV file of Hungarian-English sentence pairs into separate CSV files.

Cleans a Hungarian word frequency list by removing additional columns.

Identifies the least frequent word in each Hungarian sentence for cloze deletion.

Generates an Anki-compatible CSV file with cloze deletions.

### Prerequisites

Python 3.x

Required Libraries: csv, random, string

The latest Anki install

### File Descriptions

tatoeba_hun_eng_pairs.tsv: Input file containing Hungarian-English sentence pairs.

target_sentences.csv: Output file containing Hungarian sentences.

native_sentences.csv: Output file containing English translations.

top_5000_hungarian.txt: Input file containing Hungarian words ranked by frequency.

top_5000_hungarian_cleaned.txt: Processed frequency list with only the Hungarian words.

anki_flashcards.csv: Final output file formatted for Anki.

### Code Execution

'textprocessing.py': Convert TSV to CSV

This script extracts Hungarian-English sentence pairs from a TSV file and saves them as separate CSV files.
Run this once you have the two files required: 
- A top 5000 frequent words list
- A bunch of sentences from Tatoeba

'cloze_creation.py': Clean/create the Frequency List

This script removes additional column of numbers, retaining only the first column (Hungarian words).

This script identifies the least frequent word in each Hungarian sentence and replaces it with an underscore (_).

### Output Format

The final anki_flashcards.csv file contains two columns:

The cloze deletion sentence in Hungarian, followed by its English translation.

The original Hungarian sentence for reference.

### Usage

Ensure all required files (tatoeba_hun_eng_pairs.tsv, top_5000_hungarian.txt) are available.

Run the scripts sequentially.

Import anki_flashcards.csv into Anki as a CSV file with the first column mapped to "Front" and the second column to "Back".

Anki FAQ: https://forums.ankiweb.net/t/how-to-import-from-csv-or-database-into-existing-deck/43966

#### License

This project is based on open-source data and is intended for educational purposes. Feel free to use it!

#### Acknowledgments

Largely inspired by sookocheff.com and this would not be possible without the amazing people at the Tatoeba project!

#### MISC

General Keywords: Hungarian language learning Anki flashcards Cloze deletion flashcards Hungarian vocabulary practice Language learning automation Anki deck generator Hungarian sentence pairs Tatoeba dataset processing Frequency-based word removal Automated flashcard creation Technical Python script for Anki CSV processing in Python Bulk sentence processing Text parsing with Python Hungarian-English translation dataset Frequency analysis for language learning Natural language processing (NLP) for flashcards Cloze deletion automation Sentence tokenization in Python Cleaning text datasets Anki-Specific Anki language learning deck Anki automation with Python Spaced repetition system (SRS) Anki import CSV Creating custom Anki flashcards Generating Anki decks programmatically Anki cloze format Best Anki decks for Hungarian Learning Hungarian with Anki 