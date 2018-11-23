# Mini-project-2

Using shell commands:

sort ads.txt | uniq > ads_s.txt <-- Sorts, removes dupes
less ads_s.txt | perl break.pl > ads_b.txt <--- Pipes text to perl and converts to readable format
db_load -T -f ads_b.txt -t hash ads_b.db <--- creates Berkeley DB file
