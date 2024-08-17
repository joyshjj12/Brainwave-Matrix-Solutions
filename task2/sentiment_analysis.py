
import os
from transformers import pipeline
import matplotlib.pyplot as plt

# Initialize the sentiment analysis pipeline using BERT
sentiment_analyzer = pipeline('sentiment-analysis', model='bert-base-uncased')

# Define the folder containing the text files
folder_path = r"C:\Users\joysh\bwstask2"

# Initialize counters for sentiment categories
sentiment_counts = {'NEGATIVE': 0, 'POSITIVE': 0}

# Function to extract review comment from the file content
def extract_review(comment):
    return comment.split('Comment: ')[1].split('Date and Time:')[0].strip()

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as file:
            content = file.read()
            
            # Extract the review comment
            review_comment = extract_review(content)
            
            # Perform sentiment analysis
            result = sentiment_analyzer(review_comment)
            
            # Print result to check the labels
            print(f'Review: {review_comment}')
            print(f'Result: {result}')
            
            # Count the sentiment labels
            sentiment_label = result[0]['label']
            
            # Update sentiment counts based on the model output
            if sentiment_label in sentiment_counts:
                sentiment_counts[sentiment_label] += 1
            else:
                print(f"Unexpected sentiment label: {sentiment_label}")

# Plot the pie chart
labels = list(sentiment_counts.keys())
sizes = list(sentiment_counts.values())
colors = ['#ff9999', '#66b3ff']  # Different colors for negative and positive

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Sentiment Analysis Distribution')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.

# Save or show the pie chart
plt.savefig('sentiment_distribution_pie_chart2.png')  # Save as PNG file
plt.show()  # Uncomment this line to display the chart
