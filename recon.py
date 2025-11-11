"""
__________________________________________________________________________________
OSINT Recon Toolkit
__________________________________________________________________________________
- A lightweight Python tool to collect open-source intelligence (OSINT)
about a given domain. Gathers WHOIS data, DNS A-records, and SSL certificate info. 
__________________________________________________________________________________
"""

import whois
import dns.resolver
import requests
import json
from rich.console import Console

console = Console()

def domain_whois(domain: str) -> dict:
    """Fetch WHOIS information for the target domain."""
    try:
        return whois.whois(domain)
    except Exception as e:
        return {"error": f"WHOIS lookup failed: {e}"}

def dns_lookup(domain: str) -> list:
    """Resolve the domain's A-records."""
    try:
        return [str(rdata) for rdata in dns.resolver.resolve(domain, "A")]
    except Exception as e:
        return [f"DNS lookup failed: {e}"]

def crtsh_lookup(domain: str) -> list:
    """Retrieve SSL certificate names from crt.sh."""
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        r = requests.get(url, timeout=10)
        if r.ok:
            return sorted(list({entry["name_value"] for entry in r.json()}))
        return ["No certificate data found."]
    except Exception as e:
        return [f"crt.sh lookup failed: {e}"]

def main():
    console.print("[bold blue]OSINT Recon Toolkit[/bold blue]")
    target = input("Enter domain (without http/https): ").strip()

    if not target:
        console.print("[bold red]Error:[/bold red] No domain provided.")
        return

    console.print(f"\n[cyan]Collecting data for:[/cyan] {target}\n")

    data = {
        "whois": domain_whois(target),
        "dns": dns_lookup(target),
        "certificates": crtsh_lookup(target),
    }

    report_file = f"{target}_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)

    console.print(f"[bold green]✔ Report generated:[/bold green] {report_file}")

if __name__ == "__main__":
    main()
