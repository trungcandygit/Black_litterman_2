import csv, math
R='output/revision/'
def rd(f): return list(csv.DictReader(open(R+f)))
def star(p):
    p=float(p); return '***' if p<0.001 else '**' if p<0.01 else '*' if p<0.05 else ''
def fmt(est,se,p,d=3):
    return f"{float(est):.{d}f}{star(p)} ({float(se):.{d}f})"
def get(rows, spec, term):
    for r in rows:
        if r['spec']==spec and r['term']==term: return r
    raise KeyError(spec+term)
out=[]
t2=rd('t2_baseline_clean.csv')
lab={'P1':'Constituent × Announcement','P2':'Constituent × Confirmation','P3':'Constituent × List and rebalancing'}
out.append("TABLE2")
for k in ['P1','P2','P3']:
    cells=[]
    for s in ['clean','matched']:
        for y,d in [('lamihud',3),('lval',3),('cs',4)]:
            r=get(t2,f'{s}_{y}',f'treated:{k}'); cells.append(fmt(r['est'],r['se'],r['p'],d))
    out.append(f"| {lab[k]} | "+" | ".join(cells)+" |")
out.append(f"| Observations | "+" | ".join([f"{int(get(t2,'clean_lamihud','treated:P1')['n']):,}"]*3+[f"{int(get(t2,'matched_lamihud','treated:P1')['n']):,}"]*3)+" |")
ti=rd('t_itt.csv'); out.append("TABLE3")
rowsdef=[('ITT: preliminary list (27), all other stocks as controls','itt_all','itt'),
         ('ITT: preliminary list (27), never-named, never-included controls','itt_pure','itt'),
         ('Predicted constituents: top 27 by pre-period trading value','pred','pred')]
for name,spec,v in rowsdef:
    c=[fmt(get(ti,f'{spec}_lamihud',f'{v}:P{k}')['est'],get(ti,f'{spec}_lamihud',f'{v}:P{k}')['se'],get(ti,f'{spec}_lamihud',f'{v}:P{k}')['p']) for k in (1,2,3)]
    c+= [fmt(get(ti,f'{spec}_lval',f'{v}:P3')['est'],get(ti,f'{spec}_lval',f'{v}:P3')['se'],get(ti,f'{spec}_lval',f'{v}:P3')['p'])]
    out.append(f"| {name} | "+" | ".join(c)+f" | {int(get(ti,f'{spec}_lamihud',f'{v}:P1')['n']):,} |")
for name,v in [('  of which later included','in'),('  of which not included','out')]:
    c=[]
    for k in (1,2,3):
        term = f'itt_in:P{k}' if v=='in' else f'P{k}:itt_out'
        r=get(ti,'itt_split_lamihud',term); c.append(fmt(r['est'],r['se'],r['p']))
    out.append(f"| {name} | "+" | ".join(c)+f" |  | {int(r['n']):,} |")
ca=rd('t3_car_portfolio.csv'); out.append("TABLE4A")
evs=['Announcement','Confirmation','Constituent list','Effective date']
for e in evs:
    for w in ['[-1,1]','[-1,5]','[0,20]']:
        rs={r['benchmark']:r for r in ca if r['group']=='constituent' and r['event']==e and r['window']==w}
        if not rs: continue
        cells=[f"{100*float(rs[b]['car']):.1f}% ({float(rs[b]['t_portfolio']):.2f})" for b in ['ew','matched','topsize','market_model']]
        out.append(f"| {e if w=='[-1,1]' else ''} | {w} | "+" | ".join(cells)+f" | {float(rs['ew']['t_cross']):.2f} |")
out.append("TABLE4B")
for e in evs:
    for w in ['[-1,1]','[-1,5]','[0,20]']:
        rs={(r['group'],r['benchmark']):r for r in ca if r['event']==e and r['window']==w}
        if ('itt_nov_list','ew') not in rs: continue
        cells=[f"{100*float(rs[(g,b)]['car']):.1f}% ({float(rs[(g,b)]['t_portfolio']):.2f})" for g in ['itt_nov_list','named_excluded'] for b in ['ew','topsize']]
        out.append(f"| {e if w=='[-1,1]' else ''} | {w} | "+" | ".join(cells)+" |")
t7=rd('t7_robustness.csv'); out.append("TABLE8")
for name,spec in [('Size-tercile × week FE','size_week_fe'),('Two-way clustering (stock and week)','twoway'),('Excluding Vingroup-family stocks','drop_vin'),('Constituent-specific linear trend','trend'),('Matched sample with constituent-specific trend','matched_trend'),('Excluding July to August 2025 from the pre-period','drop_julaug2025'),('Controlling for volatility','vol_control')]:
    c=[fmt(get(t7,spec,f'treated:P{k}')['est'],get(t7,spec,f'treated:P{k}')['se'],get(t7,spec,f'treated:P{k}')['p']) for k in (1,2,3)]
    out.append(f"| {name} | "+" | ".join(c)+f" | {int(get(t7,spec,'treated:P1')['n']):,} |")
r=get(t7,'placebo','treated:fake'); out.append(f"| Placebo: fake event on 7 April 2025 (pre-period only) | {fmt(r['est'],r['se'],r['p'])} | | | {int(r['n']):,} |")
out.append("TABLE9C")
for r in rd('t8c_named_by_stock.csv'):
    out.append(f"| {r['symbol']} | {r['first_named']} | {float(r['W1']):.2f} | {float(r['W2']):.2f} | {float(r['W3']):.2f} |")
open('ars/stage4_revise/tables_generated.md','w').write("\n".join(out)); print("\n".join(out))
