Hi Alice,

I’ve investigated the issue you reported with accessing the website site.recruitment.shq.nz.

I pinged the server using the IP address you've given, what it does is to see whether the server is up and responding to network requests and the server replied to my ping which means it is still up.

I used nslookup to query DNS servers to obtain information about domain names and IP addresses, and I found where is the problem, the IP address of the website is 192.168.1.10 which is a private address and 

which is why it's inaccessible from the public internet. The website is likely behind a misconfigured DNS server.

To resolve this, I recommend the following steps:

1. Check and update the DNS records for site.recruitment.shq.nz to ensure they point to the correct public IP address.

2. If you need to manually override the DNS resolution temporarily, you can modify the hosts file on your computer to map the domain to the correct IP. This method is suitable for local testing, but won't affect the broader DNS setup.
I was able to access the site by using the correct DNS resolution. Upon accessing the site, I was able to retrieve the hidden HTML code, which is as follows:

This is the following hidden HTML code after I access to the website: 

### R3J1cTRVNmJRcVZkdHh4R0IwaDZObXVaZjh3WlpoeXZQZHdvMGw5dlF0ZEFRQT09

Please have your DNS settings corrected to ensure that the public-facing IP address is properly configured for the website. Once the DNS is fixed, the site should be accessible to everyone.

Please let me know if you need further assistance with this process!

Best regards,
Duong Tran
