import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# keyword in search: developer
url = 'https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=desarrollador&segmentId=&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&countryIds=17&sinceDate=ANY'

page = requests.get(url, headers=headers)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    print(page.status_code)
else: print(page.status_code)

job_item_class = "ij-List-item"

jobs = soup.find(job_item_class)
print(jobs)


