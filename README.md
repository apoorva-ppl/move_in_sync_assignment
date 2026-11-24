# RideOps Queue Control
Open `index.html` in Chrome or Safari. No install, server or internet needed. The CSV is embedded at build time.

**Refresh the snapshot:** replace `rideops_support_tickets.csv` (same schema), run `python3 build.py`, and update `CUTOFF` in `template.html` if the snapshot date changes. The build prints the headline counts as a check.

**What it does**
- Clickable KPIs (open, with engineering, ever escalated, >48h, P1, not yet reviewed) and quick filters (Roster/GPS, 2+ handoffs, returned to L1, update due), plus search, owner, priority, category and sort.
- Each ticket shows a rule-based next action, an evidence checklist, and why it was flagged (handoffs, last engineering outcome, reopens, tier).
- Review record per ticket: checks done, owner of next step, next-update due time, note. "Update due" flags overdue follow-ups.
- Weekly scorecard chart: arrivals, final closures and backlog together (Friday 23:59 IST weeks).
- Export the filtered queue as CSV for stand-up. Backup/restore reviews as JSON. Reset clears local reviews.

**Demo check:** 48 open, 19 with engineering, 34 ever escalated, 25 older than 48h, 3 P1; Roster/GPS chip shows 30. Save a review, reload, confirm it persisted, export CSV.

**Limits:** reviews live in this browser's local storage (use Backup to move them; if storage is blocked on file URLs run `python3 -m http.server 8000` and open http://localhost:8000). Reviews do not change ticket status or count as closures. No ticket-system integration or shared state. Fictional data: use privately, do not publish.
