import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

def get_summary_table_value(soup, label):
    try:
        tag = soup.find('td', string=label)
        if tag:
            return tag.find_next_sibling('td').text.strip()
    except:
        return "N/A"
    return "N/A"

def scrape_diversified_market(stock_dict):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}
    results = []

    for sector, symbols in stock_dict.items():
        for symbol in symbols:
            url = f"https://finance.yahoo.com/quote/{symbol}"
            try:
                print(f"Scraping {symbol} [{sector}]...")
                response = requests.get(url, headers=headers, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Basic Price Data
                price_tag = soup.find('fin-streamer', {'data-symbol': symbol, 'data-field': 'regularMarketPrice'})
                change_tag = soup.find('fin-streamer', {'data-symbol': symbol, 'data-field': 'regularMarketChangePercent'})
                
                price = price_tag.text if price_tag else "0"
                change = change_tag.text if change_tag else "0"

                # Financial Metrics
                results.append({
                    "Date": pd.Timestamp.now().strftime('%Y-%m-%d'),
                    "Sector": sector,
                    "Symbol": symbol,
                    "Price": float(price.replace(',', '')),
                    "Change %": change.strip('()%'),
                    "Market Cap": get_summary_table_value(soup, "Market Cap"),
                    "PE Ratio": get_summary_table_value(soup, "PE Ratio (TTM)"),
                    "Div Yield": get_summary_table_value(soup, "Forward Dividend & Yield"),
                    "Beta": get_summary_table_value(soup, "Beta (5Y Monthly)"),
                    "Volume": get_summary_table_value(soup, "Volume").replace(',', '')
                })
                time.sleep(1.5) # Polite delay

            except Exception as e:
                print(f"Error scraping {symbol}: {e}")

    return results

def save_and_append(new_data):
    filename = "market_analysis_data.xlsx"
    new_df = pd.DataFrame(new_data)
    
    if os.path.exists(filename):
        old_df = pd.read_excel(filename)
        # We append so you can track changes over different days
        updated_df = pd.concat([old_df, new_df], ignore_index=True)
    else:
        updated_df = new_df

    updated_df.to_excel(filename, index=False)
    print(f"\n✅ Data saved! Total records in Excel: {len(updated_df)}")

# --- THE DIVERSIFIED LIST ---
# Grouped by sector so you can observe different behaviors
target_stocks = {
    "Technology": ["AAPL", "MSFT", "GOOGL", "NVDA", "ORCL"],
    "Consumer Goods": ["KO", "PEP", "PG", "WMT", "COST"],
    "Finance/Banking": ["JPM", "BAC", "V", "MA", "GS"],
    "Energy/Auto": ["TSLA", "XOM", "CVX", "F", "TM"],
    "Healthcare": ["JNJ", "PFE", "UNH", "ABBV", "LLY"]
}

if __name__ == "__main__":
    scraped_data = scrape_diversified_market(target_stocks)
    save_and_append(scraped_data)