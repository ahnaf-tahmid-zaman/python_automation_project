import requests
from bs4 import BeautifulSoup

def job_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_cards = soup.find_all('div', class_='col-md-12')

    for job_card in job_cards:
        company_name_elem = job_card.find('div', class_='comp-name-text')
        job_title_elem = job_card.find('div', class_='job-title-text')

        # Skip the iteration if either company name or job title is not found
        if not company_name_elem or not job_title_elem or not job_title_elem.a:
            continue

        company_name = company_name_elem.get_text(strip=True)
        job_title = job_title_elem.a.get_text(strip=True)

        print(f'Company name: {company_name}; Job title: {job_title}')

url_to_scrape = "https://jobs.bdjobs.com/jobsearch.asp?fcatId=8&icatId="
job_scraper(url_to_scrape)
