import requests
import time
from torrequest import TorRequest
from user_agent import generate_user_agent

print "Welcome to EVIL BOT"
site = raw_input("Enter the Site Address : ")
views = input("Enter The number of Viewers : ")

def run():
	ua = generate_user_agent()
headers = {
	"User_Agent":ua,
	"Refer":"http://www.clixsense.com/en/View_Ads"
}
     response = tr.get(site, headers=headers)
#     time.sleep(10)
#     print(response.text)  
     print "["+str(i)+"]" + " Blog View Added With IP:" +  tr.get('http://icanhazip.com').content
     tr.reset_identity()

if __name__ == '__main__':
        with TorRequest() as tr:
	    for i in range(views):
	          run()
