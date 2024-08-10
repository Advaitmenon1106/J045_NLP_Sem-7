import re
import pandas as pd

def parse_dates(sentences):
    date_formats = [
        # Add your date formats here
        r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
        r'\d{2}/\d{2}/\d{4}',  # DD/MM/YYYY
        r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}'

        # ... other formats
    ]

    dates = []
    for sentence in sentences:
        for f in date_formats:
            matches = re.findall(f, sentence)
            dates.extend(matches)
    return dates


df = pd.read_csv('Lab-3/date_parser_testcases.csv')
sentences = df['Input'].tolist()
parsed = parse_dates(sentences)
parsed_final = []

for d in parsed:
    if '-' in d:
        parsed_final.append('/'.join(d.split('-')))
    else:
        parsed_final.append(d)

print(parsed_final)
