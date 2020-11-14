import urllib.request,ssl # Websitesinden veri cekmek ve ssl sertifikasini es gecmek
import xml.etree.ElementTree as ET # Xml yapisini ayristirmak

# SSl sertifikasi hatalarini engellemek
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Kullanacagimiz degiskenler
URL = "https://www.tcmb.gov.tr/kurlar/today.xml"
dolar,euro = 0,0

# Websitesinden veri cekmek
body = urllib.request.urlopen(URL,context=ctx)
data = body.read().decode()

# Xml dosyasini ayristirmak
xml = ET.fromstring(data)
for currency in xml:
  for child in currency:
    if(child.tag == "ForexSelling" and currency.get("Kod") == "USD"):
      dolar = float(child.text)
    elif(child.tag == "ForexSelling" and currency.get("Kod") == "EUR"):
      euro = float(child.text)
    else:
      continue
    
print("Dolar Kuru: {} ve Euro Kuru: {}".format(dolar,euro))
