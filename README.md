# DomainEnumerator
This should enumerate all Subdomains and paths of a Domain. 

+++++ Change Log +++++

> Dec 8 2022 - Added user input for Test Domain

> Dec 8 2022 - Added Output File and User input that creates file name. 

> Dec 8 2022 - Debugged the code -- The bug in the original code was that the enumerate_subdomains_and_paths function does not return any value, so the output variable is always None. This causes an error when the save_output_to_file function tries to write None to a file.


+++++ Notes to track +++++

In this code, the user is prompted to enter a domain, which is then passed as an argument to the enumerate_subdomains_and_paths function. This function then enumerates all possible combinations of subdomains and paths for the given domain.

Here is an example of how this code might be used:

> > > Enter a domain: www.example.com
> www.example.com/
> example.com/
> com/
