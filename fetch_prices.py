# Download daily OHLCV for all HOSE common stocks (+ MCH) via vnstock (VCI source).
import os, time, pandas as pd, io, contextlib
from vnstock import Quote
out = 'data/raw'
lst = pd.read_csv('data/hose_listing_VCI_20260924.csv')
syms = sorted(set(lst.loc[lst['type'] == 'STOCK', 'symbol']) | {'MCH'})
priority = ['VCB','VIC','VHM','BID','VPB','HPG','FPT','GEX','HDB','HCM','MCH','MSN','NVL','STB','SHB','SSB','SSI',
            'TCX','VCI','VJC','VNM','MSB','VRE','VPL','VIX','VND','VCK','SAB','DXG','GEE','BSR','PLX']
syms = priority + [x for x in syms if x not in priority]
log = open('data/fetch_log.txt', 'a')
for s in syms:
    f = f'{out}/{s}.csv'
    if os.path.exists(f):
        continue
    for attempt in range(4):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                df = Quote(symbol=s, source='VCI').history(start='2024-10-01', end='2026-09-23', interval='1D')
            df.to_csv(f, index=False)
            log.write(f'{s},ok,{len(df)}\n'); log.flush()
            break
        except BaseException as e:
            msg = str(e)[:120].replace(',', ';')
            log.write(f'{s},err{attempt},{msg}\n'); log.flush()
            time.sleep(65)
    time.sleep(3.6)
print('DONE')
