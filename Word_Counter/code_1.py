def count_words(file_path):
    try:
        # Read the content of the text file
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Split the content into words
        words = content.split()
        
        # Count the number of words
        word_count = len(words)
        
        return word_count
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ")
    
    word_count = count_words(file_path)
    
    if word_count is not None:
        print(f"The file contains {word_count} words.")
