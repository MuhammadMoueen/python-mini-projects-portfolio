import requests
from bs4 import BeautifulSoup
import csv

# Website configuration
WEBSITE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "scraped_books.csv"


def scrape_books(url):
    """Scrape book titles and prices from the website."""
    print(f"\nConnecting to {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("Connected successfully!")
        
    except requests.RequestException as e:
        print(f"Connection error: {e}")
        return []
    
    # Parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    book_elements = soup.find_all('article', class_='product_pod')
    
    if not book_elements:
        print("No books found.")
        return []
    
    print(f"Found {len(book_elements)} books")
    
    # Extract book data
    books = []
    for element in book_elements:
        title_tag = element.find('h3').find('a')
        price_tag = element.find('p', class_='price_color')
        
        if title_tag and price_tag:
            title = title_tag.get('title', 'Unknown')
            price_text = price_tag.text.replace('£', '').strip()
            
            try:
                price = float(price_text)
            except ValueError:
                price = 0.0
            
            books.append({
                'title': title,
                'price': price
            })
    
    print(f"Extracted {len(books)} books successfully")
    return books


def save_to_csv(books, filename):
    """Save book data to CSV file."""
    if not books:
        print("No data to save")
        return False
    
    print(f"\nSaving to {filename}...")
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'price'])
            writer.writeheader()
            writer.writerows(books)
        
        print(f"Saved successfully to {filename}")
        return True
        
    except IOError as e:
        print(f"Error saving file: {e}")
        return False


def show_statistics(books):
    """Calculate and display statistics about the books."""
    if not books:
        print("\nNo data to analyze")
        return
    
    prices = [book['price'] for book in books]
    

    print("\n" + "=" * 60)
    print("STATISTICS")
    print("=" * 60)
    print(f"Total Books:      {len(books)}")
    print(f"Highest Price:    £{max(prices):.2f}")
    print(f"Lowest Price:     £{min(prices):.2f}")
    print(f"Average Price:    £{sum(prices) / len(prices):.2f}")
    print(f"Total Value:      £{sum(prices):.2f}")
    print("=" * 60)
    
    
    # Most expensive book
    most_expensive = max(books, key=lambda x: x['price'])
    print(f"\nMost Expensive:")
    print(f"  {most_expensive['title']}")
    print(f"  £{most_expensive['price']:.2f}")
    
    # Cheapest book
    cheapest = min(books, key=lambda x: x['price'])
    print(f"\nCheapest:")
    print(f"  {cheapest['title']}")
    print(f"  £{cheapest['price']:.2f}")


def show_sample(books, count=5):
    """Display a sample of the scraped books."""
    if not books:
        return
    
    print(f"\nFirst {count} Books:")
    print("-" * 70)
    print(f"{'#':<4} {'Title':<55} {'Price':<10}")
    print("-" * 70)
    
    for i, book in enumerate(books[:count], 1):
        title = book['title']
        if len(title) > 52:
            title = title[:52] + "..."
        print(f"{i:<4} {title:<55} £{book['price']:<9.2f}")
    
    print("-" * 70)


def main():
    """Main function to run the web scraper."""
    print("\n" + "=" * 60)
    print("BOOK SCRAPER - books.toscrape.com")
    print("=" * 60)
    
    # Scrape the website
    books = scrape_books(WEBSITE_URL)
    
    if not books:
        print("\nScraping failed. Exiting...")
        return
    
    # Display results
    show_sample(books)
    show_statistics(books)
    
    # Save to CSV
    save_to_csv(books, OUTPUT_FILE)
    
    print(f"\nComplete! Check '{OUTPUT_FILE}' for all data.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    # Check for required libraries
    try:
        import requests
        import bs4
    except ImportError as e:
        print(f"\nError: Missing library - {e.name}")
        print("Install with: pip install requests beautifulsoup4")
        exit(1)
    
    main()
