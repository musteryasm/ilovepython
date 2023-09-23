import pandas as pd
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from googletrans import Translator

# Function to send data from a DataFrame to the API
def send_dataframe_to_api(csv_file_path, api_endpoint):
    try:
        # Load CSV data into a DataFrame
        df = pd.read_csv(csv_file_path, encoding='utf-8')

        # Iterate through DataFrame rows and send data to the API
        for index, row in df.iterrows():
            heading = row['heading']
            body = row['body']

            # Prepare the data to send to the API
            api_data = {
                'heading': heading,
                'description': body,
            }

            # Send a POST request to the API
            try:
                response = requests.post(api_endpoint, json=api_data)
                response.raise_for_status()
                print(f'Data sent to API for Row {index + 1}')

                # Wait for a response from the server before proceeding to the next row
                server_response = response.json()  # Assuming the server returns a JSON response
                print(f'Server Response for Row {index + 1}: {server_response}')

            except requests.exceptions.RequestException as e:
                print(f'Failed to send data to API for Row {index + 1}, Error: {str(e)}')

        print("All data sent to the API and processed.")

    except Exception as e:
        print(f'Error: {str(e)}')

# Function to scrape and send Hindi news to the API
def scrape_and_send_hindi_to_api(api_endpoint):
    try:
        # Set up Chrome WebDriver in headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to the website to extract href links
        url = "https://www.jagran.com/news/national-news-hindi.html?itm_medium=national&itm_source=dsktp&itm_campaign=navigation"
        driver.get(url)

        # Click the "Load More" button until it's no longer available
        while True:
            try:
                load_more_button = driver.find_element(By.ID, "pagination-btn")
                if load_more_button.is_displayed():
                    load_more_button.click()
                    time.sleep(2)  # Adjust as needed
                else:
                    break
            except Exception as e:
                break

        # Find all the href links starting from the specified div elements
        hrefs = []
        div_elements = driver.find_elements(By.XPATH, "//ul[@class='ListingSide_listing__G0B28']/li[@class='ListingSide_CardStory__weOJf CardStory']")
        for div_element in div_elements:
            link = div_element.find_element(By.XPATH, ".//a").get_attribute("href")
            hrefs.append(link)

        # Close the WebDriver
        driver.quit()

        # Function to scrape a URL
        def scrape_url(url):
            try:
                response = requests.get(url)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the first H1 heading
                h1_heading = soup.find('h1').text.strip()

                # Find the div with class 'ArticleBody' and extract text from all <p> tags
                article_body_div = soup.find('div', class_='ArticleBody')
                p_tags = article_body_div.find_all('p')
                paragraph_text = ' '.join([p.text.strip() for p in p_tags])

                return h1_heading, paragraph_text

            except requests.exceptions.RequestException as e:
                return None, str(e)
            except Exception as e:
                return None, str(e)

        # Function to translate text using Google Translate
        def translate_text(text):
            try:
                if not text:
                    return "No text to translate"  # Handle empty text
                translator = Translator()
                translation = translator.translate(text, src='auto', dest='en')
                if hasattr(translation, 'text'):
                    return translation.text
                else:
                    return "Translation failed"
            except Exception as e:
                return str(e)

        # Iterate through the URLs, perform scraping, and send POST requests to the API
        for url in hrefs:
            url = url.strip()
            h1, paragraph = scrape_url(url)

            if h1 is not None:
                # Translate the scraped data into English
                h1_english = translate_text(h1)
                paragraph_english = translate_text(paragraph)

                # Prepare the data to send to the API
                api_data = {
                    'heading': h1_english,
                    'description': paragraph_english,
                }

                # Send a POST request to the API
                try:
                    response = requests.post(api_endpoint, json=api_data)
                    response.raise_for_status()
                    print(f'Data sent to API for URL: {url}')

                    # Wait for a response from the server before proceeding to the next URL
                    server_response = response.json()  # Assuming the server returns a JSON response
                    print(f'Server Response: {server_response}')

                except requests.exceptions.RequestException as e:
                    print(f'Failed to send data to API for URL: {url}, Error: {str(e)}')

            else:
                print(f'Failed to scrape URL: {url}')

    except Exception as e:
        print(f'Error: {str(e)}')

# Function to scrape Marathi news and send to the API
def scrape_marathi_news(api_endpoint):
    try:
        # Set up Chrome WebDriver in headless mode
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to the website
        url = "https://divyamarathi.bhaskar.com/national/"
        driver.get(url)

        # Function to scroll to the bottom of the page to load more content
        def scroll_to_bottom():
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Find the anchor tags with the specified class name
        anchor_tags = []

        # Scroll multiple times to load more content
        for _ in range(3):  # You can adjust the number of times to scroll
            scroll_to_bottom()
            time.sleep(2)  # Wait for content to load, adjust the time as needed

        # Find all <li> elements with the specified class name
        li_elements = driver.find_elements(By.CSS_SELECTOR, "li.c7ff6507.db9a2680")

        # Create a list to store the extracted hrefs
        hrefs = []

        # Iterate through the <li> elements and extract the href attributes from <a> tags
        for li_element in li_elements:
            a_elements = li_element.find_elements(By.TAG_NAME, "a")
            for a_element in a_elements:
                href_attribute = a_element.get_attribute("href")
                hrefs.append(href_attribute)

        # Close the WebDriver
        driver.quit()

        # Function to scrape a URL and return translated heading and body
        def scrape_url_and_translate(url):
            try:
                response = requests.get(url)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the first H1 heading within div class 'a88a1c42'
                heading_div = soup.find('div', class_='a88a1c42')
                h1_heading = heading_div.find('h1').text.strip()

                # Find the div with class 'ba1e62a6' and extract text from all <p> tags
                article_body_div = soup.find('div', class_='ba1e62a6')
                p_tags = article_body_div.find_all('p')
                paragraph_text = ' '.join([p.text.strip() for p in p_tags])

                # Translate the heading and paragraph to English
                translated_heading = translate_text(h1_heading)
                translated_paragraph = translate_text(paragraph_text)

                return translated_heading, translated_paragraph

            except requests.exceptions.RequestException as e:
                return None, str(e)
            except Exception as e:
                return None, str(e)

        # Function to translate text using Google Translate
        def translate_text(text):
            try:
                if not text:
                    return "No text to translate"  # Handle empty text
                translator = Translator()
                translation = translator.translate(text, src='auto', dest='en')
                if hasattr(translation, 'text'):
                    return translation.text
                else:
                    return "Translation failed"
            except Exception as e:
                return str(e)

        # Iterate through the URLs, perform scraping, and translate
        for url in hrefs:
            url = url.strip()
            translated_heading, translated_paragraph = scrape_url_and_translate(url)

            if translated_heading is not None:
                # Prepare the data to send to the API
                api_data = {
                    'heading': translated_heading,
                    'description': translated_paragraph,
                }

                # Send a POST request to the API
                try:
                    response = requests.post(api_endpoint, json=api_data)
                    response.raise_for_status()
                    print(f'Data sent to API for URL: {url}')

                    # Wait for a response from the server before proceeding to the next URL
                    server_response = response.json()  # Assuming the server returns a JSON response
                    print(f'Server Response: {server_response}')

                except requests.exceptions.RequestException as e:
                    print(f'Failed to send data to API for URL: {url}, Error: {str(e)}')

            else:
                print(f'Failed to scrape URL: {url}')

    except Exception as e:
        print(f'Error: {str(e)}')

# Function to create a menu-driven program
def menu_driven_program():
    while True:
        print("Menu:")
        print("1. Scrape Marathi News")
        print("2. Scrape Hindi News and Send to API")
        print("3. Send Data from DataFrame to API")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            marathi_api_endpoint = "https://9ab7-103-246-224-103.ngrok-free.app/predict"  # Replace with Marathi API endpoint
            scrape_marathi_news(marathi_api_endpoint)

        elif choice == '2':
            hindi_api_endpoint = "https://9ab7-103-246-224-103.ngrok-free.app/predict"  # Replace with Hindi API endpoint
            scrape_and_send_hindi_to_api(hindi_api_endpoint)

        elif choice == '3':
            csv_file_path = "New folder/english_data.csv"  # Replace with your CSV file path
            api_endpoint = "https://9ab7-103-246-224-103.ngrok-free.app/predict"  # Replace with the actual API URL
            send_dataframe_to_api(csv_file_path, api_endpoint)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    menu_driven_program()
