import numpy as np
import pandas as pd
import seaborn as sns
import requests

year = 2012
season = 'spring'
seasons = ['spring', 'summer', 'autumn', 'winter']
tables = []
while year <= 2023:
    for season in seasons:
        print(season + ' ' + str(year))
        if year == 2023 and (season == 'autumn' or season == 'summer' or season == 'winter'):
            continue
        if year == 2021 and season == 'winter':
            url = requests.get(
                'https://www.best.eu.org/courses/list.jsp?season=BEST%20Online%20Courses')
            season = season + ' ONLINE'
        else:
            url = requests.get(
                'https://www.best.eu.org/courses/list.jsp?season=' + season + str(year % 100))
        table = pd.read_html(url.text)[0]
        table['Season'] = season
        table['Category'] = ''
        table['Applicants'] = ''
        # tables.append(table)
        name = season + '_' + str(year)
        with pd.ExcelWriter('research.xlsx', engine="openpyxl", mode='a') as writer:
            table.to_excel(writer, sheet_name=name)
    year = year + 1
