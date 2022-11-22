from sanic.response import html,json,text
from sanic import Blueprint
import requests
from bs4 import BeautifulSoup
#import mysql.connector

bp = Blueprint('city_data')


""" mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="temporal",
    database="city-data"
)
cursor =  mydb.cursor()
 """

@bp.route('/zipcodes/<zipcode:str>')
async def bp_root(request,zipcode:str):
    URL = "https://www.city-data.com/zips/"+zipcode+".html"
    try: 
        page = requests.get(URL,verify=False)
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"
    soup = BeautifulSoup(page.content,"html.parser")
    print(soup)
    elements = soup.find_all("div", class_="list-group-item col-lg-3 col-sm-4 col-xs-6")
    for element in elements:
        print(element,end="\n"*2)
    return html(page.content)

@bp.route('/city/<city:str>')
async def bp_city(request,city:str):
    URL = "https://www.city-data.com/crime/crime-"+city+".html"
    print(URL)
    try: 
        page = requests.get(URL,verify=False)
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"
    #soup = BeautifulSoup(page.content,"html.parser")
    return html(page.content)

@bp.route('/search/<state:str>')
async def bp_search(request,state:str):
    st_n = states(state)
    #cursor.execute("Select * from states where abbr='"+state+"'")
    #sts = cursor.fetchone()
    URL = "http://www.city-data.com/advanced/schCities.php?csize=a&sc=1&sd=0&states="+st_n+"&near=&nam_crit1=854&b854=MIN&e854=MAX&i854=1&ps=1000&p=0"
    page = requests.get(URL,verify=False)
    return html(page.content)
    
def states(state):
    state = state.upper()
    int_states= {"AL":"01","AK":"02","AZ":"04","AR":"05","CA":"06","CO":"08","CT":"09","DE":"10","DC":"11","FL":"12","GA":"13","HI":"15","ID":"16","IL":"17","IN":"18","IA":"19","KS":"20","KY":"21","LA":"22","ME":"23","MD":"24","MA":"25","MI":"26","MN":"27","MS":"28","MO":"29","MT":"30","NE":"31","NV":"32","NH":"33","NJ":"34","NM":"35","NY":"36","NC":"37","ND":"38","OH":"39","OK":"40","OR":"41","PA":"42","PR":"72","RI":"44","SC":"45","SD":"46","TN":"47","TX":"48","UT":"49","VT":"50","VA":"51","VI":"78","WA":"53","WV":"54","WI":"55","WY":"56"}
    return int_states[state]

""" @bp.middleware
async def print_on_request(request):
    print("This runs on every call")

@bp.middleware('request')
async def halt_request(request):
    return text('I halted the request')

@bp.middleware('response')
async def halt_response(request, response):
    return text('I halted the response')
 """
