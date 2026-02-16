# Web Scraper - Book Price Tracker

A Python web scraper that extracts book titles and prices from [books.toscrape.com](https://books.toscrape.com/) and saves the data to a CSV file.

## Features

- 🌐 Scrapes book data from an online bookstore
- 📊 Extracts titles and prices
- 💾 Saves data to CSV format
- 📈 Displays statistics (highest, lowest, average prices)
- 🎯 Shows sample results in console
- ⚡ Error handling for network issues

## Requirements

Install required dependencies:

```bash
pip install requests beautifulsoup4
```

## How to Run

```bash
python web_scraper.py
```

## Output

The scraper generates:
1. **Console Output**: Statistics and sample books
2. **CSV File**: `scraped_books.csv` with all book data

## Features Breakdown

### Data Extraction
- Book titles
- Book prices (in GBP)
- Automatic data parsing

### Statistics Display
- Total number of books
- Highest price
- Lowest price
- Average price
- Total value
- Most expensive book
- Cheapest book

### Sample Output

```
BOOK SCRAPER - books.toscrape.com
============================================================
Found 20 books
Extracted 20 books successfully

First 5 Books:
----------------------------------------------------------------------
#    Title                                                   Price     
----------------------------------------------------------------------
1    A Light in the Attic                                   £51.77    
2    Tipping the Velvet                                     £53.74    
...

STATISTICS
============================================================
Total Books:      20
Highest Price:    £57.25
Lowest Price:     £10.00
Average Price:    £35.46
```

## Code Structure

- `scrape_books()`: Main scraping function
- `save_to_csv()`: Saves data to CSV file
- `show_statistics()`: Calculates and displays statistics
- `show_sample()`: Displays sample results
- `main()`: Orchestrates the scraping process

## Error Handling

- Network timeout (10 seconds)
- Invalid HTML structure
- File I/O errors
- Missing dependencies check

## Customization

You can modify:
- `WEBSITE_URL`: Change the target website
- `OUTPUT_FILE`: Change the output filename
- Timeout duration in `requests.get()`
- Number of sample books displayed

## Notes

- Respects website structure
- Handles connection errors gracefully
- UTF-8 encoding for international characters
- Clean data format for further analysis

## Future Enhancements

- Multi-page scraping
- Filter by category/rating
- Export to JSON/Excel
- Price comparison over time
- Email notifications for price drops
