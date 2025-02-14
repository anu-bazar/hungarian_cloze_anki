import csv
""" This is a rendition of https://sookocheff.com/post/language/bulk-generating-cloze-deletions-for-learning-a-language-with-anki/
and his tutorial on creating Cloze pairs for Hungarian"""
#Turn TSV to CSV
with open("tatoeba_hun_eng_pairs.tsv", encoding="utf-8") as tsv_file, \
     open("target_sentences.csv", "w", encoding="utf-8", newline='') as target_file, \
     open("native_sentences.csv", "w", encoding="utf-8", newline='') as native_file:
    #Give target and native files for pairs (HUN, ENG)
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    target_writer = csv.writer(target_file)
    native_writer = csv.writer(native_file)
    
    for row in read_tsv:
        if len(row) >= 4:  # Columns (NUMBER/HUN/NUMBER/ENG)
            target_writer.writerow([row[1]])  # Hungarian sentence
            native_writer.writerow([row[3]])  # English sentence

#### Delete the second column
input_file = "top_5000_hungarian.txt"
output_file = "top_5000_hungarian_cleaned.txt"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        word = line.split()[0]  # Take only the first column (word)
        outfile.write(word + "\n")

print(f"File saved as {output_file}")
