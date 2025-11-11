# OSINT Recon Toolkit

A lightweight Python tool that automates **open-source intelligence (OSINT)** collection for any given domain.  
It retrieves WHOIS data, DNS A-records, and SSL certificate information from public sources and outputs a structured JSON report.

## Features

- WHOIS domain registration lookup
- DNS A-record resolution
- SSL Certificate Transparency data via [crt.sh](https://crt.sh)
- JSON report generation for further analysis

---

## Usage

### 1️ Create and activate a virtual environment

- python3 -m venv venv
- source venv/bin/activate

### 2️: Install dependencies

- pip install -r requirements.txt

### 3️: Run the tool

- python recon.py
  Enter a domain (e.g. example.com) when prompted.
  A JSON report will be generated in the current directory.

### Example Output

```bash
OSINT Recon Toolkit
Enter domain (without http/https): example.com
Report generated: example.com_report.json
```
**Sample Report:** [View sample_report.json](docs/sample_report.json)


## Learning Goals:

This project demonstrates:

- Practical OSINT data collection using Python
- DNS and WHOIS enumeration
- JSON data structuring for security reports

## Requirements:

- requests
- python-whois
- dnspython
- rich

## Author

- Barkhad Isse
GitHub: github.com/barkhad-isse
