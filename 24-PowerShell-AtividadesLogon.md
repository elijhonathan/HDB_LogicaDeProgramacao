# no powershell

Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4624 -or $_.Id -eq 4634 } | Select-Object -Property TimeCreated, Id, Message
