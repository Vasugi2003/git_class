# import requests
# from bs4 import BeautifulSoup

# # Make a request to the Scopus article page
# response = requests.get('https://www.scopus.com/record/display.uri?eid=2-s2.0-85021666607&origin=reflist&sort=plf-f&src=s&st1=data+science&sid=667fa2d93fcd814dc2499ca4ea941182&sot=b&sdt=b&sl=19&s=TITLE%28data+science%29')

# # Create a BeautifulSoup object from the response content
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find the mail symbol element
# mail_symbol = soup.find('a', class_='Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN')

# # Extract the email address from the mail symbol
# email_address = mail_symbol['href'].split(':')[1]

# # email_address = mail_symbol.text.strip()

# # Print the email address
# print(email_address)





# <a href="mailto:giovanni.abramo@uniroma2.it" class="Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN"><span class="Icon-module__p52B2 Icon-module__DWv45 Button-module__mZJEx"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 102 128" height="24" width="20" role="img" aria-hidden="true"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></span><span class="Typography-module__lVnit Typography-module__Nfgvc Typography-module___chYC">Send mail to Abramo G.</span></a>



# import requests
# from bs4 import BeautifulSoup

# # Make a request to the Scopus article page
# response = requests.get('https://www.scopus.com/record/display.uri?eid=2-s2.0-85021666607&origin=reflist&sort=plf-f&src=s&st1=data+science&sid=667fa2d93fcd814dc2499ca4ea941182&sot=b&sdt=b&sl=19&s=TITLE%28data+science%29')

# # Create a BeautifulSoup object from the response content
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find the mail symbol element
# mail_symbol = soup.find('a', class_='Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN')

# # Check if the mail symbol element exists
# if mail_symbol is not None:
#     # Extract the email address
#     href = mail_symbol.get('href')
#     if href is not None and href.startswith('mailto:'):
#         email_address = href.split(':')[1]
#         print(email_address)
#     else:
#         print("Email address not found.")
# else:
#     print("Mail symbol element not found.")


# from bs4 import BeautifulSoup

# html = '<a href="mailto:giovanni.abramo@uniroma2.it" class="Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN"><span class="Icon-module__p52B2 Icon-module__DWv45 Button-module__mZJEx"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 102 128" height="24" width="20" role="img" aria-hidden="true"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></span><span class="Typography-module__lVnit Typography-module__Nfgvc Typography-module___chYC">Send mail to Abramo G.</span></a>'

# # Create a BeautifulSoup object
# soup = BeautifulSoup(html, 'html.parser')

# # Find the mail link element
# mail_link = soup.find('a', href=True)

# # Extract the email address
# email_address = mail_link['href'].split(':')[1]

# # Print the email address
# print("Email of the author")
# print(email_address)







import csv
from bs4 import BeautifulSoup

html = '<a href="mailto:giovanni.abramo@uniroma2.it" class="Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN"><span class="Icon-module__p52B2 Icon-module__DWv45 Button-module__mZJEx"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 102 128" height="24" width="20" role="img" aria-hidden="true"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></span><span class="Typography-module__lVnit Typography-module__Nfgvc Typography-module___chYC">Send mail to Abramo G.</span></a>'
html1 = '<a href="mailto:sena.sen@yazar.edu.tr" class="Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN"><span class="Icon-module__p52B2 Icon-module__DWv45 Button-module__mZJEx"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 102 128" height="24" width="20" role="img" aria-hidden="true"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></span><span class="Typography-module__lVnit Typography-module__Nfgvc Typography-module___chYC">Send mail to Abramo G.</span></a>'

# Create a BeautifulSoup object
soup = BeautifulSoup(html1, 'html.parser')
soup1 = BeautifulSoup(html, 'html.parser')

# Find the mail link element
mail_link = soup.find('a', href=True)

mail_link1 = soup1.find('a', href=True)

# Extract the email address
email_address = mail_link['href'].split(':')[1]
email_address1 = mail_link1['href'].split(':')[1]

# Print the email address
print("Email of the author")
print(email_address)
print(email_address1)

# Save the email address in a CSV file
filename = 'email_addrese.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email'])
    writer.writerow([email_address])
    writer.writerow([email_address1])

print("Email address saved in", filename)





