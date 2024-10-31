import pandas as pd 
import requests
from bs4 import BeautifulSoup

import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table')
    
    headers = [header.text for header in table.find_all('th')]
    
    data = []
    
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) > 0:
            data.append({
                'Date': cols[0].text,
                'Open': cols[1].text,
                'Close': cols[4].text,
                'Volume': cols[6].text
            })
    
    df = pd.DataFrame(data)
    
    print(df)
else:
    print("No se pudo acceder a la página. Código de estado:", response.status_code)
    
