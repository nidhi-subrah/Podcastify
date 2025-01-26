import spacy
import heapq

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

def summarize_text_spacy(input_text):
    # Process the input text using spaCy
    doc = nlp(input_text)
    
    # Create a frequency distribution of words (excluding stop words and punctuation)
    word_freq = {}
    for word in doc:
        if word.text.lower() not in nlp.Defaults.stop_words and word.is_alpha:
            if word.text.lower() not in word_freq:
                word_freq[word.text.lower()] = 1
            else:
                word_freq[word.text.lower()] += 1

    # Get the maximum frequency
    max_freq = max(word_freq.values())

    # Normalize the word frequencies (scale them)
    for word in word_freq:
        word_freq[word] = (word_freq[word] / max_freq)

    # Score each sentence based on the frequency of words it contains
    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_freq:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_freq[word.text.lower()]
                else:
                    sentence_scores[sent] += word_freq[word.text.lower()]

    # Select the top N sentences (based on the highest score)
    num_sentences = 5  # You can adjust this based on how detailed you want the summary to be
    summarized_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Combine the summarized sentences to form the summary
    summary = " ".join([str(sentence) for sentence in summarized_sentences])
    
    return summary


def generate_podcast_script(summary):
    podcast_script = f"Welcome to today's podcast! Let's dive into an exciting topic.\n\n{summary}\n\nHope you learned something new and interesting today!"
    return podcast_script


def main():
    # Read the input text from input.txt
    try:
        with open("input.txt", "r") as file:
            input_text = file.read()
    except FileNotFoundError:
        print("Error: 'input.txt' file not found. Please make sure the file exists in the current directory.")
        return
    
    # Summarize the input text using spaCy
    summary = summarize_text_spacy(input_text)
    
    # Generate the podcast script based on the summary
    podcast_script = generate_podcast_script(summary)
    
    # Print the podcast script
    print("\nPodcast Script:")
    print(podcast_script)


if __name__ == "__main__":
    main()
