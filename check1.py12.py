hip=0
ps=0
ssl=0
uoa=0
rc=0
ifr=0
goo=0
str="www.facebook.com"
##########################################################################################
#prefix and sufix 
from urllib.parse import urlparse
dash=urlparse(str).netloc
if("-" not in dash):
    ps=0
    print("True")
else:
    ps=1
    print("False")

##########################################################################################
#subdomains
from urllib.parse import urlparse

def count_dots_in_domain(url):
    try:
        # Parse the URL to get the hostname
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc

        # Count the dots in the hostname
        dot_count = hostname.count('.')
        
        return dot_count
    except ValueError:
        # Handle invalid URLs
        return -1
# Example usage
url =str
dot_count = count_dots_in_domain(url)

if dot_count >= 0:
    print(f"Number of dots in the domain: {dot_count}")
else:
    print("Invalid URL")

##############################################################################################
#url of anchor
from urllib.parse import urlparse

def calculate_anchor_percentage(url):
    # Parse the URL using urlparse
    parsed_url = urlparse(url)
    
    # Extract the anchor (fragment) from the parsed URL
    anchor = parsed_url.fragment
    
    # Calculate the length of the anchor
    anchor_length = len(anchor)
    
    # Calculate the total length of the URL (excluding the anchor)
    total_length = len(url) - anchor_length
    
    # Calculate the percentage
    if total_length > 0:
        percentage = (anchor_length / total_length) * 100
    else:
        percentage = 0.0  # Handle division by zero
    
    return percentage

# Example usage:
url_to_parse = str
percentage = calculate_anchor_percentage(url_to_parse)

print(f"The anchor represents {percentage:.2f}% of the URL.")

if(percentage<31):
    uoa=0
elif(percentage>=31 and percentage<=67):
    uoa=-1
else:
    uoa=1

###################################################################################################
#right click
import requests

def is_right_click_enabled(url):
    try:
        # Send an HTTP GET request to fetch the website's HTML content
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Check if common JavaScript event handlers are present in the HTML content
            html_content = response.text
            if "contextmenu" not in html_content.lower() and "oncontextmenu" not in html_content.lower():
                return True
    except requests.exceptions.RequestException:
        pass
    
    return False

# Example usage:
url_to_check = str  
if is_right_click_enabled(url_to_check):
    rc=1
    print(f"{url_to_check} allows right-click.")
else:
    rc=0
    print(f"{url_to_check} may have right-click disabled.")
###########################################################################################################
#iframe
import requests
from bs4 import BeautifulSoup

def has_iframes(url):
    try:
        # Send an HTTP GET request to fetch the webpage's HTML content
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all iframe tags in the HTML
            iframe_tags = soup.find_all('iframe')

            # Check if any iframe tags were found
            if len(iframe_tags) > 0:
                return True

    except requests.exceptions.RequestException:
        pass

    return False

# Example usage:
url_to_check =str
if has_iframes(url_to_check):
    ifr=1
    print(f"{url_to_check} contains iframes.")
else:
    ifr=0
    print(f"{url_to_check} does not contain iframes or could not be reached.")

##########################################################################################################
#google index
import requests
from bs4 import BeautifulSoup

def is_url_indexed(url):
    # Prepare the search query URL
    search_url = f"https://www.google.com/search?q=site:{url}"

    # Send an HTTP GET request to Google
    response = requests.get(search_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all search results
        search_results = soup.find_all("div", class_="tF2Cxc")

        # Check if the URL appears in the search results
        for result in search_results:
            result_url = result.find("a")["href"]
            if url in result_url:
                return True

    return False
url_to_check = str
if is_url_indexed(url_to_check):
    goo=1
    print(f"{url_to_check} is not indexed by Google.")
else:
    goo=1
    print(f"{url_to_check} is indexed by Google.")

para=[hip,ps,ssl,uoa,rc,ifr,goo]
print(para)