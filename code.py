import requests
import pyqrcode
import png
from pyqrcode import QRCode




# replace your API key
api_key = "ac38eda7ffe7f281901177e33a4b1108978cb"

# the URL you want to shorten
url = "https://www.youtube.com/watch?v=T_55mVi_wQQ&ab_channel=FORMULA1"

# preferred name in the URL

api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
# or
# api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"

# make the request
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)

url2 = pyqrcode.create(shortened_url)
url2.png('myqr.png', scale = 6)
