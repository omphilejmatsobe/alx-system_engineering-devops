# Postmortem

Containers have everything running under the root user by default,
which has the ability to run anything as another user. Running containers as root is a bad idea for security,
and if maybe you fat finger a command and for example run rm -rf /, there is no comeback. 
## Summary

Time-down: 12-19-2023, 16:22

Duration: 2 hours

Impact: The container was left vulnerable and an attack was performed. This resulted in the NGINX server being down.

Cause: Lack of security, the container was running as root and the login credentials were weak.

##Timeline



## Debugging Process

1. Check the user privileges and if the system is running as root.
2. Make sure nginx is running as nginx user and not as the root user.
   ```
   sudo -u "$1" whoami
   sed -i "s/#user www-data/user ngnix/" /etc/nginx/nginx.conf
   ```
3. Make sure nginx is listening on all active IPs on port 8080.
   ```
   sed -i -E "s/(listen.*)80 /\18080 /g" /etc/nginx/sites-available/default
   ```
4. Configure the container to fit the above.
   ```
   chmod 644 /etc/nginx/nginx.conf
   ```
5. Clean Up
   ```
   pkill apache2
   sudo -u nginx service nginx restart
   ```
   
## Summation

In short, privilege. We love it don't we? But sometimes it might be bad for us, especially in networks
and computers. Sometimes it is okay to have fewer privileges cause it keeps us away from trouble.

## Prevention

This outage was due to an attack that could be prevented. To prevent such outages
moving forward, please keep the following in mind.

* Check! Test!
* Shy away from running as the root user a lot unless if it's required.
* Status monitoring. Enable some uptime-monitoring service such as

Now that we know it will never occur again, because we're programmers, and we never make
mistakes right ?! :wink:
