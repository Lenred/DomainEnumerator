### Lennart Labahn
### Domain Enumerator
### Dec 8.12.2022

import urllib.parse

def enumerate_subdomains_and_paths(domain):
    # Use the urllib.parse module to split the domain into subdomain, domain, and tld
    parsed_domain = urllib.parse.urlparse(domain)

    subdomains = parsed_domain.hostname.split('.')
    paths = parsed_domain.path.split('/')

    # Enumerate all possible combinations of subdomains and paths
    for subdomain in subdomains:
        for path in paths:
            print(f"{subdomain}.{domain}/{path}")

# Example usage
enumerate_subdomains_and_paths("www.example.com")

