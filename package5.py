import urllib3

# Create a connection pool (recommended for performance)
http = urllib3.PoolManager()

# Specify the URL you want to fetch
url = "https://create-react-app.dev/"

# Send an HTTP GET request and get the response
response = http.request('GET', url)

# Print the response content
print(response.data.decode('utf-8'))

# Close the response to release the connection back to the pool
response.release_conn()
