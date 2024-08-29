import time

from numpy.ma.mrecords import reserved_fields
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Ana sayfaya git
driver.get('https://scottishwildlifetrust.org.uk/things-to-do/visit-our-reserves-and-visitor-centres/?_gl=1*hsh48n*_up*MQ..*_ga*MTI0OTE2MjgwNS4xNzIwNTI3NTYw*_ga_5BH0XSGV9M*MTcyMDUyNzU2MC4xLjAuMTcyMDUyNzU2MC4wLjAuMA')

# Rezerv linklerinin olduğu tüm öğeler
reserve_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/reserve/")]')))

# Tekil rezerv URL'lerini çıkartmak için set kullan
reserve_urls = set(element.get_attribute('href') for element in reserve_elements)

# Reserve içinden istenen bilgileri çekme
reserve_data = []

# Her bir rezerv sayfasına gidip bilgileri çekme
for link in reserve_urls:
    driver.get(link)
    try:
        # Bilgileri çekme
        name = driver.find_element(By.XPATH, '//*[@id="intro-block"]/div[1]/div/div[1]/header/h2').text
        description = driver.find_element(By.XPATH, '//*[@id="intro-block"]/div[1]/div/div[1]/div/p[1]').text
        why_visit = driver.find_element(By.XPATH, '//*[@id="intro-block"]/div[1]/div/div[1]/div/ul[1]').text
        best_time = driver.find_element(By.XPATH, '//*[@id="intro-block"]/div[1]/div/div[1]/div/ul[2]').text
        visit = driver.find_element(By.XPATH, '//*[@id="intro-block"]/div[1]/div/div[1]/div/ul[3]').text
        how_to_get = driver.find_element(By.XPATH, '//*[@id="visiting-the-reserve"]/div[1]/div[1]/p[2]').text

        # Verileri listeye ekleme
        reserve_data.append({
            "Name": name,
            "Description": description,
            "Why Visit?": why_visit,
            "Best Time to Visit": best_time,
            "Visit": visit,
            "How to get there?": how_to_get
        })

    except Exception as e:
        print(f"Bilgi çekilirken bir hata oluştu: {e}")

# Sonuçları yazdırma
for data in reserve_data:
    print(f"Name: {data['Name']}\n"
          f"Description: {data['Description']}\n"
          f"Why Visit?: {data['Why Visit?']}\n"
          #f"Best Time to Visit: {data['Best Time to Visit']}\n"
          #f"Visit for: {data['Visit']}\n"
          f"How to get there?: {data['How to get there?']}\n"
          )


import json

# Veriyi JSON dosyasına kaydetme
with open('reserves.json', 'w') as json_file:
    json.dump(reserve_data, json_file, indent=4)

# Tarayıcıyı kapatma
driver.quit()

'''
# Rezerv linklerinin olduğu tüm öğeleri bul
reserve_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/reserve/")]'))
)

# Tekil rezerv URL'lerini çıkartmak için set kullan
reserve_urls = set(element.get_attribute('href') for element in reserve_elements)

# Rezerv URL'lerini yazdırma
print("Rezerv Linkleri:")
for url in reserve_urls:
    print(url)

# Tarayıcıyı kapatma
driver.quit()

'''

'''
Rezerv Linkleri:
https://scottishwildlifetrust.org.uk/reserve/carron-glen/
https://scottishwildlifetrust.org.uk/reserve/red-moss-of-netherley/
https://scottishwildlifetrust.org.uk/reserve/knowetop-lochs/
https://scottishwildlifetrust.org.uk/reserve/auchalton-meadow/
https://scottishwildlifetrust.org.uk/reserve/handa-island/
https://scottishwildlifetrust.org.uk/reserve/wallacebank-wood/
https://scottishwildlifetrust.org.uk/reserve/sourlie-wood/
https://scottishwildlifetrust.org.uk/reserve/pease-dean/
https://scottishwildlifetrust.org.uk/reserve/drummains-reedbed/
https://scottishwildlifetrust.org.uk/reserve/cumbernauld-glen/
https://scottishwildlifetrust.org.uk/reserve/perceton-wood/
https://scottishwildlifetrust.org.uk/reserve/gight-wood/
https://scottishwildlifetrust.org.uk/reserve/grey-hill-grassland/
https://scottishwildlifetrust.org.uk/reserve/feoch-meadows/
https://scottishwildlifetrust.org.uk/reserve/thornton-glen/
https://scottishwildlifetrust.org.uk/reserve/cullaloe/
https://scottishwildlifetrust.org.uk/reserve/johnston-terrace-garden/
https://scottishwildlifetrust.org.uk/reserve/hill-of-white-hamars/
https://scottishwildlifetrust.org.uk/reserve/seaton-cliffs/
https://scottishwildlifetrust.org.uk/reserve/corsehillmuir-wood/
https://scottishwildlifetrust.org.uk/reserve/loch-ardinning/
https://scottishwildlifetrust.org.uk/reserve/fountainbleau-ladypark/
https://scottishwildlifetrust.org.uk/reserve/hadfast-valley/
https://scottishwildlifetrust.org.uk/reserve/brock-wood/
https://scottishwildlifetrust.org.uk/reserve/carron-dam/
https://scottishwildlifetrust.org.uk/reserve/montrose-basin/
https://scottishwildlifetrust.org.uk/reserve/the-miley/
https://scottishwildlifetrust.org.uk/reserve/shewalton-sandpits/
https://scottishwildlifetrust.org.uk/reserve/cathkin-marsh/
https://scottishwildlifetrust.org.uk/reserve/keltneyburn/
https://scottishwildlifetrust.org.uk/reserve/red-moss-of-balerno/
https://scottishwildlifetrust.org.uk/reserve/woodhall-dean/
https://scottishwildlifetrust.org.uk/reserve/fleecefaulds-meadow/
https://scottishwildlifetrust.org.uk/reserve/milkhall-pond/
https://scottishwildlifetrust.org.uk/reserve/seafar-wood/
https://scottishwildlifetrust.org.uk/reserve/bemersyde-moss/
https://scottishwildlifetrust.org.uk/reserve/gailes-marsh/
https://scottishwildlifetrust.org.uk/reserve/loch-of-the-lowes/
https://scottishwildlifetrust.org.uk/reserve/linn-dean/
https://scottishwildlifetrust.org.uk/reserve/dalmellington-moss/
https://scottishwildlifetrust.org.uk/reserve/shian-wood/
https://scottishwildlifetrust.org.uk/reserve/bankhead-moss/
https://scottishwildlifetrust.org.uk/reserve/falls-of-clyde/
https://scottishwildlifetrust.org.uk/reserve/upper-nethan-gorge/
https://scottishwildlifetrust.org.uk/reserve/pepper-wood/
https://scottishwildlifetrust.org.uk/reserve/gordon-moss/
https://scottishwildlifetrust.org.uk/reserve/lower-nethan-gorge/
https://scottishwildlifetrust.org.uk/reserve/southwick-coast/
https://scottishwildlifetrust.org.uk/reserve/carstramon-wood/
https://scottishwildlifetrust.org.uk/reserve/glen-moss/
https://scottishwildlifetrust.org.uk/reserve/loch-of-lintrathen/
https://scottishwildlifetrust.org.uk/reserve/tummel-shingle-islands/
https://scottishwildlifetrust.org.uk/reserve/garnock-floods/
https://scottishwildlifetrust.org.uk/reserve/balnaguard-glen/
https://scottishwildlifetrust.org.uk/reserve/oldhall-ponds/
https://scottishwildlifetrust.org.uk/reserve/isle-of-eigg/
https://scottishwildlifetrust.org.uk/reserve/hermand-birchwood/
https://scottishwildlifetrust.org.uk/reserve/knockshinnoch-lagoons/
https://scottishwildlifetrust.org.uk/reserve/dumbarnie-links/
https://scottishwildlifetrust.org.uk/reserve/tailend-moss/
https://scottishwildlifetrust.org.uk/reserve/loch-libo/
https://scottishwildlifetrust.org.uk/reserve/stenhouse-wood/
https://scottishwildlifetrust.org.uk/reserve/talich/
https://scottishwildlifetrust.org.uk/reserve/belmaduthy-dam/
https://scottishwildlifetrust.org.uk/reserve/barnyards-marsh/
https://scottishwildlifetrust.org.uk/reserve/possil-marsh/
https://scottishwildlifetrust.org.uk/reserve/carsegowan-moss/
https://scottishwildlifetrust.org.uk/reserve/blackcraig-wood/
https://scottishwildlifetrust.org.uk/reserve/luggiebank-wood/
https://scottishwildlifetrust.org.uk/reserve/garrion-gill/
https://scottishwildlifetrust.org.uk/reserve/spey-bay/
https://scottishwildlifetrust.org.uk/reserve/longridge-moss/
https://scottishwildlifetrust.org.uk/reserve/linhouse-glen/
https://scottishwildlifetrust.org.uk/reserve/bawsinch-and-duddingston/
https://scottishwildlifetrust.org.uk/reserve/shewalton-wood/
https://scottishwildlifetrust.org.uk/reserve/addiewell-bing/
https://scottishwildlifetrust.org.uk/reserve/carlingnose-point/
https://scottishwildlifetrust.org.uk/reserve/ayr-gorge-woodlands/
https://scottishwildlifetrust.org.uk/reserve/erraid-wood/
https://scottishwildlifetrust.org.uk/reserve/bomains-meadow/
https://scottishwildlifetrust.org.uk/reserve/rahoy-hills/
https://scottishwildlifetrust.org.uk/reserve/lawthorn-wood/
https://scottishwildlifetrust.org.uk/reserve/petershill/
https://scottishwildlifetrust.org.uk/reserve/hare-and-dunhog-mosses/
https://scottishwildlifetrust.org.uk/reserve/west-quarry-braes/
https://scottishwildlifetrust.org.uk/reserve/whitlaw-wood/
https://scottishwildlifetrust.org.uk/reserve/hoselaw-loch-and-din-moss/
https://scottishwildlifetrust.org.uk/reserve/largiebaan/
https://scottishwildlifetrust.org.uk/reserve/balgavies-loch/
https://scottishwildlifetrust.org.uk/reserve/ben-mor-coigach/
https://scottishwildlifetrust.org.uk/reserve/forest-wood/
https://scottishwildlifetrust.org.uk/reserve/ballachuan-hazel-wood/
https://scottishwildlifetrust.org.uk/reserve/longhaven-cliffs/
https://scottishwildlifetrust.org.uk/reserve/cambus-pools/
https://scottishwildlifetrust.org.uk/reserve/roslin-glen/
'''