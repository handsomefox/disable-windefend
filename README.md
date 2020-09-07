# Disable WinDefend

Disable Tamper Protection manually before running.
Run with admin rights twice to disable/enable everything.

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
