tell application "Calendar"
    set todayEvents to summary of events of calendar "Work" whose start date ≥ (current date) and start date < ((current date) + 1 * days)
end tell
return todayEvents
