def count_words(text):
    # Split the text into words and return the word count
    words = text.split()
    return len(words)

def main():
    # Prompt the user for input
    user_input = input("Enter a sentence or paragraph: ")
    
    # Error handling: check if the input is empty
    if not user_input.strip():
        print("Error: No input provided. Please enter some text.")
    else:
        # Call the count_words function and display the result
        word_count = count_words(user_input)
        print(f"Word count: {word_count}")

# Run the main function
if __name__ == "__main__":
    main()