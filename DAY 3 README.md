# Day 3 — Linux Basics Part 2

## Searching

### grep — Search Inside Files
| Command | What it does |
|---|---|
| `grep "word" file` | Find lines containing word |
| `grep -i "word" file` | Case insensitive search |
| `grep -n "word" file` | Show line numbers |
| `grep -v "word" file` | Show everything EXCEPT word |
| `grep -c "word" file` | Count matching lines |

### find — Search for Files
| Command | What it does |
|---|---|
| `find . -name "file.txt"` | Find file by exact name |
| `find . -name "*.txt"` | Find all txt files |
| `find . -type d` | Find all directories |
| `find . -type f` | Find all files |

> **Key difference:** `grep` searches INSIDE files, `find` searches FOR files

---

##  Networking Tools

| Command | What it does | Real world use |
|---|---|---|
| `ping server` | Check if server is alive | Is my EC2 instance reachable? |
| `curl URL` | Make HTTP request | Test my API endpoint |
| `curl -I URL` | Show response headers only | Check status code |
| `curl -o file URL` | Save response to file | Download from URL |
| `wget URL` | Download file | Download installers on EC2 |
| `ssh user@ip` | Connect to remote server | Daily EC2 access |
| `ssh -i key.pem user@ip` | Connect with key file | AWS EC2 connection |

### curl vs wget
| | curl | wget |
|---|---|---|
| Main use | API calls, testing endpoints | Downloading files |
| Output | Prints to screen | Saves to file |

### SSH Usernames by AMI
| AMI | Username |
|---|---|
| Ubuntu | `ubuntu` |
| Amazon Linux | `ec2-user` |
| CentOS | `centos` |
| Debian | `admin` |

---

##  Process Management

| Command | What it does |
|---|---|
| `ps` | Show current session processes |
| `ps aux` | Show ALL processes |
| `ps aux \| grep name` | Find specific process |
| `top` | Live process monitor — press `q` to quit |
| `top` then `P` | Sort by CPU usage |
| `top` then `M` | Sort by memory usage |
| `kill PID` | Gracefully stop process |
| `kill -9 PID` | Force kill instantly |

### What is a PID?
> Process ID — unique number assigned to every running process.
> You need it to kill a specific process.

### kill vs kill -9
| Command | Behaviour |
|---|---|
| `kill PID` | Graceful stop — gives process time to clean up |
| `kill -9 PID` | Force kill — instant, no cleanup |

---

##  Piping with `|`

> Piping sends the output of one command as input to another command.
```bash
# Basic syntax
command1 | command2

# Examples
cat file.txt | grep "ERROR"           # Filter errors from file
ps aux | grep python | wc -l          # Count python processes
cat file.txt | grep "ERROR" | wc -l   # Count error lines
ls -la | grep "^d"                    # Show only directories
cat file.txt | sort | uniq            # Sort and remove duplicates
```

### Pipe vs Redirect
| Symbol | Sends output to | Example |
|---|---|---|
| `|` | Another command | `cat file | grep "error"` |
| `>` | A file (overwrites) | `cat file | grep "error" > errors.txt` |
| `>>` | A file (appends) | `echo "line" >> file.txt` |

---

##  Package Management (apt)

> Works on Ubuntu/Debian Linux — used on EC2 from Week 2 onwards.
> Think of `apt` as the Play Store for Linux.

| Command | What it does |
|---|---|
| `sudo apt update` | Refresh package list — always run first |
| `sudo apt install nginx -y` | Install a package |
| `sudo apt install nginx curl git -y` | Install multiple packages |
| `sudo apt remove nginx` | Remove package |
| `sudo apt purge nginx` | Remove package + config files |
| `sudo apt upgrade` | Upgrade all installed packages |
| `apt search nginx` | Search for a package |

### What is sudo?
> `sudo` = Super User Do = run as administrator
> Use only when needed — principle of least privilege

### Most Common Packages on EC2
| Command | Installs |
|---|---|
| `sudo apt install nginx -y` | Web server |
| `sudo apt install python3 -y` | Python |
| `sudo apt install git -y` | Git |
| `sudo apt install docker.io -y` | Docker |
| `sudo apt install unzip -y` | Unzip files |

> `-y` automatically answers yes to prompts — essential in scripts

---

##  Key Things to Remember

- `grep` searches INSIDE files — `find` searches FOR files
- `ping` tells you if a server is alive
- `curl` is for API calls — `wget` is for downloading files
- SSH to EC2: `ssh -i mykey.pem ubuntu@YOUR_EC2_IP`
- PID = Process ID — needed to kill a process
- `kill` = graceful, `kill -9` = force
- `|` sends output to next command
- Always run `sudo apt update` before installing anything
- `sudo` = run as administrator — use only when needed

----------------------------------------------------------------
