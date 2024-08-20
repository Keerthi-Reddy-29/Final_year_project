import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Function to get the HTML content of a page
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

# Function to parse the HTML content and extract reviews
def parse_reviews(html):
    soup = BeautifulSoup(html, 'html.parser')
    reviews = []
    review_divs = soup.find_all('div', {'data-hook': 'review'})
    for review in review_divs:
        title = review.find('a', {'data-hook': 'review-title'}).get_text(strip=True) if review.find('a', {'data-hook': 'review-title'}) else ''
        rating = review.find('i', {'data-hook': 'review-star-rating'}).get_text(strip=True) if review.find('i', {'data-hook': 'review-star-rating'}) else ''
        date = review.find('span', {'data-hook': 'review-date'}).get_text(strip=True) if review.find('span', {'data-hook': 'review-date'}) else ''
        text = review.find('span', {'data-hook': 'review-body'}).get_text(strip=True) if review.find('span', {'data-hook': 'review-body'}) else ''
        reviews.append({
            'title': title,
            'rating': rating,
            'date': date,
            'text': text
        })
    return reviews

# Function to parse the HTML content and extract reviews
def parse_reviews(html):
    soup = BeautifulSoup(html, 'html.parser')
    reviews = []
    review_divs = soup.find_all('div', {'data-hook': 'review'})
    for review in review_divs:
        title = review.find('a', {'data-hook': 'review-title'}).get_text(strip=True) if review.find('a', {'data-hook': 'review-title'}) else ''
        rating = review.find('i', {'data-hook': 'review-star-rating'}).get_text(strip=True) if review.find('i', {'data-hook': 'review-star-rating'}) else ''
        date = review.find('span', {'data-hook': 'review-date'}).get_text(strip=True) if review.find('span', {'data-hook': 'review-date'}) else ''
        text = review.find('span', {'data-hook': 'review-body'}).get_text(strip=True) if review.find('span', {'data-hook': 'review-body'}) else ''
        reviews.append({
            'title': title,
            'rating': rating,
            'date': date,
            'text': text
        })
    return reviews

# Function to scrape reviews from multiple pages
def scrape_amazon_reviews(url, num_pages):
    all_reviews = []
    for page in range(1, num_pages + 1):
        page_url = f'{url}&pageNumber={page}'
        print(f'Scraping page {page}...')
        html = get_html(page_url)
        reviews = parse_reviews(html)
        all_reviews.extend(reviews)
        time.sleep(2)  # Be polite and don't overwhelm the server
    return all_reviews

# Main function
def main():
    # URL of the Amazon product reviews page you want to scrape
    url = 'https://www.amazon.com/One-Star-Reviews-Very-Worst-Products-ebook/dp/B00PMIGXIS/ref=sr_1_1?crid=2Y4OGCCN2FOVD&dib=eyJ2IjoiMSJ9.ayJMusQjiVDhf-iBpmOF2pdnhRwKCNwr-86TvZmk-wPARM4KqmAXs5PyW2mIFyl8.GtN1hCd1P9rhkZSHGTexbvFg-HmUIKxQpLlrOBC8cfk&dib_tag=se&keywords=worst+reviewed+products+1+star&qid=1723611509&sprefix=1+star+produ%2Caps%2C474&sr=8-1'

    num_pages = 5  # Number of pages to scrape
    reviews = scrape_amazon_reviews(url, num_pages)

    # Create a DataFrame from the reviews and save it to a CSV file
    if reviews:
        df = pd.DataFrame(reviews)
        df.to_csv('amazon_reviews_maus.csv', index=False)
        print('Reviews saved to amazon_reviews_maus.csv')
    else:
        print('No reviews')
    
    # Create a DataFrame from the reviews and save it to a CSV file
    df = pd.DataFrame(reviews)
    df.to_csv('amazon_reviews_maus.csv', index=True)
    print('Reviews saved to amazon_reviews_maus.csv')

if __name__ == '__main__':
    main()
