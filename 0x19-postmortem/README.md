# Apache Server Postmortem: When "phpp" Tried to Sneak into Our PHP Party

This postmortem details an Apache server issue that caused a nasty 500 error. We'll delve into the culprit, the debugging journey (with a few dead ends!), and the steps we're taking to prevent future mishaps. 

## Issue Summary (Exec Summary for the Busy Bee) 

**Duration:**  Thursday, 2024-04-04, 10:00 AM PST - Thursday, 2024-04-04, 12:30 PM PST (2.5 hours)

**Impact:** Our website users encountered a dreaded 500 error, preventing them from accessing the site. 

**Root Cause:** A misplaced extension in a critical file caused a configuration error.  


## Timeline: Wrestling with the 500 Beast  

* **10:00 AM PST:** Alert! Monitoring flagged an increase in 500 errors originating from the Apache server. 
* **10:15 AM PST:**  Engineers dug into logs, suspecting an application issue. Initial focus was on application errors and database connectivity.
* **10:45 AM PST:** After chasing application ghosts, a hunch led to investigating Apache access logs. The culprit? A suspicious pattern of failed requests for a specific file – `/var/www/html/wp-settings.php`.
* **11:00 AM PST:**  Strace, our debugging champion, entered the scene. Running strace alongside `curl` revealed an error during file parsing – a clue that the issue resided within the file itself. ️‍♂️
* **11:30 AM PST:** Bingo! A close examination of the file exposed the real enemy – a line containing "phpp" instead of the rightful ".php" extension. 
* **12:00 PM PST:** The fix was swift. A Puppet manifest was created to use `sed` and permanently replace all ".phpp" occurrences with ".php" in the problematic file.
* **12:30 PM PST:**  With the fix deployed, Apache purred back to life, and website access was restored. 


## Root Cause and Resolution: The Extension Escapade 

The culprit was a misplaced extension in the `/var/www/html/wp-settings.php` file.  A line referring to a file with the extension ".phpp" instead of ".php" caused a configuration error when Apache attempted to process it.  

The resolution involved a two-pronged attack:

1. **Immediate Fix:** A Puppet manifest was created to utilize `sed` and permanently replace all instances of ".phpp" with ".php" within the `/var/www/html/wp-settings.php` file.
2. **Investigating the Origin:**  Further investigation is needed to determine how this errant extension found its way into the file. 


## Corrective and Preventative Measures:  Learning from Our Mistakes 

This incident highlights the importance of thorough configuration management and code review practices. Here's how we'll tighten things up:

* **Strengthen Code Reviews:**  Double-checking code for typos and configuration errors will be a top priority during code reviews.
* **Enhanced Monitoring:**  We'll explore implementing more granular monitoring for critical files to detect configuration drifts in the future.
* **Version Control Hygiene:** Enforcing stricter version control practices can help prevent unauthorized changes from slipping through the cracks.

By implementing these measures, we aim to create a more robust system less susceptible to such extension-related escapades. 

**P.S.** While this incident caused a temporary website outage, it served as a valuable learning experience. We're committed to continuous improvement and ensuring a smooth user experience in the future. 
