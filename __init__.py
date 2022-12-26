import requests, os, random
from bs4 import BeautifulSoup
from retrying import retry

__author__ = "ChargeDev"
__version__ = "1.0"

class Start:
    def __init__(self):
        self.valid_domain_types = ["com", "net", "xyz", "org", "info", "me"]


    def requestErrorHandler(exception):
        return True

    @retry(retry_on_exception=requestErrorHandler, wait_fixed=1)
    def getinbox(self, email=None, log=None):
        if email == None:
            raise TypeError("Missing email") 
        
        if type(email) == str:
            email_request = requests.get(f"https://emailfake.com/{email}").text
            beautiful_soup_client = BeautifulSoup(email_request.encode("utf-8"), "html.parser")
            email_list = beautiful_soup_client.find_all("a", {"class": "e7m list-group-item list-group-item-info"})
            if len(email_list) == 0:
                email_list = beautiful_soup_client.find("div", {"class": "e7m list-group-item list-group-item-info"})
                if email_list == None:
                    return {"status": None}
                else:
                    email_link = f"https://emailfake.com/{email}"
                    email_sender = email_list.find("div", {"class": "e7m from_div_45g45gg"}).text
                    email_subject = email_list.find("div", {"class": "e7m subj_div_45g45gg"}).text
                    email_time = email_list.find("div", {"class": "e7m time_div_45g45gg"}).text
                    return {"status": True, "amount": 1, "emails": [{"link": email_link, "sender": email_sender, "subject": email_subject, "timestamp": email_time}]}
            else:
                emails = []
                for email_class in beautiful_soup_client.find_all("a", {"class": "e7m list-group-item waves-effect"}):
                    email_sender = email_class.find("div", {"class": "e7m from_div_45g45gg"}).text
                    email_subject = email_class.find("div", {"class": "e7m subj_div_45g45gg"}).text
                    email_time = email_class.find("div", {"class": "e7m time_div_45g45gg"}).text
                    email_link = email_class['href']
                    emails.append({"link": email_link, "sender": email_sender, "subject": email_subject, "timestamp": email_time})
                
                for email_class in email_list:
                    email_sender = email_class.find("div", {"class": "e7m from_div_45g45gg"}).text
                    email_subject = email_class.find("div", {"class": "e7m subj_div_45g45gg"}).text
                    email_time = email_class.find("div", {"class": "e7m time_div_45g45gg"}).text
                    email_link = email_class['href']
                    emails.append({"link": email_link, "sender": email_sender, "subject": email_subject, "timestamp": email_time})
                
                total_amount = len(beautiful_soup_client.find_all("a", {"class": "e7m list-group-item waves-effect"}))+len(email_list)
                return {"status": True, "amount": total_amount, "emails": emails}
    
    @retry(retry_on_exception=requestErrorHandler, wait_fixed=1)
    def getdomain(self, domain_type=None):
        if not domain_type == None:
            if domain_type.lower().strip(".") in self.valid_domain_types:
                found_domain=False
                various_domains = []
                try:
                    for i in range(4):
                        email_request = requests.get("https://emailfake.com/", timeout=5).text
                        parser_client = BeautifulSoup(email_request.encode("utf-8"), "html.parser")
                        domain_tags = parser_client.find_all("div", "e7m tt-suggestion")
                        for tag in domain_tags:
                            various_domains.append(tag.find("p").text)
                            if not tag == None:
                                found_domain = True
                except:
                    found_domain = False
                
                if found_domain == True:
                    new_domains_end = []
                    for domain in various_domains:
                        if domain.endswith(domain_type.lower().strip(".")):
                            new_domains_end.append(domain)
                    
                    if not len(new_domains_end) == 0:
                        return random.choice(new_domains_end)
                    else:
                        return None
            else:
                raise TypeError(f"No {domain_type} domains found")
        else:
            raise TypeError("Please provide a domain type")

    
    @retry(retry_on_exception=requestErrorHandler, wait_fixed=1)
    def getemail(self, link) -> dict:
        if not link == None:
            if link.startswith("https://emailfake.com"):

                email_request = requests.get(link, timeout=5).text
                beautiful_soup_client = BeautifulSoup(email_request.encode("utf-8"), "html.parser")
                # Search for email found -> dict otherwise found -> False
                message_body = beautiful_soup_client.find("div", {"class": "e7m mess_bodiyy"}).text
                print(message_body)

        else:
            raise TypeError("Please provide a link to your email")
