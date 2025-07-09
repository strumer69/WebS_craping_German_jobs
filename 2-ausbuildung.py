import requests
from bs4 import BeautifulSoup

# URL for job listings on Kleinanzeigen
url = 'https://www.kleinanzeigen.de/s-jobs/c102'

# Send request and parse HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Look for all job titles or listings containing 'Ausbildung'
job_listings = soup.find_all('li', class_='ad-listitem')

# Count how many contain the word "Ausbildung"
ausbildung_count = 0
for job in job_listings:
    title = job.get_text().lower()
    if 'ausbildung' in title:
        ausbildung_count += 1

print(f"Number of 'Ausbildung' jobs found: {ausbildung_count}")
