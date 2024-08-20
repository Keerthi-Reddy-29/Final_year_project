import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the scraped reviews from the CSV file into a DataFrame
df = pd.read_csv('amazon_reviews_maus.csv')

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Determine sentiment polarity: > 0 is positive, < 0 is negative, = 0 is neutral
    if analysis.sentiment.polarity > 0:
        return 'positive' 
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis to each review
df['sentiment'] = df['text'].apply(analyze_sentiment)

# Visualize the sentiment distribution
sentiment_counts = df['sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Sentiment Analysis of Amazon Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.show()

# Print the sentiment distribution
print(sentiment_counts)
