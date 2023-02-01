#This web scraper will pull the stats out of a webpage and put them into another document

#this imports the request library
import requests

#This defines the function that will run and respond to the user input for the website pulling the
#html code for the website
def page_get_fnc(url):

    web_page_html = requests.get(url)

    return web_page_html
    