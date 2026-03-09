# Day 4 — Networking Basics 

## 1. IP Address

### What is an IP Address?
A numeric address that uniquely identifies a device on a network.
Just like a home address tells the postman where to deliver —
an IP address tells the internet where to send data.Each octet range 0-255.

### Two Types

| | IPv4 | IPv6 |
|---|---|---|
| **Bits** | 32 bits | 128 bits |
| **Format** | Decimal — `66.94.29.13` | Hexadecimal — `2001:0db8:85a3:0000:0000:8a2e:0370:7334` |
| **Structure** | 4 octets separated by `.` | 8 groups of 16 bits separated by `:` |
| **Example** | `192.168.1.1` | `2001:0db8::1` |
| **Total addresses** | ~4.3 billion | 340 undecillion |

### IPv4 — How Binary Works
Each octet is 8 bits. Chart: `128, 64, 32, 16, 8, 4, 2, 1`
```
66 in binary:
128  64  32  16   8   4   2   1
  0   1   0   0   0   0   1   0
      ↑                   ↑
     64                 + 2  = 66
Result: 01000010
```

### IPv6 — How Hexadecimal Works
128 bits total — 8 groups of 16 bits. Each 4 bits = 1 hex character.
Chart: `8, 4, 2, 1`
```
0101 = 5
1101 = 13 = D

Hex digits: 0-9 then A=10, B=11, C=12, D=13, E=14, F=15
```

### ⚠️ Key Things to Remember
- IPv4 = 32 bits, IPv6 = 128 bits (not 126)
- IPv4 has ~4.3 billion addresses — almost exhausted, why IPv6 exists
- IPv6 uses letters A-F for numbers 10-15


 ## 2. Subnet & CIDR Notation

### What is a Subnet Mask?
A number that resembles an IP address and reveals how many bits 
in the IP address are used for the network portion by masking it.

### IP Address = Two Parts
Every IP address has two parts:
- **Network portion** — identifies the network
- **Host portion** — identifies the device on that network

### Example 1 — Simple
```
IP Address:  172.16.1.0    → 10101100.00010000.00000001.00000000
Subnet Mask: 255.255.0.0   → 11111111.11111111.00000000.00000000

Network portion: 172.16      (first 2 octets — where 1s are)
Host portion:    1.0         (last 2 octets — where 0s are)
```

### Example 2 — Tricky
```
IP Address:  172.16.1.0      → 10101100.00010000.00000001.00000000
Subnet Mask: 255.255.224.0   → 11111111.11111111.11100000.00000000

Network portion: 172.16 + 3 bits of third octet
Host portion:    remaining 13 bits
```

---

### What is Subnetting?
IP addresses have network and host parts so networks can be 
**logically broken down into smaller networks** — this is subnetting.

### Real World Example
A business has 1 network `255.255.255.0` with 254 usable hosts.
They want 3 separate networks for 3 departments.

**Solution: Borrow bits from host portion**

| Borrowed Bits | Subnet Mask | Subnets | Hosts per Subnet |
|---|---|---|---|
| 0 | 255.255.255.0 | 1 | 254 |
| 1 | 255.255.255.128 | 2 | 126 |
| 2 | 255.255.255.192 | 4 | 62 |
| 3 | 255.255.255.224 | 8 | 30 |
| 4 | 255.255.255.240 | 16 | 14 |
| 5 | 255.255.255.248 | 32 | 6 |
| 6 | 255.255.255.252 | 64 | 2 |

**For 3 departments → borrow 2 bits**
- New subnet mask: `255.255.255.192`
- Result: 4 subnets, 62 hosts each ✅

### Key Rules
- Each borrowed bit **doubles** the number of subnets
- Each borrowed bit **halves** the number of hosts per subnet
- 2 addresses always reserved per subnet:
  - **Network address** (first)
  - **Broadcast address** (last)

---

### IP Classes

| Class | Range | Subnet Mask | Used For |
|---|---|---|---|
| A | 1-126 | 255.0.0.0 | Large networks, internet |
| B | 128-191 | 255.255.0.0 | Medium networks |
| C | 192-223 | 255.255.255.0 | Small networks |

---

### CIDR — Classless Inter-Domain Routing

CIDR uses **slash notation** to represent subnet masks:

| CIDR | Subnet Mask | Hosts |
|---|---|---|
| `/8` | 255.0.0.0 | 16 million |
| `/16` | 255.255.0.0 | 65,534 |
| `/24` | 255.255.255.0 | 254 |
| `/32` | 255.255.255.255 | 1 (single host) |

### What does /24 mean?
`192.168.1.0/24` means:
- First **24 bits** are the network portion
- Last **8 bits** are for hosts ,**2^8= 256**
- Allows **254 usable hosts**

### AWS Context
In AWS VPC you will always see CIDR notation:
- VPC: `10.0.0.0/16` → 65,534 possible addresses
- Subnet: `10.0.1.0/24` → 254 possible addresses
- Single EC2: `10.0.1.5/32` → exactly 1 host

### AWS Context
When you create a subnet in AWS with /24:
- AWS actually reserves 5 addresses not 2
- So you get 251 usable hosts in AWS subnets
- AWS reserves first 4 and last 1 for internal purposes

## 3. DNS — Domain Name System

### What is DNS?
DNS converts human readable domain names like `google.com` 
into IP addresses like `142.250.192.14` so computers can 
communicate with each other.

> DNS is like a phone book for the internet.

### The DNS Journey — Step by Step
```
You type google.com
        ↓
1. Browser/OS Cache
   checks locally first — been here before?
        ↓ not found
2. DNS Resolver (ISP)
   your internet provider's DNS server
   checks its own cache first
        ↓ not found
3. Root Server
   doesn't know google.com but knows
   where .com servers live → directs resolver
        ↓
4. TLD Server (Top Level Domain)
   manages .com, .org, .net domains
   directs resolver to google's nameserver
        ↓
5. Authoritative Name Server
   knows EVERYTHING about google.com
   returns IP address → 142.250.192.14
        ↓
6. Resolver returns IP to your browser
   browser connects to 142.250.192.14
   Google page loads ✅
```

### Key Players

| Player | Role |
|---|---|
| **DNS Resolver** | Your ISP's DNS — first stop after cache |
| **Root Server** | Knows where TLD servers live |
| **TLD Server** | Manages .com, .org, .net etc |
| **Authoritative Server** | Final answer — knows exact IP |

### DNS Caching
Every step caches the result to speed up future requests:
- Browser cache — fastest
- OS cache — second
- ISP resolver cache — third
- If all cache miss → full journey above

### Common DNS Records

| Record | Purpose | Example |
|---|---|---|
| **A** | Domain → IPv4 address | `google.com → 142.250.192.14` |
| **AAAA** | Domain → IPv6 address | `google.com → 2607:f8b0::200e` |
| **CNAME** | Domain → another domain | `www.google.com → google.com` |
| **MX** | Mail server for domain | `gmail.com mail server` |

### AWS Context
- **Route 53** is AWS's DNS service
- You'll use it in Week 8 to point your domain to CloudFront
- Understanding DNS now makes Route 53 feel simple later

### ⚠️ Key Things to Remember
- DNS resolver = your ISP (or 8.8.8.8 Google DNS)
- Root servers → TLD servers → Authoritative servers
- Caching speeds everything up
- Without DNS you'd have to memorize IP addresses for every website



## 4. Ports

### What is a Port?
Think of an IP address as a **building** and a port as a 
**door number** inside that building.
Each door leads to a different service.
```
192.168.1.1:80   → HTTP web traffic door
192.168.1.1:443  → HTTPS secure web traffic door
192.168.1.1:22   → SSH remote access door
192.168.1.1:3306 → MySQL database door
```

### The 4 Ports You Must Know

| Port | Protocol | Used For | AWS Context |
|---|---|---|---|
| `80` | HTTP | Web traffic — unsecured | EC2 web server |
| `443` | HTTPS | Web traffic — secured | CloudFront, ALB |
| `22` | SSH | Remote server access | Connecting to EC2 |
| `3306` | MySQL | Database connections | RDS MySQL |

### Memory Tricks

| Port | Memory Trick |
|---|---|
| `80` | HTTP — 80 is the standard web door |
| `443` | HTTPS — 443 is the secure web door |
| `22` | SSH — Secure Shell |
| `3306` | MySQL — just memorize this one |

### Other Common Ports for AWS

| Port | Used For |
|---|---|
| `5432` | PostgreSQL database |
| `6379` | Redis cache |
| `8080` | Alternative HTTP |
| `27017` | MongoDB |

### AWS Context
In AWS Security Groups you control which ports are open:
- Allow port `22` → let SSH traffic in
- Allow port `80` → let web traffic in
- Allow port `443` → let secure web traffic in
- Block everything else → principle of least privilege

> **Real world:** When your EC2 web server is unreachable,
> first thing to check is whether port 80 or 443 is open
> in the Security Group.


## 5. Firewall

### What is a Firewall?
A firewall guards your server from unwanted traffic
by allowing or blocking specific ports.

Think of it as a **security guard at a building entrance:**
```
Internet Traffic
      ↓
  🛡️ Firewall
      ↓
   Checks rules:
   - Port allowed? ✅ Let it in
   - Port blocked? ❌ Reject it
      ↓
   Your Server
```

### Two Types of Rules

| Rule | What it does |
|---|---|
| **Inbound** | Controls traffic coming INTO your server |
| **Outbound** | Controls traffic going OUT of your server |

### AWS Context
In AWS the firewall is called a **Security Group:**
- Open port `22` → allow SSH access
- Open port `80` → allow web traffic
- Open port `443` → allow secure web traffic
- Everything else → blocked by default ✅

> **Real world:** Server unreachable? First thing to check
> is whether the correct port is open in the Security Group.

---

## 6. HTTP vs HTTPS

### What is the Difference?

| | HTTP | HTTPS |
|---|---|---|
| **Full name** | HyperText Transfer Protocol | HyperText Transfer Protocol Secure |
| **Port** | 80 | 443 |
| **Encrypted** | ❌ No | ✅ Yes |
| **Padlock in browser** | ❌ No | ✅ Yes |
| **Used for** | Old websites | All modern websites |

### Simple Analogy
- HTTP = sending a **postcard** — anyone can read it
- HTTPS = sending a **sealed envelope** — only sender and receiver can read it

### How HTTPS Works
```
Browser → "I want to connect securely"
Server  → "Here is my SSL certificate"
Browser → "Certificate trusted ✅"
Both    → Create encrypted tunnel
Data    → Flows securely 🔒
```

### AWS Context
- **CloudFront** adds HTTPS to your S3 static website
- **ACM (Certificate Manager)** gives free SSL certificates
- Always use HTTPS in production — never HTTP
- In Week 8 you will set this up for your resume website