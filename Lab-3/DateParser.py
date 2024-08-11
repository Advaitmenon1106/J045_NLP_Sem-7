import re
import pandas as pd

def parse_dates(sentences):
    date_formats = [
        r'(\d{1,2})\W+(\d{1,2})\W+(\d{4})',
        r'(\d{4})\W+(\d{1,2})\W+(\d{1,2})',
        r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}'
    ]

    dates = []
    for sentence in sentences:
        for f in date_formats:
            matches = re.findall(f, sentence)
            # print(matches)
            if len(matches) != 0: 
                dates.extend(matches)
    return dates


df = pd.read_csv('Lab-3/date_parser_testcases.csv')
sentences = df['Input'].tolist()
parsed = parse_dates(sentences)

parsed_final = []

# for d in parsed:
#     if '/' in d:
#         d = d.split('/')
#         for val in d:
#             if int(d[1])>int(d[2]):
#                 d[1], d[2] = d[2], d[1]
#             parsed_final.append('/'.join(d))
            
#     else:
#         parsed_final.append(d)

print(parsed)



print(len(parsed_final))


# for i in range(0, 95):
#     if df['Expected Output'].iloc[i] == parsed_final[i]:
#         c+=1

# print(c)
