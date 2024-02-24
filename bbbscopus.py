from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the Selenium webdriver
driver = webdriver.Chrome()

# Navigate to the Scopus article page
url = 'https://www.scopus.com/record/display.uri?eid=2-s2.0-85078361802&origin=reflist&sort=plf-f&src=s&st1=deep+learning&sid=a6f3d87cfa406bdae74516775fdc96f4&sot=b&sdt=b&sl=20&s=TITLE%28deep+learning%29'  # Replace with the actual Scopus article URL
driver.get(url)

# Wait for the page to load (if necessary)
# ...

# Extract the HTML content of the page
html_content = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the title of the article
title_element = soup.find('h1')
title = title_element.text.strip() if title_element else 'N/A'

# Extract the abstract of the article
abstract_element = soup.find('a', class_='Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN')
abstract = abstract_element.text.strip() if abstract_element else 'N/A'

# Extract other relevant information from the article page
# ...

# Close the browser
driver.quit()

# Print or store the extracted data
print("Title:", title)
print("Abstract:", abstract)


# <a href="mailto:sena.sen@yasar.edu.tr" class="Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN"><span class="Icon-module__p52B2 Icon-module__DWv45 Button-module__mZJEx"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 102 128" height="24" width="20" role="img" aria-hidden="true"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></span><span class="Typography-module__lVnit Typography-module__Nfgvc Typography-module___chYC">Send mail to Sen S.Y.</span></a>