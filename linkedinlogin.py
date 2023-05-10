#import the necessary libraries
import requests
from bs4 import BeautifulSoup

#set up dictionaries of login credentials and the header to be fed in the POST() or GET() 
#   requests to the website  

data = {
    'session-key' : 'kumarkyle287@gmail.com',
    'session-password' : 'goodlord123'
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}  #user-agent allos data to be accessed that is prevented by the website on certain conditions. 
    #user-agents bypass it by simulating the required conditions

#set up a sessions object that will handle the cookie requests and header update for each request made.
sessions = requests.Session()
sessions.headers.update(headers)
response = sessions.post('https://www.linkedin.com/uas/login-submit', data = data)


# r = requests.get("https://www.linkedin.com/home", data = data, headers = headers)


#small validation block to check if our request was successful
if response.status_code == 200:
    print('Successful')
else:
    print("Unsuccessful")