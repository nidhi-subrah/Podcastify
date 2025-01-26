from transformers import BartForConditionalGeneration, BartTokenizer

# Load the pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

# Function to summarize text
def summarize_text(input_text):
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
    
    # Generate the summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=1500, early_stopping=True)
    
    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Function to create a podcast-style script from a summary
def generate_podcast_script(summary):
    # Make the podcast script dynamic and engaging, based on the summary
    podcast_script = f"Welcome to today's podcast! Let's dive into an exciting topic.\n\n{summary}\n\nHope you learned something new and exciting today!"
    return podcast_script

# Main function to run the program
def main():
    # Read the input text from input.txt
    try:
        with open("input.txt", "r") as file:
            input_text = file.read()
    except FileNotFoundError:
        print("Error: 'input.txt' file not found. Please make sure the file exists in the current directory.")
        return
    
    # Summarize the input text
    summary = summarize_text(input_text)
    
    # Generate the podcast script based on the summary
    podcast_script = generate_podcast_script(summary)
    
    # Print the podcast script
    print("\nPodcast Script:")
    print(podcast_script)

# Run the program
if __name__ == "__main__":
    main()
