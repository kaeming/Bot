import requests
import time
from torrequest import TorRequest
from user_agent import generate_user_agent

ua = generate_user_agent()
headers = {
	"User_Agent":ua,
	"Refer":"http://www.clixsense.com/en/View_Ads"
}

print """\033[1m\033[37m
     _____ ___  ____            ____  _              __     ___                     ____        _                                                     
    |  ___/ _ \/ ___|          | __ )| | ___   __ _  \ \   / (_) _____      _____  | __ )  ___ | |_                                                   
    | |_ | | | \___ \   _____  |  _ \| |/ _ \ / _` |  \ \ / /| |/ _ \ \ /\ / / __| |  _ \ / _ \| __|                                                  
    |  _|| |_| |___) | |_____| | |_) | | (_) | (_| |   \ V / | |  __/\ V  V /\__ \ | |_) | (_) | |_                                                   
    |_|   \___/|____/          |____/|_|\___/ \__, |    \_/  |_|\___| \_/\_/ |___/ |____/ \___/ \__|                                                  
                                              |___/                                                                                                  

                                                                     \033[41m FOS- Fools of Security :)
\033[0m
"""
site = raw_input("Enter your Blog Address : ")
blog = input("Enter The number of Viewers : ")


def run():
     response = tr.get(site, headers=headers)
#     time.sleep(10)
#     print(response.text)  
     print "["+str(i)+"]" + " Blog View Added With IP:" +  tr.get('http://ipecho.net/plain').content
     tr.reset_identity()
  


if __name__ == '__main__':
        with TorRequest() as tr:
	    for i in range(blog):
	          run()
