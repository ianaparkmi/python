import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import re
import argparse
import sys

def read_countries(filename):
    try: 
        with open(filename, 'r', encoding='utf-8') as file:
            countries=[line.strip() for line in file if line.strip() ]
            return countries
    except FileNotFoundError:
        print(f"Error: file {filename} not found")
        return []
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []
    
def save_to_csv(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer=csv.DictWriter(file, fieldnames=['country', 'city','area', 'population'])
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"Data saved in {filename}")
    except Exception as e:
        print(f"Error while saving to CSV: {e}")

def setup_argparse():
    parser=argparse.ArgumentParser(description='Wikipedia country information parser')
    parser.add_argument('--input', '-i', default='countries.txt',
    help='Input file with countries list')
    parser.add_argument('--output', '-o', default='countries_data.csv',
    help='Output CSV file')
    return parser.parse_args()

class CountryParser:
    def __init__(self,cache_dir='cache'):
        self.session=requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.cache_dir=cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def get_page(self, country):
        cache_file = os.path.join(self.cache_dir, f"{country.replace(' ', '_')}.html")
        if os.path.exists(cache_file):
            print(f"  [cache] {country}")
            with open(cache_file, 'r', encoding='utf-8') as f:
                return f.read()
        url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
        try:
            response=self.session.get(url)
            response.raise_for_status()
            with open(cache_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            return response.text
        except requests.RequestException as e:
            print(f"Error loading page for {country}: {e}")
            return None
        
    def parse_country_info(self, country):
        html=self.get_page(country)
        if not html:
            return None
        soup = BeautifulSoup(html, 'lxml')
        data = {
            'country': country,
            'city': self._parse_capital(soup),
            'area': self._parse_area(soup),
            'population': self._parse_population(soup)
        }
        return data
    
    def _parse_capital(self, soup):
        try:
            capital_labels = ['Capital', 'Capitaland largest city', 'Official capital']
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                for label in capital_labels:
                    capital_th = infobox.find('th', string=re.compile('Capital', re.I))
                    if capital_th:
                        capital_td = capital_th.find_next('td')
                        if capital_td:
                            capital_link = capital_td.find('a')
                            if capital_link:
                                return capital_link.get_text().strip()
            return "Not found"
        except Exception:
            return "Error"
        
    def _parse_area(self, soup):
        try:
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                area_th = infobox.find('th', string=re.compile('Area', re.I))
                if area_th:
                    area_td = area_th.find_next('td')
                    if area_td:
                        for sup in area_td.find_all('sup'):
                            sup.decompose()
                        area_text = area_td.get_text()
                        area_match = re.search(r'(\d[\d,\.]*)', area_text)
                        if area_match:
                            area = re.sub(r'[^\d]', '', area_match.group(1))
                            return area
            return "Not found"
        except Exception:
            return "Error"

    def _parse_population(self, soup):
        try:
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                pop_labels = ['Population', 'Population estimate', 'Pop.\nestimate']
                population_th = infobox.find('th', string=re.compile('Population', re.I))
                if population_th:
                    population_td = population_th.find_next('td')
                    if population_td:
                        for sup in population_td.find_all('sup'):
                            sup.decompose()
                        population_text = population_td.get_text()
                        numbers = re.findall(r'(\d{1,3}(?:,\d{3})*)', population_text)
                        if numbers:
                            populations = [int(n.replace(',', '')) for n in numbers]
                            return str(max(populations))
            return "Not found"
        except Exception:
            return "Error"


def main():
    args = setup_argparse()
    input_file = args.input
    output_file = args.output
    countries = read_countries(input_file)  
    if not countries:
        print("Could not read the list of countries")
        return
    print(f"Found countries: {len(countries)}")
    parser = CountryParser()
    results = []
    for i, country in enumerate(countries, 1):
        print(f"[{i}/{len(countries)}] {country}")
        data = parser.parse_country_info(country)
        if data:
            results.append(data)
            print(f" {data['city']} | {data['area']} km² | {data['population']} чел.")
        else:
            print(f"  error")
        if i < len(countries):
            time.sleep(1)
    if results:
        save_to_csv(results, output_file)
        print(f"Success: {len(results)} of {len(countries)} countries")
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    main()