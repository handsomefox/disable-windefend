# Disable WinDefend

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/5/50/Windows_Defender_logo.svg">

[Reason why this exists](https://pureinfotech.com/windows-10-removes-disableantispyware-disable-defender/)

</p>

## Requirements

1. Python

## Instructions

1. You may need to disable Tamper Protection.
2. Run Disable.bat/Enable.bat to disable/enable Windows Defender.
3. (Optional) If you don't want to use Python, you can run files in "bat" folder manually (disable needs to be ran twice).

## Some additional stuff you may want

### Delete Systray icon

```batchfile
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run" /v "SecurityHealth" /f
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v "SecurityHealth" /f
```

### Delete Context menu entries

```batchfile
reg delete "HKCR\*\shellex\ContextMenuHandlers\EPP" /f
reg delete "HKCR\Directory\shellex\ContextMenuHandlers\EPP" /f
reg delete "HKCR\Drive\shellex\ContextMenuHandlers\EPP" /f
```

### Disable System Guard Runtime Monitor Broker

```batchfile
reg add "HKLM\System\CurrentControlSet\Services\SgrmBroker" /v "Start" /t REG_DWORD /d "4" /f
```

### Disable Windows Defender Security Center

```batchfile
reg add "HKLM\System\CurrentControlSet\Services\SecurityHealthService" /v "Start" /t REG_DWORD /d "4" /f
```
