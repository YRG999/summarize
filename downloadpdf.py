# download pdf

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
service = Service(ChromeDriverManager().install())

# Choose Chrome Browser
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to open
url = 'https://www.example.com'

# Open URL
driver.get(url)

# Printing the page to PDF
params = {
    'landscape': False,
    'printBackground': True,
    'pageSize': 'A4',
}

# Execute the command to print to PDF
result = driver.execute_cdp_cmd('Page.printToPDF', params)
pdf_base64 = result['data']

# Decode the base64 string to bytes
pdf_bytes = base64.b64decode(pdf_base64)

# Save the PDF to a file
with open('output.pdf', 'wb') as file:
    file.write(pdf_bytes)

# Close the browser
driver.quit()
