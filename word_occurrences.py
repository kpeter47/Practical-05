"""
Program: word_occurrences.py
Author: Peter 
Date: October 15, 2023
Time Estimate: 30 minutes

Description:
This program counts the occurrences of words in a user-provided string and displays the word counts in sorted order, aligned with a consistent width.

Usage:
1. Run the program.
2. Enter a string when prompted.
3. The program will display the word counts in sorted order with aligned output.
"""

def count_word_occurrences(text):
    # Split the text into words
    words = text.split()

    # Create a dictionary to store word counts
    word_count = {}

    # Count occurrences of each word
    for word in words:
        word = word.lower()  # Convert to lowercase to make counts case-insensitive
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Find the maximum word length for alignment
    max_word_length = max(len(word) for word in word_count)

    # Sort the word counts and print the results with aligned output
    sorted_word_count = sorted(word_count.items())
    for word, count in sorted_word_count:
        print(f"{word:>{max_word_length}} : {count}")

if __name__ == "__main__":
    user_text = input("Enter a string: ")
    count_word_occurrences(user_text)
