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
        print(f"Title for article '{article['dc:title']}':")
        print(f"Authors for article '{article['dc:creator']}':")
        eid = article['eid']
        
        # Make a request to the Scopus Author Retrieval API to retrieve author details
        author_api_url = f"https://api.elsevier.com/content/author/EID/{eid}?apiKey={api_key}"
        author_response = requests.get(author_api_url)
        
        # Check the status code of the author API response
        if author_response.status_code == 200:
            author_json = json.loads(author_response.text)
            author_details = author_json['author-retrieval-response'][0]
            author_affiliation = author_details['affiliation-current']['affiliation-name']
            author_email = author_details.get('email', 'N/A')
            print(f"Author affiliation: {author_affiliation}")
            print(f"Author email: {author_email}")
        else:
            print(f"Error retrieving details for author with EID: {eid}")
