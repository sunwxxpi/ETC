from selenium import webdriver
from bs4 import BeautifulSoup

def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="

    browser = webdriver.Chrome()
    browser.get(f"{base_url}{keyword}")
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    pagination = soup.find('nav', {'aria-label': 'pagination'})
    pages = pagination.find_all('div', recursive=False)
    count = len(pages)
    if count == 0:
        return 1
    elif count >= 5:
        return 5
    else:
        return count - 1

def extract_indeed_jobs(keyword): 
    pages = get_page_count(keyword)    
    base_url = "https://kr.indeed.com/jobs"
    browser = webdriver.Chrome()
    
    results = []
    
    for page in range(pages):
        url_pages = page * 10
        browser.get(f"{base_url}?q={keyword}&start={url_pages}")
                
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        job_list = soup.find('ul', {'class': 'jobsearch-ResultsList'})
        jobs = job_list.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find('div', {'class': 'mosaic-zone'})
            if zone == None:
                anchor = job.select_one('h2 a')
                title = anchor['aria-label']
                link = anchor['href']

                company = job.find('span', {'class': 'companyName'})
                location = job.find('div', {'class': 'companyLocation'})
                
                print(location)

                job_data = {
                    'Link': f"https://kr.indeed.com{link}",
                    'Company': company.string.replace(',', ' '),
                    'Location': location.string.replace(',', ' '),
                    'Position': title.replace(',', ' '),
                }
                
                results.append(job_data)
                
    return results