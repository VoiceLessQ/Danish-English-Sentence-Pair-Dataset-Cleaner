import re

def clean_dataset(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        line = line.strip()
        # Use regular expressions to extract the sentences
        match = re.match(r'^\d+\t(.+)\t\d+\t(.+)$', line)
        if match:
            source_sentence = match.group(1)
            target_sentence = match.group(2)
            cleaned_lines.append(f"{source_sentence}\t{target_sentence}")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_lines))

def extract_words(line):
    match = re.match(r'^(.+?)\t(.+?)$', line)
    if match:
        danish_word = match.group(1)
        english_word = match.group(2)
        return danish_word, english_word
    else:
        return None

def write_words(words, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

input_file = 'Sentence pairs in Danish-English - 2023-05-09.txt'
output_file = 'Danish-English pairs.txt'

clean_dataset(input_file, output_file)

danish_words = []
english_words = []

with open(output_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        words = extract_words(line)
        if words:
            danish_words.append(words[0])
            english_words.append(words[1])

write_words(danish_words, 'danish.txt')
write_words(english_words, 'english.txt')
