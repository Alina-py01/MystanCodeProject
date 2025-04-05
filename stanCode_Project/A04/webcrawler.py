"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # ----- Write your code below this line ----- #

        # Find the table with class 't-stripe', which contains the name data
        table = soup.find('table', class_='t-stripe')
        tbody = table.find('tbody')  # Locate the <tbody> element within the table
        rows = tbody.find_all('tr')  # Get all <tr> (table row) elements
        # Initialize counters for total male and female name counts
        male_total = 0
        female_total = 0
        # Loop through each row in the table
        for row in rows:
            cols = row.find_all('td')  # Get all <td> (table data) elements in the row
            # Ensure the row contains at least 5 columns, otherwise skip it
            if len(cols) < 5:
                continue
                # Extract the male and female name counts from the table columns
            male_number = int(cols[2].text.replace(',', ''))  # Convert male count to integer (remove commas)
            female_number = int(cols[4].text.replace(',', ''))  # Convert female count to integer (remove commas)
            # Accumulate the total counts for male and female names
            male_total += male_number
            female_total += female_number
        # Print the total counts of male and female names for the current decade
        print(f"Male Number: {male_total}")
        print(f"Female Number: {female_total}")


if __name__ == '__main__':
    main()
