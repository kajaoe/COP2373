# Import regular expressions.
import re

def extract_sentences(paragraph):
    # Modified regular expression to support capital letters or numbers.
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences

# Define main to gather user input.
def main():
    print('-' * 50)
    print("Sentence Counter Program!")
    print('Enter or paste your paragraph below! \n')
    print('Then please press Enter twice to finish.')
    print("-" * 50)

    # Read input from the user
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    paragraph = "\n".join(lines)

    # Check if the user did not enter anything.
    if not paragraph.strip():
        print("\nNo text entered.")
        return

    # Call the extract_sentences function.
    sentence_list = extract_sentences(paragraph)

    # Display the user's results.
    print('-' * 50)
    print('Extracted Sentences...')
    for index, sentence in enumerate(sentence_list, start=1):
        print(f"Sentence {index}: {sentence.strip()}")
    print('-' * 50)
    print(f"Total sentence count: {len(sentence_list)}")

# Run main to execute the script.
if __name__ == "__main__":
    main()