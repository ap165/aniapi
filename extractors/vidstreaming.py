try:
  from Cryptodome.Util.Padding import pad
  from Cryptodome.Cipher import AES
except:
  from Crypto.Util.Padding import pad
  from Crypto.Cipher import AES
import random
from bs4 import BeautifulSoup
import base64
import requests
import json

key = b'37911490979715163134003223491201'
second_key = b'54674138327930866480207815084989'
iv = b'3134003223491201'

def request_headers():
    headers = {"User-Agent" : random.choice([
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
        "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",
    ])}
    return headers

def get_video_id(url):
  data = requests.get(url,headers=request_headers())
  html = BeautifulSoup(data.text,"html.parser")
  return html.select_one("script[data-name='episode']")["data-value"]

def unpad(data):
  padding_len = data[-1]
  return data[:-padding_len]

def urlParser(url): 
  protocol = url.split("://")[0]
  urldict = {
    "protocol" : protocol,
    "hostname" : url.strip(protocol+"://").split("/")[0],
    "params" : [{ x.split("=")[0] : x.split("=")[1]} for x in url.split("?")[1].split("&")]
  }
  return urldict

def generate_encrypted_parameters(url):
  urlDict = urlParser(url)
  url1 = f"{urlDict['protocol']}://{urlDict['hostname']}/streaming.php?id={urlDict['params'][0]['id']}" 
  vid_id = url.split("?")[1].split("&")[0].split("=")[1]
  cipher_key = AES.new(key, AES.MODE_CBC, iv)
  padded_key = pad(vid_id.encode(), AES.block_size)
  encrypted_key = cipher_key.encrypt(padded_key)
  encoded_key = base64.b64encode(encrypted_key).decode()
  script = get_video_id(url1)
  decoded_script = base64.b64decode(script)
  cipher_script = AES.new(key, AES.MODE_CBC, iv)
  decrypted_script = unpad(cipher_script.decrypt(decoded_script))
  token = decrypted_script.decode()
  encrypted_params = f"id={encoded_key}&alias={vid_id}&{token}"
  return encrypted_params

def decrypt_encrypted_response(response_data):
  decoded_data = base64.b64decode(response_data)
  cipher = AES.new(second_key, AES.MODE_CBC, iv)
  decrypted_data = cipher.decrypt(decoded_data)
  unpadded_data = unpad(decrypted_data)
  decrypted_text = unpadded_data.decode('utf-8')
  return decrypted_text

def getEpStreamingLink(iframeUrl):
  # if "typesub" in iframeUrl:
  #   pass
  # else:
  #   iframeUrl = iframeUrl + "&typesub=DUB" 
  urldict = urlParser(iframeUrl)
  USER_AGENT = request_headers()["User-Agent"]
  encrypted_params = generate_encrypted_parameters(iframeUrl)
  request_url = f"{urldict['protocol']}://{urldict['hostname']}/encrypt-ajax.php?{encrypted_params}"
  headers = {"User-Agent" : USER_AGENT,"X-Requested-With": "XMLHttpRequest"}
  response = requests.get(request_url,headers = headers)
  decryptedJson = decrypt_encrypted_response(response.json()["data"])
  return json.loads(decryptedJson)

# if __name__ == "__main__":
#   print(getEpStreamingLink("https://embtaku.pro/streaming.php?id=MjU1OTA=&title=Naruto+Episode+205"))