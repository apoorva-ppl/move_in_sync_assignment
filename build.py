import csv, json, pathlib, sys
p = pathlib.Path(__file__).parent
rows = list(csv.DictReader((p / 'rideops_support_tickets.csv').open(encoding='utf-8')))
tpl = (p / 'template.html').read_text(encoding='utf-8')
assert '/*DATA*/[]' in tpl, 'template.html is missing the /*DATA*/[] placeholder'
keep = ['ticket_id','created_at','channel','client_name','client_tier','category','priority','description',
        'assigned_agent','escalated_to_eng','eng_handoffs','eng_outcome','status','final_closed_at','reopen_count']
slim = [{k: r[k] for k in keep} for r in rows]   # drops unused columns (smaller file, less data to leak)
html = tpl.replace('/*DATA*/[]', json.dumps(slim, separators=(',', ':')).replace('</', '<\\/'))
(p / 'index.html').write_text(html, encoding='utf-8')
o = [r for r in rows if not r['final_closed_at']]
print(f"{len(rows)} tickets | open {len(o)} | with engineering {sum('Engineering' in r['status'] for r in o)} | "
      f"ever escalated {sum(r['escalated_to_eng']=='Yes' for r in o)} | P1 {sum(r['priority']=='P1' for r in o)}")
print('wrote', p / 'index.html', f"({(p/'index.html').stat().st_size//1024} KB)")
