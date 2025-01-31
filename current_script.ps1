# # Ensure the ThreadJob module is installed
# if (-not (Get-Module -ListAvailable -Name ThreadJob)) {
#     Install-Module -Name ThreadJob -Scope CurrentUser -Force
# }

# Import-Module ThreadJob

# # Define the script paths
# $script1 = "current_defense_data/test.py"
# $script2 = "current_defense_data/test.py"
# $script3 = "current_defense_data/test.py"
# $script4 = "current_defense_data/test.py"

# # Start parallel execution using ThreadJobs
# $jobs = @(
#     Start-ThreadJob -ScriptBlock { & $using:script1 }
#     Start-ThreadJob -ScriptBlock { & $using:script2 }
#     Start-ThreadJob -ScriptBlock { & $using:script3 }
#     Start-ThreadJob -ScriptBlock { & $using:script4 }
# )

# # Wait for all jobs to complete
# $jobs | Wait-Job

# # Retrieve job results (optional)
# $jobs | Receive-Job

# StartPython.ps1
$scriptPath = "current_defense_data/current_defense_scraper_processor.py"  # Replace with your actual script path
$scriptPath_parser = "current_defense_data/current_defense_parser_processor.py"

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

