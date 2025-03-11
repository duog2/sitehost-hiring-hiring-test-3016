import requests

base_url = "https://api.recruitment.shq.nz"

api_key = "h523hDtETbkJ3nSJL323hjYLXbCyDaRZ"

# Function to retrieve domain data by client_id
def get_domains(client_id):
    url = f"{base_url}/domains/{client_id}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error retrieving domains: {response.status_code}")
        return None

# Function to retrieve DNS records by zone_id
def get_dns_records(zone_id):
    url = f"{base_url}/zones/{zone_id}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        dns_data = response.json()
        return dns_data.get("records", [])  
    else:
        print(f"Error retrieving DNS records: {response.status_code}")
        return None

# client id = 100
data = get_domains(100)

if data:
    for domain in data:
        print(f"Domain: {domain['name']}\n")
        for zone in domain['zones']:
            zone_id = zone['uri'][7:]  
            dns_records = get_dns_records(zone_id)
            for record in dns_records:
                print(f"Record: {record}\n")  
