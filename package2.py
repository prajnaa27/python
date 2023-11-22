from urllib.parse import urlparse
from urllib.parse import parse_qs

query_string = "name=John&age=30&city=New+York"
parsed_query = parse_qs(query_string)

print(parsed_query)
# Output: {'name': ['John'], 'age': ['30'], 'city': ['New York']}


url = "https://www.example.com/path?name=John&age=30"
parsed_url = urlparse(url)

print(parsed_url.scheme)  # Output: "https"
print(parsed_url.netloc)  # Output: "www.example.com"
print(parsed_url.path)    # Output: "/path"
print(parsed_url.query)   # Output: "name=John&age=30"
