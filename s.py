import requests
import json, random
import re
from bs4 import BeautifulSoup
from retrying import retry

# Load domains list from JSON file
with open("domains_list.json", "r") as domains_list_file:
    domains_list = json.load(domains_list_file)

# Error handler for retrying failed requests
def requestErrorHandler(exception):
    return isinstance(exception, requests.RequestException)

# Function to fetch inbox emails dynamically
@retry(retry_on_exception=requestErrorHandler, wait_fixed=1000)
def getinbox(email=None):
    if email is None:
        raise TypeError("Missing email")
    
    # Request and parse inbox page
    response = requests.get(f"https://emailfake.com/{email}", timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    
    emails = []
    email_table = soup.find("div", {"id": "email-table"})
    
    if email_table:
        # Locate each email entry within email-table
        email_entries = email_table.find_all("a", class_="list-group-item")
        
        for entry in email_entries:
            # Extract sender, subject, and timestamp
            sender = entry.find("div", class_="from_div_45g45gg").get_text(strip=True) if entry.find("div", class_="from_div_45g45gg") else "Unknown"
            subject = entry.find("div", class_="subj_div_45g45gg").get_text(strip=True) if entry.find("div", class_="subj_div_45g45gg") else "(No Subject)"
            timestamp = entry.find("div", class_="time_div_45g45gg").get_text(strip=True) if entry.find("div", class_="time_div_45g45gg") else "Unknown"
            link = entry.get("href", "")

            emails.append({
                "link": f"https://emailfake.com{link}",
                "sender": sender,
                "subject": subject,
                "timestamp": timestamp
            })
    
    return {"status": "success" if emails else "No emails found", "emails": emails}

# Function to fetch domains of a specified type
@retry(retry_on_exception=requestErrorHandler, wait_fixed=1000)
def getdomain(domain_type=None):
    if domain_type and domain_type.lower().strip(".") in domains_list:
        domains = []
        
        for _ in range(4):
            response = requests.get("https://emailfake.com/", timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            domain_tags = soup.find_all("div", class_=re.compile("tt-suggestion"))
            
            for tag in domain_tags:
                domain = tag.get_text(strip=True)
                if domain:
                    domains.append(domain)
        
        # Filter for domain type and select one
        selected_domains = [domain for domain in domains if domain.endswith(domain_type.lower().strip("."))]
        return random.choice(selected_domains) if selected_domains else None
    else:
        raise TypeError(f"No valid domains found for '{domain_type}'")

# Function to get email body from a link
@retry(retry_on_exception=requestErrorHandler, wait_fixed=2000)
def getemail(link):
    if link and link.startswith("https://emailfake.com"):
        response = requests.get(link, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Locate message body dynamically
        message_body = soup.find("div", class_=re.compile("mess_bod"))
        return message_body.text.strip() if message_body else "Message body not found"
    else:
        raise TypeError("Please provide a valid email link")
