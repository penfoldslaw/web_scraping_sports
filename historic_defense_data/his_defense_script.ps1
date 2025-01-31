# StartPython.ps1
$scriptPath = "his_defense_scraper_processor.py"  # Replace with your actual script path
$scriptPath_parser = "his_defense_parser_processor.py"

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


$process_parser = Start-Process -FilePath "python" -ArgumentList $scriptPath_parser -NoNewWindow -PassThru

if ($process_parser) {
    Write-Host "Parser script is running... (PID: $($process_parser.Id))" -ForegroundColor Yellow
    $process_parser | Wait-Process
    Write-Host "Parser script has completed." -ForegroundColor Cyan
} else {
    Write-Host "Failed to start the Parser script script log." -ForegroundColor Red
}
