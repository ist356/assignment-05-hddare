from datetime import datetime

def clean_currency(item: str) -> float:
    '''
    remove anything from the item that prevents it from being converted to a float
    '''    
    cleaned_item = ''.join(c for c in item if c.isdigit() or c == '.' or c == '-')
    return float(cleaned_item) if cleaned_item else 0.0

def extract_year_mdy(timestamp: str) -> int:
    '''
    use the datetime.strptime to parse the date and then extract the year
    '''
    try:
        dt = datetime.strptime(timestamp, '%m/%d/%Y %H:%M:%S')
        return dt.year
    except ValueError:
        raise ValueError(f"Timestamp '{timestamp}' does not match the format 'MM/DD/YYYY'")

def clean_country_usa(item: str) -> str:
    '''
    This function should replace any combination of 'United States of America', USA' etc.
    with 'United States'
    '''
    possibilities = [
        'united states of america', 'usa', 'us', 'united states', 'u.s.'
    ]
    item_lower = item.lower().strip()
    if item_lower in possibilities:
        return 'United States'
    return item

if __name__ == '__main__':
    print("""
        Add code here if you need to test your functions
        Comment out the code below this before submitting to improve your code similarity score.
    """)
    # Example usage
    print(clean_currency("$1,234.56"))  # Should output: 1234.56
    print(extract_year_mdy("03/25/2021"))  # Should output: 2021
    print(clean_country_usa("USA"))  # Should output: United States
