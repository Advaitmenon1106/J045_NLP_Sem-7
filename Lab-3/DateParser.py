import re
import pandas as pd

def parse_dates(sentences):
    date_formats = [
        r'\d{4}-\d{2}-\d{2}',
        r'\d{2}/\d{2}/\d{4}',
        r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}'
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
parsed_mid = []

for d in parsed:
    if '-' in d:
        parsed_mid.append('/'.join(d.split('-')))
    else:
        parsed_mid.append(d)

parsed_final = []

for d in parsed_mid:
    if '/' in d:
        d = d.split('/')
        for val in d:
            if int(d[1])>int(d[2]):
                temp = d[1]
                d[1] = d[2]
                d[2] = temp
            parsed_final.append('/'.join(d))
            
    else:
        parsed_final.append(d)

print(parsed_final)
print(df['Expected Output'].tolist())