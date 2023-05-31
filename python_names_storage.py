from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests
import csv

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict ={
  "type": "service_account",
  "project_id": "perfect-reserve-307816",
  "private_key_id": "2a6c945b0d23ff3e8655be310c6b54642d6602ba",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCfTACM89uUcf30\n1Lrd9OlUld2eCzaE3HCq8IKaEjGtWwE0ckmHvuftKSebK8UJC8qIV0sI6CBhcd8A\nO1mWi1jay9AtTt8qmYHnZjEkmIN2K7XgDm11yOoZGjFq8M5PaYd5zxF0rJBUYneD\nBTxRvamI1zucc3/aVQX5NLvWO2TgKt9TOG37D7ORNITD2ZvVhZMjeLzfrjcrebwZ\nUVsv6f+Q+u8TNld7TnYpaxfAD1QOqxjDH8mfodooAMXevsxPy7XOwgqoq0qKm/8K\nz8ICjY6vRrWHGXrYNSBcnyNIPv3zNDTdrE80//r6AGwxuCbvMb38oKj9EW+FBU0e\nArRPZSRjAgMBAAECggEAIQA0yP6oCcvHydXcVKktQYm+nMRD6ihk6vTiiZqlUf2d\ndUkL9KRXFenFu77IlgQsVCyJbfHw618UzM5+09JQeRtqKEjDsOaWY+Lm4Wb7LRsH\nFcDHanRSExs7C6WRiCAbod+FBT/Osrynd6w4/9Ij8iZswg+neArPLv5+v3YUgt/r\nEUDT5m7flJkI5NWnQkRGeaRyvBko0QC3HCqeBipK+9FPHmV5DTOy2zmGC8lzmKdE\nJklPDH0ZAEb0omby6Q0lEH/qzJhr0fR5viEKhUSkoFIDUD8fvkJX3rAGvwrIvtzR\n0/k+M5bcPpQVZO/VGHXmM8xRWHDvNM6GhBTSuzthwQKBgQDVd4Vueg9N8tbteGyO\neEoEVXG17Vm4OYpsBBk1OUm+cvp6CmCQgQqlLRJGlRt/FtVEgGWkn96HjzsbMA6z\nkEp/0ov6tTbOre7YUycrXmVi66GflSaqxccgvkN1u10zqCzfIidRV0KmpNASe0nB\nCbpq90Y7/1NN6QuOrT9DGdbywwKBgQC/CWNLFyH1lvZxTa2mK4UK0YRjwvLJ6UBV\nGcTEthPyyipCxYKUJkc1j91T7JtpYIrAJn3uz/sH+pN01+nmx/0WusiBtwTtZvms\nFthC9H8r/b7GEZRikkSNR1x2MISmAMjCdOxpCyRqRa774z8NLRQ+1Rx7pXmnse2m\nyMsBvCSt4QKBgCrmiV9pknfU7RLul8qOLDnwvhiU6eoXTlVlAXfr2oE29FXgjgWc\nmXoWs8yRnOQOv6+zqjnKk1tlErjlEJ9PyVklBFLPZoNk+1Joa7/Qicm2l1XOEOZT\nNzDCbCZWEGYYT2RMpeA4DEIXb2W3d1wfS2LB7VCTgLdwtYzoDoW6xLMnAoGAKgfT\nu8qsIw+Cyyzu/rdmfxnXyeczaa8TA2Y2/5ybyPgn0icIcrX1RtiPNo7BJq8h9+LA\nJFHIBlpgJP34LVlk2qJfyQJOaDkWx4EDNb/7Vt9uIL/vaLyLrpW7xxknpipYAUie\nVwInkeYg+LRnw+teH/DdYmrm2DlycxaMa6ZMX6ECgYASdZ/fKRaknsclpLBXpMEA\nMuoSIFRHHdWszTx8XHqiJJuxiWaaSS5fsWzjX+dcPMAf8gHGrEd/Ntnt7fPDBYTD\np0htqHj9pSQRWGNKgRNlp1R4nRhe3SwyfrAF9CQOgRtt6Y4Sbp+IFbvH7P/5OKc6\nliluf2+SrDhEvWjJ7B7Ttg==\n-----END PRIVATE KEY-----\n",
  "client_email": "perfect-reserve-307816@appspot.gserviceaccount.com",
  "client_id": "117569674111822918734",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/perfect-reserve-307816%40appspot.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
try:

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('perfect-reserve-307816-bucket') ### Nome do seu bucket
  blob = bucket.blob('artist-names.csv')

  pages = []
  names = "Name \n"

  for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

  for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
      names = names + artist_name.contents[0] + "\n"

    blob.upload_from_string(names, content_type="text/csv")

except Exception as ex:
  print(ex) 
