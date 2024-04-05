import requests
# import

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-03-05&"
       "sortBy=publishedAt&apiKey="
       "d395f29510bf401bb6e65148ae903558")

# Get API
request = requests.get(url)
# Connvert API into a python dictionary (JSON)
content = request.json()

for article in content["articles"]:
    print(article["title"])