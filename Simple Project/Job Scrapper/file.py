from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

def save_to_file(file_name, jobs):
    file = open(f'./Simple Project/Job Scrapper/{file_name}.csv', 'w', encoding='utf-8-sig')
    
    file.write('Position, Company, Location, URL\n')
    for job in jobs:
        file.write(f"{job['Position']}, {job['Company']}, {job['Location']}, {job['Link']}\n")

    file.close()
    
if __name__ == '__main__':
    keyword = input("What do you want to search for?")

    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr

    save_to_file(keyword, jobs)