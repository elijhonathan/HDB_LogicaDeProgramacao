# no power shell

Get-Process | Where-Object { $_.Path -eq $null -and $_.Handles -gt 500 -and $_.CPU -gt 50 }
