1)

#Complex direct scrapping sidelined

driver = webdriver.Chrome()
driver.get(url)

count = 0

while True:
    try:
        time.sleep(30)

        page = driver.page_source
        soup = BeautifulSoup(page,'lxml')

        main_table = soup.find('table',id="underlyingTableUnderlyingList").find_all("tr")
        for val in main_table:
            nifty_list.append(val.find_all("a",href=True).text)
        
        break

    except(AttributeError,InvalidSessionIdException) :
        if count<=2:
            driver.refresh()
            count +=1

        elif count == 3:
            driver.close()
            driver.get(url)

        else:
            driver.close()
        
        print("Issue lies elsewhere")
        

driver.close()



2)

#Csv conversion (Backup)
for name in company_names:
url = "https://finance.yahoo.com/quote/"+name+".NS/history/"
headers = ["Dates","Open","High","Low","Close","Adj Close","Volume"]

folder_path = "Stocks_Data"
os.makedirs(folder_path,exist_ok=True)

file_name = "Reliance_Data.csv"
csv_file_path = os.path.join(folder_path,file_name)

driver = webdriver.Chrome()
driver.get(url)
time.sleep(15)

page = driver.page_source
soup = BeautifulSoup(page,'lxml')

values = soup.find("tbody").find_all("tr")

with open(csv_file_path,"w",newline="",encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for val in values :
        csv_list = []
        elems = val.find_all("td")

        for i,elem in enumerate(elems) :
            csv_list.append(elem.text.strip())

        if csv_list :
            writer.writerow(csv_list)
            
driver.quit()

3)

#Download Proxies list


folder_path = "NSE_Folder"
os.makedirs(folder_path,exist_ok=True)

file_name = "Free_Proxy_List.html"
Store_path = os.path.join(folder_path,file_name)

driver = webdriver.Chrome()
driver.get("https://geonode.com/free-proxy-list")

time.sleep(5)

try:
    accept_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Accept all cookies"]'))
    )
    print("Button clicked!!")
except:
    print("Button not found!!")

accept_button.click()
time.sleep(3)

html = driver.page_source
with open(Store_path,'w',encoding='utf-8') as file:
    file.write(html)

driver.quit()


4)

#Scrapping the list and getting our proxies

with open('Free_Proxy_List.html','r',encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content,'lxml')

proxie_values = soup.find("tbody").find_all("td")
pattern_1 = re.compile(r'(\d{1,4}.\d{1,4}.\d{1,4}.\d{1,4})')
pattern_2 = re.compile(r'[^.\w]([\d]{2,5})[^.\w]')

for val in proxie_values:
    if re.match(pattern_1, val.text) :
        ip_list.append(val.text)
        print("Match 1 found!!")

    elif str.isdigit(val.text) :
        port_list.append(val.text)
        print("Match 2 found !!")

    else:
        continue

for i,val in enumerate(port_list):
    ip_list[i] = "http://"+ip_list[i] +":"+ val

5)

#Testing Proxies 


def check_proxies():

    for val in ip_list:
        proxy = val
        try: 
            res = requests.get("https://httpbin.org/ip",proxies={"http": proxy, "https": proxy},timeout=10)
            print("proxy is working")

            if res.status_code == 200:
                print(f"Proxy{proxy} is working: {res.json()}")
            else:
                print(f"Proxy{proxy} failed with status: {res.json()}")
        except Exception as e:
            print(f"proxy failure: {e}")

check_proxies()

6)

#To find missing data and store it

folder_name = "C:\\Users\\Shiva\\Videos\\Jonathan_1\\Scrapping\\Stocks_html_files"
missing_names = []

for name in company_names:

    check_link = name + "_Data.html"
    
    if check_link in os.listdir(folder_name):
        print("It's here")
    
    else:
        missing_names.append(name)


for name in missing_names:

        url = "https://finance.yahoo.com/quote/"+name+".NS/history/"

        folder_path = "Stocks_html_files"
        os.makedirs(folder_path,exist_ok=True)

        file_name = name + "_Data.html"
        html_file_path = os.path.join(folder_path,file_name)

        count = 0
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(7)

        
        while True :
            try:
                page = driver.page_source

                with open(html_file_path,"w",newline="",encoding='utf-8') as file:
                    file.write(page)
                    
                print("No : "+ str(i) + " " + name + "html download succesful !!")
                break
                    
            except Exception as e:
                count+=1
                if count <=1 :
                    driver.refresh()
                elif count == 2:
                    driver.close()
                    driver = webdriver.Chrome()
                    driver.get(url)
                    time.sleep(7)
                else:
                    print("No : "+ str(i) + " " + name + " html download failed !!")
                    break

        
        driver.close()

driver.quit()

7)

# Scraping data and Csv conversion


for i,name in enumerate(company_names):
        
    if i > 59 :

        url = "https://finance.yahoo.com/quote/"+name+".NS/history/"
        headers = ["Dates","Open","High","Low","Close","Adj Close","Volume"]

        folder_path = "Stocks_Data"
        os.makedirs(folder_path,exist_ok=True)

        file_name = name+"_Data.csv"
        csv_file_path = os.path.join(folder_path,file_name)

        count = 0
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(7)

        
        while True :
            try:
                page = driver.page_source
                soup = BeautifulSoup(page,'lxml')

                values = soup.find("tbody").find_all("tr")

                with open(csv_file_path,"w",newline="",encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)

                    for val in values :
                        csv_list = []
                        elems = val.find_all("td")

                        for i,elem in enumerate(elems) :
                            csv_list.append(elem.text.strip())

                        if csv_list :
                            writer.writerow(csv_list)
                    
                print("No : "+ str(i) + " " + name + "data scrape succesful !!")
                break
                    
            except Exception as e:
                count+=1
                if count <=1 :
                    driver.refresh()
                elif count == 2:
                    driver.close()
                    driver = webdriver.Chrome()
                    driver.get(url)
                    time.sleep(7)
                else:
                    print("No : "+ str(i) + " " + name + " data scrape failed !!")
                    break

        
        driver.quit()

    else:
        print("No : "+ str(i) + " " + name+" data already exists !!")
        continue


8)
# Downloading html data
def html_data_download():
    for i,name in enumerate(company_names):
        if i > 185 :
            url = "https://finance.yahoo.com/quote/"+name+".NS/history/"

            folder_path = "Stocks_html_files"
            os.makedirs(folder_path,exist_ok=True)

            file_name = name + "_Data.html"
            html_file_path = os.path.join(folder_path,file_name)

            count = 0
            driver = webdriver.Chrome()
            driver.get(url)
            time.sleep(7)

            
            while True :
                try:
                    page = driver.page_source

                    with open(html_file_path,"w",newline="",encoding='utf-8') as file:
                        file.write(page)
                        
                    print("No : "+ str(i) + " " + name + "html download succesful !!")
                    break
                        
                except Exception as e:
                    count+=1
                    if count <=1 :
                        driver.refresh()
                    elif count == 2:
                        driver.close()
                        driver = webdriver.Chrome()
                        driver.get(url)
                        time.sleep(7)
                    else:
                        print("No : "+ str(i) + " " + name + " html download failed !!")
                        break

            
            driver.close()

        else :
            print("No : "+ str(i) + " " + name + " html already exists !!")
            continue

        driver.quit()
    print("Company data downloaded and done")

9)

#  Scraping the data from html files without considering that already exists 

def stock_data_scrape(company_names):
    headers = ["Dates","Open","High","Low","Close","Adj Close","Volume"]

    for name in company_names:
        
        html_name = name + "_Data.html"
        csv_name = name + "_Data.csv"

        html_folder_name = "Stocks_html_files"
        csv_folder_name = "Stocks_Data"

        html_file_path = os.path.join(html_folder_name,html_name)
        csv_file_path = os.path.join(csv_folder_name,csv_name)

        if  csv_name in os.listdir("Stocks_Data") :

            print(name + " already exist's")
        
        else:
            with open(html_file_path,'r',encoding='utf-8') as file:
                page = file.read()

            with open(csv_file_path,'w',newline="",encoding="utf-8") as file :
                writer = csv.writer(file)

                soup = BeautifulSoup(page,'lxml')

                values = soup.find("tbody").find_all("tr")
                writer.writerow(headers)

                for val in values :
                    csv_list = []
                    elems = val.find_all("td")

                    for i,elem in enumerate(elems) :
                        csv_list.append(elem.text.strip())

                    if csv_list :
                        writer.writerow(csv_list)
            print(name + " created ")

    print("Stock data scraped and done") 
