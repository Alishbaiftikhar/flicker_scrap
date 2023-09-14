import requests
from bs4 import BeautifulSoup
cookies = {
    'xb': '521810',
    'ccc': '%7B%22needsConsent%22%3Afalse%2C%22managed%22%3A0%2C%22changed%22%3A0%2C%22info%22%3A%7B%22cookieBlock%22%3A%7B%22level%22%3A0%2C%22blockRan%22%3A0%7D%7D%2C%22freshServerContext%22%3Atrue%7D',
    '_sp_ses.df80': '*',
    '_uc_referrer': 'https://www.google.com/',
    'sp': 'd6eddb87-c23c-4f1b-aa4e-64ef77edef92',
    '__ssid': 'df1ecaaca6b93342f33d96db421dc73',
    '__gads': 'ID=7bac0c2a78d6d40d:T=1694589244:RT=1694589244:S=ALNI_MYVLYe9bzupC04FfFbuQgadFTQWJw',
    '__gpi': 'UID=00000ca11b8c933b:T=1694589244:RT=1694589244:S=ALNI_MYVre2Cd_QPmX4sUCqtIwMbL9V_XQ',
    'vp': '1903%2C492%2C1%2C17%2Csearch-photos-everyone-view%3A1182%2Cphotolist-container%3A1522%2Cprofile-container%3A1522%2Cphotosof-container%3A1522%2Calbums-list-page-view%3A1522%2Cshowcase-container%3A1903',
    '_sp_id.df80': 'a48f3b3e-28ba-4284-ac34-01c94ddb7879.1694589237.1.1694589372..24beb468-11d5-4e19-a7d0-c7f2bcc74515..fa10a2ba-f2c4-4f66-81b0-a16dfe753676.1694589236752.38',
}

headers = {
    'authority': 'www.flickr.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'xb=521810; ccc=%7B%22needsConsent%22%3Afalse%2C%22managed%22%3A0%2C%22changed%22%3A0%2C%22info%22%3A%7B%22cookieBlock%22%3A%7B%22level%22%3A0%2C%22blockRan%22%3A0%7D%7D%2C%22freshServerContext%22%3Atrue%7D; _sp_ses.df80=*; _uc_referrer=https://www.google.com/; sp=d6eddb87-c23c-4f1b-aa4e-64ef77edef92; __ssid=df1ecaaca6b93342f33d96db421dc73; __gads=ID=7bac0c2a78d6d40d:T=1694589244:RT=1694589244:S=ALNI_MYVLYe9bzupC04FfFbuQgadFTQWJw; __gpi=UID=00000ca11b8c933b:T=1694589244:RT=1694589244:S=ALNI_MYVre2Cd_QPmX4sUCqtIwMbL9V_XQ; vp=1903%2C492%2C1%2C17%2Csearch-photos-everyone-view%3A1182%2Cphotolist-container%3A1522%2Cprofile-container%3A1522%2Cphotosof-container%3A1522%2Calbums-list-page-view%3A1522%2Cshowcase-container%3A1903; _sp_id.df80=a48f3b3e-28ba-4284-ac34-01c94ddb7879.1694589237.1.1694589372..24beb468-11d5-4e19-a7d0-c7f2bcc74515..fa10a2ba-f2c4-4f66-81b0-a16dfe753676.1694589236752.38',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

response = requests.get('https://www.flickr.com/people/alihill007/', cookies=cookies, headers=headers)
file_html=open('text.html','w',encoding="utf-8")
file_html.write(str(response.text))
file_html.close()
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    # Find the <span> element with the specified class name
    date_span = soup.find("a", class_="archives-link")
    print("///////////////////////////////////////////////////////////////////////////////////////////")
    if date_span:
        # Extract the date text
        joined_date = date_span.text.strip()
        print("Joined Date:", joined_date)
    else:
        print("Joined date not found on the page.")
    print("///////////////////////////////////////////////////////////////////////////////////////////")
    span_element = soup.find('p', class_='metadata-item photo-count')
    if span_element:
        # Extract the text content from the <span> element
        photos = span_element.text
        print("Photo_count:", photos)
    else:
        print("Span element with the specified id not found.")
    print("///////////////////////////////////////////////////////////////////////////////////////////")
    p_element = soup.find('p', class_='followers')
    if p_element:
        # Extract the text content from the <p> element
        text_content = p_element.text
        
        # Split the text into "followers" and "following" parts
        parts = text_content.split('•')
        
        if len(parts) == 2:
            followers = parts[0].strip()
            following = parts[1].strip()
            
            print("Followers:", followers)
            print("///////////////////////////////////////////////////////////////////////////////////////////")
            print("Following:", following)
        else:
            print("Invalid format in the <p> element.")
    else:
        print("Paragraph element with the specified id not found.")
    print("///////////////////////////////////////////////////////////////////////////////////////////")
    photo_divs = soup.find_all('div', class_='view photo-list-photo-view requiredToShowOnServer')

h4_element = soup.find('h4', text='Most popular photos')

# Find the parent div of h4_element
parent_div = h4_element.find_parent()
# Find the next div with class "view photo-list-view requiredToShowOnServer"
photo_list_div = parent_div.find_next('div', class_='view photo-list-view requiredToShowOnServer')

# Find all div elements inside photo_list_div with a background-image
divs_with_background_image = photo_list_div.find_all('div', style=lambda x: x and 'background-image' in x)

# Extract and print the URLsS
background_image_urls = [div['style'].split('background-image: url(')[1].rstrip(')') for div in divs_with_background_image]
print("Most Popular Photos:")
for url in background_image_urls:
    print(url)
else:
    print("")
