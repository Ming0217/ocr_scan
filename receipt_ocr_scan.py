import easyocr
import os
import re
import pandas as pd

receipts = os.path.join(os.getcwd(),"receipts")

date_filter = re.compile(".*(19|20)\d{2}")

amount_filter = re.compile("total")

ocr = easyocr.Reader(['en','la'],gpu=False)

data = []

for receipt in os.listdir(receipts):
    content = ocr.readtext(f'{receipts}/{receipt}',detail=0)
    content_lower = [x.lower() for x in content]
    date = list(filter(date_filter.match, content))[0]
    amount_index = content_lower.index(list(filter(amount_filter.match, content_lower))[0]) + 1
    amount = content_lower[amount_index]
    data.append([date,amount])

df = pd.DataFrame(data,columns=["date","amount"])

print(df)