### Sentiment Analysis of Amazon Reviews for "Maus" Graphic Novel

This project performs sentiment analysis on Amazon reviews for the graphic novel "Maus" by Art Spiegelman. It scrapes the reviews from Amazon, analyzes the sentiment of each review using TextBlob, and visualizes the sentiment distribution.

#### Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sentiment Analysis Methodology](#sentiment-analysis-methodology)
- [Author](#author)

#### Features
- Scrapes Amazon reviews current link is doing for the graphic novel "Maus" using web scraping techniques.
- Analyzes sentiment using TextBlob, classifying each review as positive, negative, or neutral.
- Visualizes the sentiment distribution with a bar chart.
- Provides insights into the overall sentiment of the reviews.

#### Requirements
- Python 3.x
- pandas
- requests
- BeautifulSoup
- textblob
- matplotlib

#### Getting Started
Clone this repository to your local machine:


#### Usage
- Run the `scrape_amazon_reviews.py` script to scrape Amazon reviews and perform sentiment analysis.
- Ensure that the CSV file containing the scraped reviews is named `amazon_reviews_maus.csv` and is saved in the same directory as the script.
- Execute the script using Python:
    ```bash
    python scrape_amazon_reviews.py
    ```
- Go to <b>scrape_amazon_reviews.py</b>
```cd scrape_amazon_reviews.py```

- Replace the url link with your requierd url and run command
Run commands and your Sentimental would be on screen
  ```bash
  python scrape_amazon_reviews.py
  ```
  then 
  ```bash
  python sentiment_analysis.py
  ```
     
#### Sentiment Analysis Methodology
- The script utilizes the TextBlob library for sentiment analysis.
- Each review is classified as positive, negative, or neutral based on the polarity score obtained from TextBlob.
- The sentiment distribution is visualized using a bar chart.

#### Author
Asjid Ali  
Email: asjidale@gmail.com

Feel free to reach out for any questions or feedback.

---
