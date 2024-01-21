# Postmortem

Containers have everything running under the root user by default,
which has the ability to run anything as another user. Running containers as root is a bad idea for security,
and if maybe you fat finger a command and for example run rm -rf /, there is no comeback. 

## Debugging Process

Bug debugger Brennan (BDB... as in my actual initials... made that up on the spot, pretty
good, huh?) encountered the issue upon opening the project and being, well, instructed to
address it, roughly 19:20 PST. He promptly proceeded to undergo solving the problem.

1. Checked the user privileges and if the system is running as root.
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
5. 

## Summation

In short, a typo. Gotta love'em. In full, the WordPress app was encountering a critical
error in `wp-settings.php` when tyring to load the file `class-wp-locale.phpp`. The correct
file name, located in the `wp-content` directory of the application folder, was
`class-wp-locale.php`.

Patch involved a simple fix on the typo, removing the trailing `p`.

## Prevention

This outage was not a web server error, but an application error. To prevent such outages
moving forward, please keep the following in mind.

* Test! Test test test. Test the application before deploying. This error would have arisen
and could have been addressed earlier had the app been tested.

* Status monitoring. Enable some uptime-monitoring service such as
[UptimeRobot](./https://uptimerobot.com/) to alert instantly upon outage of the website.

Note that in response to this error, I wrote a Puppet manifest
[0-strace_is_your_friend.pp](https://github.com/bdbaraban/holberton-system_engineering-devops/blob/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp)
to automate fixing of any such identitical errors should they occur in the future. The manifest
replaces any `phpp` extensions in the file `/var/www/html/wp-settings.php` with `php`.

But of course, it will never occur again, because we're programmers, and we never make
errors! :wink:
