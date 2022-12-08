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

# Ask the user for a domain
domain = input("Enter a domain: ")

# Enumerate the subdomains and paths of the given domain
enumerate_subdomains_and_paths(domain)
