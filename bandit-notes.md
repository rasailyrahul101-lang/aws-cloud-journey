# Bandit Notes 🎮

## Level 0 → 1
**How to solve:** SSH in, run `ls -la` to find the readme file, then `cat readme`
**Password:** ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If


## Level 1 → 2
**How to solve:** File was named `-`. Can't use `cat -` 
because Linux treats `-` as keyboard input. 
Use `cat ./-` to specify current directory path.
**Password:** 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

## Level 2 → 3
**How to solve:** Filename had dashes and spaces: `--spaces in this filename--`
Can't use `cat` directly because `--` is treated as a flag.
Two solutions:
1. `cat ./"--spaces in this filename--"` → use ./ with quotes
2. `cat -- "--spaces in this filename--"` → -- tells Linux everything after is a filename
**Password:** MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

## Level 3 → 4
**How to solve:** Hidden file inside `inhere` directory.
1. `cd inhere` to move into directory
2. `ls -la` to reveal hidden files (file was `...Hiding-From-You`)
3. `cat "...Hiding-From-You"` to read it
**Password:** 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

## Level 4 → 5
**How to solve:** Multiple files in `inhere` directory.
1. `cd inhere`
2. `file ./-file*` → checks file type of all files at once
3. Only `-file07` said ASCII text — that's human readable
4. `cat ./-file07` to read password
**Key learning:** `file` command tells you what type of data is in a file
**Password:** 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

New command you just learned:
file filename Shows what type of data is inside a file, file ./* Check type of ALL files at once


## Level 5 → 6
**How to solve:** Find file with specific size in nested directories
1. `cd inhere`
2. `find . -size 1033c` → find file exactly 1033 bytes (`c` = bytes)
3. Found `./maybehere07/.file2`
4. `cat ./maybehere07/.file2` to read password
**Key learning:** `find -size` searches by file size
**Password:** HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

New command you just learned:
find . -size 1033cFind files exactly 1033
bytes \ find . -size +1033cFind files larger than 1033 bytes \ find . -size -1033cFind files smaller than 1033 bytes

## Level 6 → 7
**How to solve:** Search entire server for file owned by specific user and group
1. `find / -user bandit7 -group bandit6 -size 33c`
2. Lots of "Permission denied" errors — ignore them, look for the actual result
3. Found `/var/lib/dpkg/info/bandit7.password`
4. `cat /var/lib/dpkg/info/bandit7.password`
**Key learning:** 
- `find /` searches entire server
- `-user` and `-group` filter by owner
- Permission denied errors are normal — just look for the actual file path
**Password:** morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
Pro tip for next time — hide those permission errors:
bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null

2>/dev/null redirects error messages to nowhere — cleaner output!

## Level 7 → 8
**How to solve:** Search for word "millionth" inside data.txt
1. `grep -i "millionth" data.txt`
2. Password is right next to the word
**Key learning:** grep is perfect for searching large files instantly
**Password:** dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

## Level 8 → 9
**How to solve:** Find the only line that appears once in data.txt
1. `sort data.txt | uniq -u`
2. `sort` first — uniq only works on consecutive lines
3. `uniq -u` shows only unique lines (appearing once)
**Key learning:** 
- `sort` + `uniq -u` is a classic combo
- `uniq` only works correctly after sorting
**Password:** 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
New commands learned:
sort file Sort lines alphabetically, uniq -u Show only unique lines , uniq -d Show only duplicate lines , uniq -c Count occurrences of each line


## Level 9 → 10
**How to solve:** Extract human readable strings from binary file
1. `strings data.txt | grep "==="`
2. `strings` extracts readable text from binary file
3. `grep "==="` filters lines with = characters
4. Password is on the last line
**Key learning:** `strings` command extracts human readable 
text from any file including binaries
**Password:** FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

New command learned:
strings file   Extract human readable text from any file

## Level 10 → 11
**How to solve:** Decode base64 encoded file
1. `base64 -d data.txt`
2. `-d` means decode
**Key learning:** base64 is a common encoding used in 
cloud configs, AWS credentials, and API responses
**Password:** dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr