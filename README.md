# RideOps Queue Control

A lightweight, browser-based dashboard for managing and monitoring operational ticket queues. No installation, backend, or internet connection is required.

## Getting Started
Open `index.html` in Chrome or Safari to launch the dashboard. The supplied CSV dataset is embedded at build time. To refresh the dashboard with an updated snapshot, replace the CSV with a file following the same schema and run:

```bash
python3 build.py
```

Update the snapshot cutoff date in `template.html` if required.

## Demo Walkthrough
1. Explore the 48 open tickets in the queue.
2. Filter tickets by Engineering or P1 priority.
3. Search for a specific ticket and review its recommended action.
4. Record verification checks, assign an owner, and set the next update.
5. Save your changes and reload the dashboard to verify persistence.
6. Export the currently filtered queue for further review.

## Data & Persistence
- Operational notes are saved locally in the browser.
- Reloading the dashboard preserves saved notes.
- Reset clears locally recorded notes.
- Notes do not modify the original ticket status or affect the source ticket count.
- Local storage may be restricted when opening files directly. If persistence does not work, run the following command from the project directory:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Limitations & Data Privacy
This is a standalone demonstration tool with no integration to a live ticket management system. All data and notes remain within the browser environment. The case dataset is intended for private use and must not be published or shared publicly.
