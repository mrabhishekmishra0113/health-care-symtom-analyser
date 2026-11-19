$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectPath

Write-Host "Starting AI Health Symptom Analyzer..." -ForegroundColor Cyan

# Open browser after 2 seconds in a background job
Start-Job -ScriptBlock {
    Start-Sleep -Seconds 2
    Start-Process "http://127.0.0.1:5000"
} | Out-Null

if (Test-Path ".\.venv\Scripts\python.exe") {
    & ".\.venv\Scripts\python.exe" app.py
} elseif (Test-Path "..\.venv\Scripts\python.exe") {
    & "..\.venv\Scripts\python.exe" app.py
} else {
    python app.py
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[ERROR] App failed to start. Check if Python and Flask are installed." -ForegroundColor Red
    Read-Host "Press Enter to exit"
}