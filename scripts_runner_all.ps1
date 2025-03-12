# Launch PowerShell scripts that run Python programs
function Start-NestedScripts {
    param(
        [Parameter(Mandatory=$true)]
        [string[]]$PowerShellScripts
    )
    
    # Store processes for monitoring
    $processes = @()
    
    foreach ($script in $PowerShellScripts) {
        try {
            # Check if PowerShell script exists
            if (-not (Test-Path $script)) {
                Write-Error "PowerShell script not found: $script"
                continue
            }
            
            # Start PowerShell process with execution policy bypass for convenience
            $processInfo = Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File `"$script`"" -PassThru -NoNewWindow
            $processes += $processInfo
            Write-Host "Started PowerShell script $script with PID: $($processInfo.Id)"
        }
        catch {
            Write-Error "Failed to start $script : $_"
        }
    }
    
    return $processes
}

# Example PowerShell script content (save as run_python1.ps1):
<#
# Sample content for your PowerShell scripts:
$pythonScript = "path/to/your/python_script1.py"
$pythonProcess = Start-Process python -ArgumentList $pythonScript -PassThru -NoNewWindow
Write-Host "Started Python script $pythonScript with PID: $($pythonProcess.Id)"
#>

# Example usage:
# $processes = Start-NestedScripts -PowerShellScripts @("run_python1.ps1", "run_python2.ps1")

$processes_1 = Start-NestedScripts -PowerShellScripts @("historic_defense_data\his_defense_script.ps1")
$processes_1 | Wait-Process

$processes_2 = Start-NestedScripts -PowerShellScripts @("historic_player_data\his_player_script.ps1")
$processes_2 | Wait-Process

$processes_3 = Start-NestedScripts -PowerShellScripts @("historic_usage_data\his_usage_script.ps1")
$processes_3 | Wait-Process

#### current starts here

$processes_1 = Start-NestedScripts -PowerShellScripts @("current_defense_data\current_defense_script.ps1")
$processes_1 | Wait-Process

$processes_2 = Start-NestedScripts -PowerShellScripts @("current_player_data\current_player_script.ps1")
$processes_2 | Wait-Process

$processes_3 = Start-NestedScripts -PowerShellScripts @("current_usage_data\current_usage_script.ps1")
$processes_3 | Wait-Process

$processes_4 = Start-NestedScripts -PowerShellScripts @("schedule\schedule_script.ps1")
$processes_4 | Wait-Process

$processes_5 = Start-NestedScripts -PowerShellScripts @("track_data\track_script.ps1")
$processes_5 | Wait-Process


$processes_4 = Start-NestedScripts -PowerShellScripts @("mover.ps1")
$processes_4 | Wait-Process

Write-Host "Mover is done!"