from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="

    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website.")
    else:
        results = []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('section', {'class': 'jobs'})
        
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href'] # 속성 값을 dictionary를 이용하여 return 가능
                
                company, _, region = anchor.find_all('span', {'class': 'company'})
                title = anchor.find('span', {'class': 'title'}) # not return list
                
                job_data = {
                    'Link': f"https://weworkremotely.com{link}",
                    'Company': company.string.replace(',', ' '),
                    'Location': region.string.replace(',', ' '),
                    'Position': title.string.replace(',', ' ')
                }
                
                results.append(job_data)
                    
        return results