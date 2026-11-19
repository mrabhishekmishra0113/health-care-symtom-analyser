# AI Health Symptom Analyzer

A Flask-based health symptom analysis app with a modern medical dashboard interface.

## Run as an application

### Windows desktop launch
- Double-click `start_app.bat`
- Or run PowerShell file: `start_app.ps1`

### Manual run
```bash
python app.py
```

Then open:
- http://127.0.0.1:5000

## Features
- Symptom input with natural-language or comma-separated values
- Mild, moderate, and severe analysis
- Ranked disease suggestions
- Health dashboard with risk and summary cards
- Educational guidance and doctor recommendations
- Input is limited to 500 characters and 20 symptoms per analysis; negated symptoms are not treated as currently present.
- Reported severity is not a diagnosis, and recognized emergency warning symptoms prompt urgent-care guidance regardless of severity.

## Setup
```bash
pip install -r requirements.txt
```

## Test
```bash
python -m unittest discover -s tests -v
```

## Deploy to Vercel
1. Import this repository into Vercel.
2. Set **Root Directory** to `ai-health-symptom-analyzer`.
3. Leave the build and output settings at their defaults, then deploy. Vercel uses `vercel.json` to route requests to the Flask app and `requirements.txt` to install Flask.

## Notes
This app is meant for educational and informational purposes and is not a substitute for professional medical advice.
