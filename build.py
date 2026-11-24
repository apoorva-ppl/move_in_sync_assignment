import csv,json,pathlib
p=pathlib.Path(__file__).parent
rows=list(csv.DictReader((p/'rideops_support_tickets.csv').open()))
html=(p/'template.html').read_text().replace('/*DATA*/[]',json.dumps(rows).replace('</','<\\/'))
(p/'index.html').write_text(html)
