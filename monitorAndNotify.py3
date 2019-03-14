#log current time, temperature, and humidity to a database every minute. 
#Database options: SQLite 3 or MySQL.
#Script should run at startup automatically. Use cronjob, systemd service, run on boot in background etc.

#check against the config.json for values outside range and send notification
#push notification: Push bullet - 1 notification per day. - Use databse to remeber if notification sent or NOT. 
