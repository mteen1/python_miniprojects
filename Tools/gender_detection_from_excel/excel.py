import json
import pandas as pd


def read_json(file):
    f = open(f'{file}', "r", encoding='utf8')
    data = json.loads(f.read())
    f.close()
    return data


male_names = read_json('male.json')
fem_names = read_json('female.json')

sheet = pd.read_excel('st_iran.xlsx')
print(sheet.columns.ravel())

x = []
for name in sheet['نام']:
    name = name.strip().split()[0]
    if name in male_names:
        x.append(1)
    elif name in fem_names:
        x.append(0)
    else:
        x.append('not found')
print(x)

df = pd.DataFrame(x)
writer = pd.ExcelWriter('out.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
