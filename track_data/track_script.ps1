$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Output "This is what you are looking for: $scriptDir"


# StartPython.ps1
$scriptPath = Join-Path -Path $scriptDir "current_tracking_processor.py"  # Replace with your actual script path
$scriptPath_his = Join-Path -Path $scriptDir "his_tracking_processor.py"  # Replace with your actual script path
$scriptPath_parser = Join-Path -Path $scriptDir "tracking_parser_processor.py"

Write-Host "Starting Python script: $scriptPath" -ForegroundColor Green

# Explicitly call python.exe
$process = Start-Process -FilePath "python" -ArgumentList $scriptPath -NoNewWindow -PassThru

if ($process) {
    Write-Host "Scraper script script is running... (PID: $($process.Id))" -ForegroundColor Yellow
    $process | Wait-Process
    Write-Host "Scraper script has completed." -ForegroundColor Cyan
} else {
    Write-Host "Failed to start the Scraper script check log." -ForegroundColor Red
}


$process_2 = Start-Process -FilePath "python" -ArgumentList $scriptPath_his -NoNewWindow -PassThru

if ($process_2) {
    Write-Host "Scraper script is running... (PID: $($process_2.Id))" -ForegroundColor Yellow
    $process_2 | Wait-Process
    Write-Host "Scraper script has completed." -ForegroundColor Cyan
} else {
    Write-Host "Failed to start the Scraper script script log." -ForegroundColor Red
}


$process_parser = Start-Process -FilePath "python" -ArgumentList $scriptPath_parser -NoNewWindow -PassThru

if ($process_parser) {
    Write-Host "Parser script is running... (PID: $($process_parser.Id))" -ForegroundColor Yellow
    $process_parser | Wait-Process
    Write-Host "Parser script has completed." -ForegroundColor Cyan
} else {
    Write-Host "Failed to start the Parser script script log." -ForegroundColor Red
}


