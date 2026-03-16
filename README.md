# Atlas

An interactive globe app built as a mostly self-contained HTML file.

It currently supports:
- COBE-style rotating globe
- City search via Geoapify
- City markers with notes and photo uploads
- Local persistence in the browser
- CSV import/export for cities
- Country and city counters
- No user login

## Project Files

- [globe.html](./globe.html): main app UI and client logic
- [serve_globe.py](./serve_globe.py): tiny local server that exposes `config.js`
- `.env`: local API key config, ignored by Git

## Requirements

- Python 3
- Internet access
- A Geoapify API key

## Local Setup

Create a `.env` file in the repo root:

```env
GEOAPIFY_API_KEY=your_key_here
```

`.env` is already ignored by Git.

## Run Locally

From the repo root:

```bash
python3 serve_globe.py
```

Then open:

[http://127.0.0.1:8001/globe.html](http://127.0.0.1:8001/globe.html)

What the local server does:
- serves the static files in this folder
- injects `window.__APP_CONFIG__` at `/config.js`
- keeps the Geoapify key out of Git

## How To Use

- Click `Add New Location` to search for a city.
- Click a city marker to edit notes and upload photos.
- Use `Import CSV` to add cities from a file.
- Use `Export CSV` to download your current city list.
- Use `Remove City` in the side panel to delete a location.

Notes:
- Cities, notes, and photos currently persist in browser `localStorage`.
- Data is local to that browser/device unless you export/import it manually.

## CSV Format

The exporter writes:

```csv
city,countryCode,countryName,lat,lon
Tokyo,JP,Japan,35.6762,139.6503
```

The importer accepts that format and also tolerates common aliases like:
- `name`
- `country`
- `latitude`
- `longitude`

## GitHub Workflow

Current remote:

```bash
git remote -v
```

This repo is configured to push to:

```text
https://github.com/amadan95/atlas.git
```

### Check status

```bash
git status
```

### Commit changes

```bash
git add README.md globe.html serve_globe.py .gitignore
git commit -m "Describe your change"
```

### Push to GitHub

```bash
git push origin main
```

If GitHub prompts for credentials, use your normal GitHub auth flow:
- SSH key, if your remote uses SSH
- or HTTPS with a personal access token

## Ignored Files

The repo intentionally excludes:
- `.env`
- `.codex-tmp/`
- `__pycache__/`
- `output/`

## Troubleshooting

### The city search does not work

Check:
- `.env` exists
- `GEOAPIFY_API_KEY` is set
- you started the app with `python3 serve_globe.py`

### The app opens but looks stale

Hard refresh the browser:

- macOS: `Cmd + Shift + R`

### My data is missing

The app currently stores data in localStorage, so it is tied to the browser profile unless exported.
