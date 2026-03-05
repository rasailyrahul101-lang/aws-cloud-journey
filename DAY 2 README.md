# Day 2 — Linux Basics Cheatsheet 🐧

## 🗂️ Navigation
| Command | What it does |
|---|---|
| `pwd` | Show current directory |
| `cd /path` | Move to a directory |
| `cd ~` | Go home instantly |
| `cd ..` | Go one level up |
| `ls` | List files |
| `ls -la` | List all files with permissions + hidden files |

## 📄 Files
| Command | What it does |
|---|---|
| `touch file.txt` | Create empty file |
| `cat file.txt` | View file contents |
| `echo "text" > file.txt` | Write to file (overwrites) |
| `echo "text" >> file.txt` | Append to file |
| `cp file.txt folder/` | Copy file |
| `mv file.txt new.txt` | Move or rename file |
| `rm file.txt` | Delete file |
| `rm -rf folder` | Delete folder — ⚠️ no undo |
| `mkdir folder` | Create folder |

## 🔐 Permissions
| chmod | Meaning | Use case |
|---|---|---|
| `400` | Owner read only | AWS `.pem` keys |
| `600` | Owner read+write | SSH config files |
| `644` | Owner read+write, others read | Regular files |
| `755` | Owner full, others read+execute | Scripts, web servers |

## 👀 Viewing Files
| Command | What it does |
|---|---|
| `head file.txt` | First 10 lines |
| `head -5 file.txt` | First 5 lines |
| `tail file.txt` | Last 10 lines |
| `tail -3 file.txt` | Last 3 lines |
| `tail -f file.txt` | Follow file live — server logs |
| `less file.txt` | Scroll through file — `q` to quit |

## ➡️ Redirect Operators
| Operator | What it does |
|---|---|
| `>` | Write to file — overwrites existing content |
| `>>` | Append to file — keeps existing content |

## 🔑 Key Things to Remember
- Folders show `d` at start of permissions — files show `-`
- Hidden files start with `.` — only visible with `ls -la`
- `rm -rf` has no undo — always double check before running
- `chmod 400` on `.pem` files — SSH will refuse to work without it
- `tail -f` is your best friend for watching live server logs
