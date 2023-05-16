#import the necessary libraries
import time
import requests
from bs4 import BeautifulSoup
import urllib # this library enables use of urllib.parse.quote() function useful for using encoded urls

#---------------------------------------------------------------------------------------------

#function that has the login credentials and header data  
def login_credentials():
    #set up dictionaries of login credentials and the header to be fed in the
    # POST() or GET() requests to the website 
    data = {
        'session-key' : 'kumarkyle287@gmail.com',
        'session-password' : 'goodlord123'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    } #user-agent allows data to be accessed that is prevented by the website 
      #on certain conditions.user-agents bypass it by simulating the required conditions
        
    return data, headers

#--------------------------------------------------------------------------------------------

#function to deal with login requests and handling a session
def login_linkedin():
    try:
        data, headers = login_credentials()
        
        #set up a sessions object that will handle the cookie requests and
        #header update for each request made.
        sessions = requests.Session()
        sessions.headers.update(headers)
        
        #submit your username and password to the wesbite login
        response = sessions.post('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin', data = data)

        #* *raise exception if not successful i.e != 200
        response.raise_for_status()
        print("Login Successful")
    
    #this block catches the exception raised in try block and from the error
    #class it finds the error and assigns it to a variable
    except requests.exceptions.RequestException as e:
        print(f"Login failed {e}")
  
#-------------------------------------------------------------------------------------------

#get request to get the homepage url 
def homepage_request():
    home = requests.get("https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit")
    #print(home.status_code) #this is only for testing and can be omitted in the final code
    

#function to get the search result page urls 
def search_query():
    try:
        user_query = "Jack in the Box"
        search_address = "https://www.linkedin.com/search/results/companies/?heroEntityKey=urn%3Ali%3Aorganization%3A164516&keywords=" + urllib.parse.quote(user_query)
            #the base url is taken from manual navigation. The hero entity is
            #the highlighted company name in search results
        search_get = requests.get(search_address)
        search_get.raise_for_status()
        #if there are no exceptions thrown go next
        print("Successful search")
        soup_search = BeautifulSoup(search_get.text, 'html.parser')
        return soup_search
        # page_text = soup_search.get_text().strip()
        # print(page_text)
    except requests.exceptions.RequestException as fe:
        print(f"Failed {fe}")
        
        
#Just a test function to print results(to check if we are on the right page)
def first_company(soup_object):
    link = soup_object.findAll('a')
    for i in link:
        print(i.prettify())    
        


    

#a main function to unify the function calls       
def main():
    login_linkedin()
    time.sleep(2) # include time delays between requests to bypass antibot and to prevent website overload
    homepage_request()
    time.sleep(1.4)
    # search_query()
    time.sleep(1.9)
    first_company(search_query())

# main script control start
main() 