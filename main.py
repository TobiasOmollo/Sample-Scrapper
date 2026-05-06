from bs4 import BeautifulSoup, Tag
import requests
import time

def find_jobs():
    unfamiliar_skill = input('>')
    print(f'Filtering out {unfamiliar_skill}')
    html_text = requests.get('https://www.fuzu.com/kenya').text
    soup = BeautifulSoup(html_text, 'html.parser')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.find('span', class_='srp-skills').text.replace(' ', '')
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:

                    f.write(f"Company Name: {company_name.strip()}")
                    f.write(f"Required Skills :{skills.strip()}")
                    f.write(f'More Info: {more_info}')
                print(f'File saved: {index}')
    
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
        
    
    #print(soup.prettify())
    #tags = soup.find('p')
    
