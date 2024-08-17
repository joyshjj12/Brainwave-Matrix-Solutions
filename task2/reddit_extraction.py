from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from datetime import datetime
import time

# Function to scrape comments and timestamps
def scrape_comments_and_timestamps(url, retries=3, delay=5):
    options = Options()
    options.headless = True  # Run in headless mode

    # Specify the path to your chromedriver executable
    chromedriver_path = r"C:\Users\joysh\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Replace with the actual path to your ChromeDriver

    # Initialize WebDriver
    service = Service(executable_path=chromedriver_path)
    
    attempt = 0
    while attempt < retries:
        try:
            driver = webdriver.Chrome(service=service, options=options)
            
            try:
                # Load the page
                driver.get(url)
                
                # Wait for the comments to load
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.md')))
                
                # Extract comments and timestamps
                comments_elements = driver.find_elements(By.CSS_SELECTOR, 'div.md p')
                timestamps_elements = driver.find_elements(By.CSS_SELECTOR, 'time')
                
                data = []
                for comment, timestamp in zip(comments_elements, timestamps_elements):
                    comment_text = comment.text
                    date_time_str = timestamp.get_attribute('datetime')
                    
                    # Handle cases where date_time_str might be None
                    if date_time_str:
                        date_time = datetime.fromisoformat(date_time_str.replace('Z', '+00:00'))
                        data.append({'comment': comment_text, 'date_time': date_time})
                
                return data
            
            finally:
                # Ensure the WebDriver session is closed
                driver.quit()
        
        except (TimeoutException, WebDriverException) as e:
            print(f"Error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            attempt += 1
    
    print("Failed to retrieve data after several retries.")
    return None

# Function to save comments to a text file
def save_comments_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in data:
            file.write(f"Comment: {entry['comment']}\n")
            file.write(f"Date and Time: {entry['date_time']}\n")
            file.write("\n" + "-"*80 + "\n")  # Separator for readability

# URL of the Reddit page
url = 'https://www.reddit.com/r/Android/comments/1b7756j/samsung_galaxy_s24_review_the_best_small_android/'
# Scrape comments and timestamps
data = scrape_comments_and_timestamps(url)

# Save the data to a text file
if data:
    save_comments_to_file(data, 'c13.txt')
    print("Comments saved to comments.txt")
else:
    print("No comments found or failed to scrape the webpage.")
