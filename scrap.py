from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

chrome_driver_path = 'chromedriver-win32\chromedriver-win32\chromedriver.exe'
# First website (Daraz)
daraz_url = 'https://www.daraz.pk/catalog/?q=phone&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34076RJGmo2'
daraz_driver = webdriver.Chrome(executable_path=chrome_driver_path)
daraz_driver.get(daraz_url)

# Find product title and price on the first website (Daraz)
daraz_product_title = daraz_driver.find_element(By.XPATH, '(//*[contains(text(),"Samsung A14 6/128")])[2]').text.strip()
daraz_product_price = daraz_driver.find_element(By.XPATH,'(//*[contains(text(),"Rs. 53,999")])[2]').text.strip()

# Second website (PriceOye)
PriceOye_url = 'https://priceoye.pk/search?q=Samsung+A14'
PriceOye_website_driver = webdriver.Chrome(executable_path=chrome_driver_path)
PriceOye_website_driver.get(PriceOye_url)

# Find product title and price on the second website
PriceOye_product_title = PriceOye_website_driver.find_element(By.XPATH,"//div[@class='p-title bold h5']").text.strip()
PriceOye_product_price = PriceOye_website_driver.find_element(By.XPATH,"//div[@class='price-box p1']").text.strip()

# Close the browsers
daraz_driver.quit()
PriceOye_website_driver.quit()

# Create Pandas DataFrame
data = {
    'Website': ['Daraz', 'PriceOye'],
    'Product Title': [daraz_product_title, PriceOye_product_title],
    'Product Price': [daraz_product_price, PriceOye_product_price]
}
df = pd.DataFrame(data)

# Clean data and check for duplicates and missing values
df.drop_duplicates(subset=['Product Title', 'Product Price'], keep='last', inplace=True)
df.dropna(subset=['Product Title', 'Product Price'], inplace=True)

# Print the cleaned data
print('Cleaned Data:')
print(df)

if daraz_product_price > PriceOye_product_price:
    print('Priceoye recommended for buying this product!')
else: 
    print('Daraz recommended for buying this product!')
