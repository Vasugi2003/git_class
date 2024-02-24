import requests
import json

# Enter your Scopus API key here
api_key = "de3fa64422812154a049747abb09e00b"

# Get user input for topic
topic_name = input("Enter the topic you want to search: ")

# Make the request to the Scopus API
url = f"https://api.elsevier.com/content/search/scopus?query=all({topic_name})&apiKey={api_key}"
response = requests.get(url)

# Check the status code of the response
if response.status_code != 200:
    print("Error making request to Scopus API")
else:
    # Parse the JSON response
    json_data = json.loads(response.text)
    # Extract the list of articles from the response
    articles = json_data['search-results']['entry'][:5]  # Limit to first 5 articles
    # Loop through the articles and extract the author information
    
    for article in articles:
        print(articles)
        print("\n")
        print(f"Title for article '{article['dc:title']}':")
        print("\n")
        print(f"Authors for article '{article['dc:creator']}':")
        print(f" eid for article '{article['eid']}':")
        eid = article['eid']
        
        
        
        # for author in author_list:
        #     author_name = author.split(',')[0]
        #     url = f"https://api.elsevier.com/content/author/EID/{eid}?view=METRICS&apiKey={api_key}"
        #     author_response = requests.get(url)
        #     if author_response.status_code == 200:
        #         author_json = json.loads(author_response.text)
        #         author_details = author_json['author-retrieval-response'][0]
        #         author_affiliation = author_details['affiliation-current']['affiliation-name']
        #         author_email = author_details.get('email', 'N/A')
        #         print(f"{author_name} - {author_affiliation} - Email: {author_email}")
        #     else:
        #         print(f"Error retrieving details for author '{author}'") 
        
        
        url = f"https://api.elsevier.com/content/author/EID/{eid}?view=METRICS&apiKey={api_key}"
        response = requests.get(url)

# Check the status code of the response
        if response.status_code != 200:
            print("Error making request to Scopus API")
        else:
            json_data = json.loads(response.text)
 
# import requests

# def download_paper_by_doi(doi):
#     base_url = "https://doi.org/"
#     headers = {
#         "Accept": "application/pdf",
#     }

#     url = base_url + doi
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         # Save the paper as a PDF file
#         file_name = doi.replace("/", "_") + ".pdf"
#         with open(file_name, "wb") as f:
#             f.write(response.content)
#         print(f"Paper downloaded successfully: {file_name}")
#     else:
#         print(f"Failed to download the paper. Status code: {response.status_code}")

# # Example usage with the DOI of the first paper in your provided data
# doi = "10.1002/9781119724872.ch4"
# download_paper_by_doi(doi)


import webbrowser

def open_paper_by_doi(doi):
    base_url = "https://doi.org/"
    url = base_url + doi
    webbrowser.open(url)

# Example usage with the DOI of the first paper in your provided data
# doi = "10.1002/9781119724872.ch4"

doi = "10.1002/9781119724872.ch9"
open_paper_by_doi(doi)
