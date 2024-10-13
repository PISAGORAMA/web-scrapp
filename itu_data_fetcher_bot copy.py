from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_person(first_name, last_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://rehber.itu.edu.tr/")

    try:
        first_name_input = driver.find_element(By.NAME, "firstName")
        last_name_input = driver.find_element(By.NAME, "lastName")
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        last_name_input.submit()

        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='table table-hover search-result-table']//tbody//tr"))
        )

        results = driver.find_elements(By.XPATH, "//table[@class='table table-hover search-result-table']//tbody//tr")
        if results:
            print(f"{first_name} {last_name} için sonuçlar bulundu:")
            for result in results:
                cells = result.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 4:
                    unvan = cells[0].text
                    ad_soyad = cells[1].text
                    birim = cells[2].text
                    bolum = cells[3].text
                    print(f"Unvan: {unvan}, Ad Soyad: {ad_soyad}, Birim: {birim}, Bölüm: {bolum}")
        else:
            print(f"{first_name} {last_name} için sonuç bulunamadı.")
    except Exception as e:
        print(f"{first_name} {last_name} için sonuç bulunamadı.")
        #print(f"Bir hata oluştu: {e}")
    finally:
        driver.quit()

# Kullanım örneği
search_person("Name","Surname")

