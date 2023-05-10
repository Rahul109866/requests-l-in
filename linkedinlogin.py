#import the necessary libraries
import requests
from bs4 import BeautifulSoup


#function that has the login credentials and header data  
def login_credentials():
    #set up dictionaries of login credentials and the header to be fed in the POST() or GET() 
#   requests to the website 
    data = {
        'session-key' : 'kumarkyle287@gmail.com',
        'session-password' : 'goodlord123'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }  #user-agent allows data to be accessed that is prevented by the website on certain conditions. 
        #user-agents bypass it by simulating the required conditions
        
    return data, headers


#function to deal with login requests and handling a session
def login_linkedin():
    try:
        data, headers = login_credentials()
        #set up a sessions object that will handle the cookie requests and header update for each request made.
        sessions = requests.Session()
        sessions.headers.update(headers)
        response = sessions.post('https://www.linkedin.com/uas/login-submit', data = data)

        #raise exception if not successful i.e != 200
        response.raise_for_status()
        print("Login Sucessful")
    
    #this block catches the exception raised in try block and from the error class it finds the error and assigns it to a variable
    except requests.exceptions.RequestException as e:
        print(f"Login failed {e}")
  

#a main fucntion to unify the function calls       
def main():
    login_linkedin()
    
main()