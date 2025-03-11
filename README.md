# Recruitment API Challenge

## Overview

This repository contains a solution to the Recruitment API Challenge. The challenge consists of two parts:

### Part One: Calling an API
The first part of the challenge requires retrieving information about registered domain names and associated DNS records using a simple API. The API provides two endpoints:
1. `/domains/{client_id}` - Returns a list of domains registered by the customer, along with any DNS zones.
2. `/zones/{zone_id}` - Returns DNS records for a given DNS zone.

the API key is `h523hDtETbkJ3nSJL323hjYLXbCyDaRZ` and the customer ID is `100` for Business Systems International to retrieve their domains and DNS records. The API URL is `https://api.recruitment.shq.nz`.

Below is the samele of retrieved data:

Domain: shq.nz

Record: {'id': '2511471', 'name': 'recruitment.shq.nz', 'type': 'SOA', 'content': 'ns1.sitehost.co.nz soa@sitehost.co.nz 2024030806 10800 3600 1209600 3600', 'ttl': '3600', 'prio': '0', 'change_date': '1709868974'}

Record: {'id': '2511472', 'name': 'recruitment.shq.nz', 'type': 'NS', 'content': 'ns1.sitehost.co.nz', 'ttl': '3600', 'prio': '0', 'change_date': '1709868856'}

Record: {'id': '2511473', 'name': 'recruitment.shq.nz', 'type': 'NS', 'content': 'ns2.sitehost.co.nz', 'ttl': '3600', 'prio': '0', 'change_date': '1709868856'}

Record: {'id': '2511474', 'name': 'recruitment.shq.nz', 'type': 'NS', 'content': 'ns3.sitehost.co.nz', 'ttl': '3600', 'prio': '0', 'change_date': '1709868856'}

Record: {'id': '2511475', 'name': 'recruitment.shq.nz', 'type': 'NS', 'content': 'ns4.sitehost.co.nz', 'ttl': '3600', 'prio': '0', 'change_date': '1709868856'}

Record: {'id': '2511486', 'name': 'site.recruitment.shq.nz', 'type': 'A', 'content': '192.168.1.10', 'ttl': '3600', 'prio': '0', 'change_date': '1709868926'}

Record: {'id': '2511487', 'name': 'api.recruitment.shq.nz', 'type': 'A', 'content': '223.165.64.38', 'ttl': '3600', 'prio': '0', 'change_date': '1709868974'}

Record: {'id': '1835283', 'name': 'wal.shq.nz', 'type': 'SOA', 'content': 'ns1.sitehost.co.nz soa@sitehost.co.nz 2023011100 10800 3600 604800 3600', 'ttl': '3600', 'prio': '0', 'change_date': '1673404852', 'state': '1'}

Record: {'id': '1835284', 'name': 'wal.shq.nz', 'type': 'NS', 'content': 'ns1.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1596518117', 'state': '1'}

Record: {'id': '1835285', 'name': 'wal.shq.nz', 'type': 'NS', 'content': 'ns2.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1596518117', 'state': '1'}

Record: {'id': '1835286', 'name': 'wal.shq.nz', 'type': 'NS', 'content': 'ns3.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1596518117', 'state': '1'}

Domain: sitehost.nz

Record: {'id': '960775', 'name': 'sitehost.nz', 'type': 'SOA', 'content': 'ns1.sitehost.co.nz soa@sitehost.co.nz 2023123100 10800 3600 604800 3600', 'ttl': '3600', 'prio': '0', 'change_date': '1703987774', 'state': '1'}

Record: {'id': '960776', 'name': 'sitehost.nz', 'type': 'NS', 'content': 'ns1.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1579148134', 'state': '1'}

Record: {'id': '960777', 'name': 'sitehost.nz', 'type': 'NS', 'content': 'ns2.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1579148134', 'state': '1'}

Record: {'id': '960778', 'name': 'sitehost.nz', 'type': 'NS', 'content': 'ns3.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1579148134', 'state': '1'}

Record: {'id': '963446', 'name': 'sitehost.nz', 'type': 'A', 'content': '120.138.23.6', 'ttl': '3600', 'prio': '0', 'change_date': '1579148134', 'state': '1'}

Record: {'id': '963447', 'name': 'www.sitehost.nz', 'type': 'A', 'content': '120.138.23.6', 'ttl': '3600', 'prio': '0', 'change_date': '1579148134', 'state': '1'}

Record: {'id': '968063', 'name': 'sitehost.nz', 'type': 'MX', 'content': 'mx3.ext.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1579148134', 'state': '1'}

Record: {'id': '1183223', 'name': 'sitehost.nz', 'type': 'AAAA', 'content': '2403:7000:4000:100::6', 'ttl': '3600', 'prio': '0', 'change_date': '1579148134', 'state': '1'}

Record: {'id': '1183224', 'name': 'www.sitehost.nz', 'type': 'AAAA', 'content': '2403:7000:4000:100::6', 'ttl': '3600', 'prio': '0', 'change_date': '1579148135', 'state': '1'}

Record: {'id': '1183274', 'name': 'sitehost.nz', 'type': 'TXT', 'content': 'v=spf1 a mx include:_spf.sitehost.co.nz ~all', 'ttl': '3600', 'prio': '0', 'change_date': '1579148135', 'state': '1'}

Record: {'id': '1234684', 'name': 'docs.sitehost.nz', 'type': 'A', 'content': '120.138.23.6', 'ttl': '3600', 'prio': '0', 'change_date': '1579148135', 'state': '1'}

Record: {'id': '1322547', 'name': 'kb.sitehost.nz', 'type': 'A', 'content': '120.138.23.6', 'ttl': '3600', 'prio': '0', 'change_date': '1579148136', 'state': '1'}

Record: {'id': '1322550', 'name': 'feedback.sitehost.nz', 'type': 'A', 'content': '120.138.23.6', 'ttl': '3600', 'prio': '0', 'change_date': '1579148136', 'state': '1'}

Record: {'id': '1711326', 'name': 'blog.sitehost.nz', 'type': 'A', 'content': '120.138.23.25', 'ttl': '3600', 'prio': '0', 'change_date': '1663544873', 'state': '1'}

Record: {'id': '1712527', 'name': 'webmail.sitehost.nz', 'type': 'A', 'content': '120.138.23.25', 'ttl': '3600', 'prio': '0', 'change_date': '1663544873', 'state': '1'}

Record: {'id': '1305087', 'name': 'paste.sitehost.nz', 'type': 'SOA', 'content': 'ns1.sitehost.co.nz soa@sitehost.co.nz 2017112905 10800 3600 604800 3600', 'ttl': '3600', 'prio': '0', 'change_date': '1511942652', 'state': '1'}

Record: {'id': '1305088', 'name': 'paste.sitehost.nz', 'type': 'NS', 'content': 'ns1.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1511942651', 'state': '1'}

Record: {'id': '1305089', 'name': 'paste.sitehost.nz', 'type': 'NS', 'content': 'ns2.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1511942651', 'state': '1'}

Record: {'id': '1305090', 'name': 'paste.sitehost.nz', 'type': 'NS', 'content': 'ns3.sitehost.co.nz.', 'ttl': '3600', 'prio': '0', 'change_date': '1511942652', 'state': '1'}

Record: {'id': '1305091', 'name': 'paste.sitehost.nz', 'type': 'A', 'content': '120.138.23.6', 'ttl': '3600', 'prio': '0', 'change_date': '1511942652', 'state': '1'}

Record: {'id': '1305092', 'name': 'www.paste.sitehost.nz', 'type': 'A', 'content': '120.138.23.6', 'ttl': '3600', 'prio': '0', 'change_date': '1511942652', 'state': '1'}

Domain: sitename.co.nz

Record: {'id': '9037', 'name': 'sitename.co.nz', 'type': 'SOA', 'content': 'ns1.sitehost.co.nz support@sitehost.co.nz 2023121400 28800 7200 604800 3600', 'ttl': '3600', 'prio': '0', 'change_date': '1702478822', 'state': '1'}

Record: {'id': '9038', 'name': 'sitename.co.nz', 'type': 'A', 'content': '120.138.16.26', 'ttl': '3600', 'prio': '0', 'change_date': '1521027594', 'state': '1'}

Record: {'id': '9039', 'name': 'sitename.co.nz', 'type': 'NS', 'content': 'ns1.sitehost.co.nz', 'ttl': '3600', 'prio': '0', 'change_date': '1262487917', 'state': '1'}

Record: {'id': '9040', 'name': 'sitename.co.nz', 'type': 'NS', 'content': 'ns2.sitehost.co.nz', 'ttl': '3600', 'prio': '0', 'change_date': '1262487918', 'state': '1'}

Record: {'id': '9041', 'name': 'sitename.co.nz', 'type': 'NS', 'content': 'ns3.sitehost.co.nz', 'ttl': '3600', 'prio': '0', 'change_date': '1274303138', 'state': '1'}

Record: {'id': '58898', 'name': 'sitename.co.nz', 'type': 'MX', 'content': 'mx3.ext.sitehost.co.nz.', 'ttl': '3600', 'prio': '10', 'change_date': '1316481763', 'state': '1'}

Record: {'id': '81779', 'name': 'ns1.sitename.co.nz', 'type': 'A', 'content': '223.165.67.4', 'ttl': '3600', 'prio': '0', 'change_date': '1646238823', 'state': '1'}

Record: {'id': '81780', 'name': 'ns2.sitename.co.nz', 'type': 'A', 'content': '120.138.23.11', 'ttl': '3600', 'prio': '0', 'change_date': '1645547152', 'state': '1'}

Record: {'id': '81781', 'name': 'ns3.sitename.co.nz', 'type': 'A', 'content': '194.195.246.56', 'ttl': '3600', 'prio': '0', 'change_date': '1644855580', 'state': '1'}

Record: {'id': '81806', 'name': 'www.sitename.co.nz', 'type': 'A', 'content': '120.138.16.26', 'ttl': '3600', 'prio': '0', 'change_date': '1521035086', 'state': '1'}

Record: {'id': '153028', 'name': 'signup.sitename.co.nz', 'type': 'A', 'content': '120.138.16.26', 'ttl': '3600', 'prio': '0', 'change_date': '1521027594', 'state': '1'}

Record: {'id': '921559', 'name': 'feedback.sitename.co.nz', 'type': 'A', 'content': '120.138.23.6', 'ttl': '3600', 'prio': '0', 'change_date': '1519860754', 'state': '1'}

Record: {'id': '2263721', 'name': 'sitename.co.nz', 'type': 'TXT', 'content': 'v=spf1 a mx include:_spf.sitehost.co.nz ~all', 'ttl': '3600', 'prio': '0', 'change_date': '1673563897', 'state': '1'}

### Part Two: Resolving a Customer Issue
The second part involves troubleshooting an issue faced by the customer, Business Systems International, with their website. We identify the problem, retrieve hidden code from the page, and then communicate a resolution to the customer.

See the reply.md for more information about how I troubleshoot and what should be the solution.

---

