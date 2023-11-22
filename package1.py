from urllib.request import urlopen, Request

url = "https://www.google.com"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # Create a Request object with custom headers
response = urlopen(req)  # Open the URL using the Request object
html = response.read()   # Read the HTML content

print(html.decode('utf-8'))  # Decode and print the content
