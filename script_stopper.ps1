if ($global:processes) {
    foreach ($proc in $global:processes) {
        Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
    }
    Write-Host "Stopped all nested scripts."
}
