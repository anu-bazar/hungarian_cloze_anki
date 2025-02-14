import csv
import random
import string

def load_frequency_list(filepath):
    """Load the frequency list into a set for quick lookups."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return {line.strip().lower() for line in f}

def find_cloze(sentence, frequency_list):
    """Find the least frequent word in the sentence for cloze deletion."""
    # Remove punctuation
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    sentence = sentence.translate(translator)
    
    min_word = None
    valid_words = []
    
    for word in sentence.split():
        if word.istitle() or len(word) <= 2:
            continue  # Skip proper nouns and very short words
        valid_words.append(word)
        
        if word.lower() not in frequency_list:
            min_word = word  # Choose a rare word if not in the list
    
    return min_word if min_word else random.choice(valid_words) if valid_words else None

def generate_anki_csv(target_file, native_file, freq_file, output_file):
    """Generate an Anki-compatible CSV file with cloze deletion flashcards."""
    frequency_list = load_frequency_list(freq_file)
    
    with open(target_file, 'r', encoding='utf-8') as target_f, \
         open(native_file, 'r', encoding='utf-8') as native_f, \
         open(output_file, 'w', encoding='utf-8', newline='') as output_f:
        
        target_reader = csv.reader(target_f)
        native_reader = csv.reader(native_f)
        csv_writer = csv.writer(output_f)
        
        for target_row, native_row in zip(target_reader, native_reader):
            if not target_row or not native_row:
                continue
            
            hungarian_sentence = target_row[0]
            english_sentence = native_row[0]
            
            cloze_word = find_cloze(hungarian_sentence, frequency_list)
            if not cloze_word:
                continue  # Skip if no valid word found
            
            cloze_sentence = hungarian_sentence.replace(cloze_word, '_', 1)
            csv_writer.writerow([f"{cloze_sentence} - {english_sentence}", hungarian_sentence])

generate_anki_csv('target_sentences.csv', 'native_sentences.csv', 'top_5000_hungarian_cleaned.txt', 'anki_flashcards.csv')