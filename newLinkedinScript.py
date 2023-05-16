#new script 
import requests
from bs4 import BeautifulSoup
import time


def login_details():
    """return login details and other initialization data for page request session"""
    
    login_data = {
        "session_key":"kumarkyle287@gmail.com",
        "session_password":"goodlord123",
        "csrfToken": "ajax:7785454001634787549"
    }    
    
    headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
        }
    
    proxies = {
        'http':"5.161.41.17",
        'https': "5.161.41.17"
    }
    
  
    return login_data, headers, proxies

def login_linkedin():
    try:
        login_data, headers, proxi = login_details()
        login_url ="https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin" 
        sessions = requests.Session()
        sessions.headers.update(headers)
        
     
        r1 = requests.get(login_url, proxies=proxi)
        print(r1.status_code)
        response = sessions.post("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin", data = login_data)
        result = sessions.post(login_url,data = login_data,headers= headers, proxies=proxi)
        response.raise_for_status()
        print("Login Successful")
        
    except requests.exceptions.RequestException as e:
        print(f"Login Failed {e}")
        
        
login_linkedin()
