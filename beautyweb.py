# from bs4 import BeautifulSoup
# from requests import get
# import re

# page = "https://www.eurocham-cambodia.org/member/476/2-LEau-Protection"

# content = get(page).content
# soup = BeautifulSoup(content, "lxml")

# exp = re.compile(r"(?:.*?='(.*?)')")
# # Find any element with the mail icon
# for icon in soup.findAll("i", {"class": "icon-mail"}):
#     # the 'a' element doesn't exist, there is a script tag instead
#     script = icon.next_sibling
#     # the script tag builds a long array of single characters- lets gra
#     chars = exp.findall(script.text)
#     output = []
#     # the javascript array is iterated backwards
#     for char in reversed(list(chars)):
#         # many characters use their ascii representation instead of simple text
#         if char.startswith("|"):
#             output.append(chr(int(char[1:])))
#         else:
#             output.append(char)
#     # putting the array back together gets us an `a` element
#     link = BeautifulSoup("".join(output))
#     email = link.findAll("a")[0]["href"][8:]
#     # the email is the part of the href after `mailto: `
#     print(email)











# import requests
# from bs4 import BeautifulSoup as soup
# def get_emails(_links:list, _r = [0, 10]):
#   for i in range(*_r):
#      new_d = soup(requests.get(_links[i]).text, 'html.parser').find_all('a', {'class':'Button-module__f8gtt Button-module__rphhF Button-module__VBKvn Button-module__PzLy5 Button-module__NJVRN'})
#      if new_d:
#        yield new_d[-1]['title']

# d = soup(requests.get(' https://www.scopus.com/record/display.uri?eid=2-s2.0-85021666607&origin=reflist&sort=plf-f&src=s&st1=data+science&sid=667fa2d93fcd814dc2499ca4ea941182&sot=b&sdt=b&sl=19&s=TITLE%28data+science%29').text, 'html.parser')
# results = [i['href'] for i in d.find_all('a')][52:-9]
# print(list(get_emails(results)))



# import requests
# from bs4 import BeautifulSoup

# def get_email_address(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     mail_link = soup.find('a', href=True)
#     email_address = mail_link['href'].split(':')[1] if mail_link else None

#     return email_address

# if __name__ == '__main__':
#     article_url = input("Enter the article URL: ")
#     email_address = get_email_address(article_url)
#     print("Email of the author:")
#     print(email_address)



# import requests
# from bs4 import BeautifulSoup

# def get_email_address(url, class_name):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     mail_link = soup.find('a', class_=class_name, href=True)
#     email_address = mail_link['href'].split(':')[1] if mail_link else None

#     return email_address

# if __name__ == '__main__':
#     article_url = input("Enter the article URL: ")
#     class_name = input("Enter the class name: ")
#     email_address = get_email_address(article_url, class_name)
#     print("Email of the author:")
#     print(email_address)


import requests
from bs4 import BeautifulSoup

# Send a GET request to the article page URL
url = 'https://www.example.com/article'  # Replace with the actual article page URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the article
title_element = soup.find('h1')
title = title_element.text.strip() if title_element else 'N/A'

# Extract the content of the article
content_element = soup.find('div', class_='article-content')
content = content_element.text.strip() if content_element else 'N/A'

# Extract other relevant information from the article page
# ...

# Print or store the extracted data
print("Title:", title)
print("Content:", content)
