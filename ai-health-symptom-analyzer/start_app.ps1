$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectPath

if (Test-Path ".\.venv\Scripts\python.exe") {
    & ".\.venv\Scripts\python.exe" app.py
} else {
    python app.py
}
