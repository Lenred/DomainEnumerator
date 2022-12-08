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

def save_output_to_file(output, filename):
    with open(filename, "w") as file:
        file.write(output)

# Ask the user for a domain
domain = input("Enter a domain: ")

# Enumerate the subdomains and paths of the given domain
output = enumerate_subdomains_and_paths(domain)

# Ask the user for an output file name
output_file = input("Please give a file name for the subdomains and paths: ")

# Save the output to a file
save_output_to_file(output, output_file)
