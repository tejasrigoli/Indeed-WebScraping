##Used python3.9, selenium and chromedriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    logging.info("Opening the Indeed URL")
    url = "https://www.indeed.com/jobs?q=Fall+2024+Software+Intern"
    driver.get(url)

    logging.info("Waiting for job listings to be visible")
    wait = WebDriverWait(driver, 10)
    job_listings_selector = 'td.resultContent'  # Updated selector for job listings
    job_listings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, job_listings_selector)))

    logging.info("Extracting job listings")
    jobs = driver.find_elements(By.CSS_SELECTOR, job_listings_selector)

    if not jobs:
        logging.error("No job listings found.")
        driver.save_screenshot('screenshot_no_jobs.png')
    else:
        logging.info(f"Found {len(jobs)} job listings.")

    for i, job in enumerate(jobs[:10]):
        try:
            logging.info(f"Processing job {i+1}")

            title_element = job.find_element(By.CSS_SELECTOR, 'h2.jobTitle span')
            title = title_element.get_attribute('title') if title_element else "No Title"

            company_element = job.find_element(By.CSS_SELECTOR, 'span[data-testid="company-name"]')
            company = company_element.text if company_element else "No Company"

            location_element = job.find_element(By.CSS_SELECTOR, 'div[data-testid="text-location"]')
            location = location_element.text if location_element else "No Location"

            print(f"Job {i+1}:")
            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Location: {location}")
            print("-" * 20)
        
        except Exception as e:
            logging.error(f"Error processing job {i+1}: {e}")
            driver.save_screenshot(f'screenshot_error_job_{i+1}.png')

except Exception as e:
    logging.error(f"An error occurred: {e}")
    driver.save_screenshot('screenshot_error.png')

finally:
    logging.info("Closing the browser")
    driver.quit()
