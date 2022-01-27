# Disable WinDefend

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/5/50/Windows_Defender_logo.svg">

[Reason why this exists](https://pureinfotech.com/windows-10-removes-disableantispyware-disable-defender/)

</p>

## Requirements

1. Tamper protection needs to be disabled

## Instructions

### How to disable Windows Defender

1. Disable Tamper Protection.
2. Run Disable.bat to disable Windows Defender.
3. Reboot.
4. Run it once (maybe more, thanks Microsoft) again so it can actually disable Windows Defender. Console output will say "SUCCESS" instead of "ERROR" when it actually disables it.
5. Once there's no "Antimalware Service Executable" in the Task Manager - it's disabled.
6. (Optional) Reboot once more, because sometimes Windows still manages to enable Defender by itself and you have to do everything from the start again.

### How to enable Windows Defender

1. Run Enable.bat.
2. Reboot so that Windows can start services again.
3. Open Windows Security and check all the options (Real-time protection, Tamper Protection and etc.).

## Some additional stuff you may want

### Delete Systray icon

```batchfile
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run" /v "SecurityHealth" /f
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v "SecurityHealth" /f
```

### Restore Systray icon

```batchfile
reg add "HKLM\Software\Classes\*\shellex\ContextMenuHandlers\EPP" /ve /t REG_SZ /d "{09A47860-11B0-4DA5-AFA5-26D86198A780}" /f
reg add "HKLM\Software\Classes\Drive\shellex\ContextMenuHandlers\EPP" /ve /t REG_SZ /d "{09A47860-11B0-4DA5-AFA5-26D86198A780}" /f
reg add "HKLM\Software\Classes\Directory\shellex\ContextMenuHandlers\EPP" /ve /t REG_SZ /d "{09A47860-11B0-4DA5-AFA5-26D86198A780}" /f
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
