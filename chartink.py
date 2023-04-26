from glob import glob
import pandas as pd
from datetime import datetime


def set_to_tv(s, outfile):
    s = {"NSE:" + x.replace("&", "_").replace("-", "_") for x in s}
    tv_string = ",".join(list(s))
    with open(outfile, "w") as text_file:
        text_file.write(tv_string)
    print(outfile)


today_ = datetime.today().strftime("%Y%m%d")

while True:
    fname = input("Please Enter Filename:")
    fname = f"{fname}.xlsx"
    if fname in glob('*.xlsx'):
        break
    else:
        print('File not present in folder, please try again!')

df = pd.read_excel(fname)

tickers = set(df["Unnamed: 2"])

bands_url = 'https://archives.nseindia.com/content/equities/sec_list.csv'
bands_data = pd.read_csv(bands_url)

ignore_filters = ['2', '5']
filtered_stocks = bands_data.loc[~bands_data['Band'].isin(ignore_filters)]
filtered_set = set(filtered_stocks['Symbol'])

tickers = tickers.intersection(filtered_set)
print(len(tickers))
set_to_tv(tickers, f"{today_}_{fname.replace('xlsx', 'txt')}")
