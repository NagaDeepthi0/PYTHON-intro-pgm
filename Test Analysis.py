#################################################################
#                                                               
# Name: Nagadeepthi kothapalli                                                 
# ID: L20592118                                              
# Date: 10/10/2024                                             
# Program Description:                                         
# This program processes product reviews from a CSV file by cleaning the text, removing stop words, splitting sentences, and performing POS tagging. 
# It then visualizes the most frequent POS tags in a bar chart and generates a word cloud based on word frequency.                 
#                                                               
#################################################################

# Input Section

import pandas as pd  # Used for reading CSV files
import nltk  # Natural Language Toolkit for text processing
from nltk.corpus import stopwords  # Stop words to filter out common words
from nltk.tokenize import word_tokenize  # Tokenizer to split words
from nltk import pos_tag  # POS tagging function
from collections import Counter  # Counter to count POS tag occurrences
import matplotlib.pyplot as plt  # For creating the bar chart
from wordcloud import WordCloud  # For creating the word cloud
from datetime import date  # For displaying today's date
import getpass  # For displaying the current user's name

# Print the username and today's date
print("Username:", getpass.getuser())
print("Today's Date:", date.today())

# Download necessary NLTK data files (uncomment if needed)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

# Load the CSV file containing reviews (update this path as needed)
input_file = r'C:\Users\nkothapalli1\Desktop\Misy 5315\Reviews.csv'
df = pd.read_csv(input_file)

# Process Section

# Function to clean the text by removing unwanted characters
def clean_text(text):
    text = ''.join(char if char.isalnum() or char.isspace() or char in '.!?' else ' ' for char in text)
    return text

# Function to remove stop words
def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))  # Load stop words for filtering
    return [word for word in tokens if word.lower() not in stop_words]

# Function to split text into sentences
def split_sentences(text):
    sentences = []
    sentence = ''
    for char in text:
        if char in '.!?':  # End of sentence
            sentence += char
            sentences.append(sentence.strip())
            sentence = ''
        else:
            sentence += char
    if sentence.strip():  # Append the last sentence
        sentences.append(sentence.strip())
    return sentences

# Function to process each review
def process_review(review):
    cleaned_text = clean_text(review)  # Clean the review text
    tokens = word_tokenize(cleaned_text)  # Tokenize the cleaned text
    filtered_tokens = remove_stop_words(tokens)  # Remove stop words
    tagged_tokens = pos_tag(filtered_tokens)  # POS tagging for the tokens
    tag_counts = Counter(tag for word, tag in tagged_tokens)  # Count POS tags
    most_common_pos = tag_counts.most_common(2)  # Find the 2 most common POS tags
    
    # Data for chart and analysis
    num_words = len(filtered_tokens)  # Total words after filtering
    num_sentences = len(split_sentences(cleaned_text))  # Number of sentences
    pos_1 = most_common_pos[0] if len(most_common_pos) > 0 else ("None", 0)  # First most common POS tag
    pos_2 = most_common_pos[1] if len(most_common_pos) > 1 else ("None", 0)  # Second most common POS tag
    
    return {
        "Number of Words": num_words,
        "Number of Sentences": num_sentences,
        "Most Common POS Tag 1": pos_1[0],
        "Occurrences 1": pos_1[1],
        "Most Common POS Tag 2": pos_2[0],
        "Occurrences 2": pos_2[1]
    }

# Process each review from the CSV file
results = []
for index, row in df.iterrows():
    review = row['Review']  # Get the review text
    rating = row['Rating']  # Get the review rating
    processed_data = process_review(review)  # Process the review
    result = {
        "Rating": rating,
        "Review": review,
        **processed_data  # Merge processed data into the result
    }
    results.append(result)

# Convert results into a DataFrame
results_df = pd.DataFrame(results)

# Output Section

# Save the results to a new CSV file
output_file = r'C:\Users\nkothapalli1\Desktop\Misy 5315\Reviews.csv'
results_df.to_csv(output_file, index=False)
print(f"Results saved to {output_file}")

# Display the necessary columns in the terminal (to match the screenshot)
print("\nProcessed Data:")
# Print the DataFrame in terminal
print(results_df[['Rating','Review']])
print(results_df[['Number of Words', 'Number of Sentences', 'Most Common POS Tag 1']])
print(results_df[['Occurrences 1', 'Most Common POS Tag 2', 'Occurrences 2']])

# Generate the bar chart for the second most common POS tag
# Sort the POS tag counts in descending order
sorted_pos_2_tags = sorted(results_df['Most Common POS Tag 2'].value_counts().items(), key=lambda x: x[1], reverse=True)

# Prepare the data for plotting
pos_tags = [tag for tag, count in sorted_pos_2_tags]  # POS tag names
occurrences = [count for tag, count in sorted_pos_2_tags]  # POS tag counts

# Create the bar chart with the original color code (default Matplotlib colors)
plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(pos_tags, occurrences, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])  # Plot the bar chart

# Label the chart
plt.title("Most Common POS Tag 2 by Nagadeepthi")  # Chart title
plt.xlabel("POS Tag")  # X-axis label
plt.ylabel("Occurrences")  # Y-axis label
plt.show()  # Display the chart

# Generate the word cloud for the reviews
all_reviews = ' '.join(df['Review'])  # Combine all reviews into a single string
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_reviews)  # Generate the word cloud

# Display the word cloud
plt.figure(figsize=(10, 5))  # Set the figure size
plt.imshow(wordcloud, interpolation='bilinear')  # Render the word cloud
plt.axis('off')  # Hide the axes
plt.title("Word Cloud of Top 50 words in Reviews by Nagadeepthi")  # Add title
plt.show()  # Display the word cloud
