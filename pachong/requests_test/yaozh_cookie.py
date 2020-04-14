import requests
import time


class Login_Yaozh():
    def __init__(self):
        self.url = "https://www.yaozh.com/member"
        self.login_url = "https://www.yaozh.com/login"
        self.header = {
                "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko)Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36"
        }
        self.name = "wangyiqing8866"
        self.passwd = "wyq123456789"
        self.cookie_path = "./cookie.txt"
        self.login_data = {
                "username":self.name,
                "pwd":self.passwd,
                "formhash":"900CCA214B",
                "backurl":self.url
        }

    def handle_cookie(self):
        index = 0
        size_1 = 0
        size_2 = 0
        with open(self.cookie_path,"r") as f:
            while(1):
                content = f.read(20)
                if content=="":
                    return
                if content.find(";") == -1:
                    size_1+=20+1
                    f.seek(size_1)
                else:
                    size_1+=content.find(";")+1
                    f.seek(size_2)
                    content_p = f.read(size_1-size_2-1)
                    size_2 = size_1
                    f.seek(size_1)
                    yield content_p


    def save_data(self,data):
        #response = requests.get(self.url,headers=self.header)
        #data = response.content.decode("utf8")
        with open("member.html","w") as f:
            f.write(data)

    def shoudong_cookie(self):
        self.cookie_dict = {
                content.split("=")[0].strip():content.split("=")[1].strip() for content in self.handle_cookie()
        }
        response  = requests.get(self.url,headers=self.header,cookies=self.cookie_dict)
        data = response.content.decode("utf8")
        self.save_data(data)

    def auto_login(self):
        session = requests.session()
        session.post(self.login_url,headers=self.header,data=self.login_data)
        response = session.get(self.url,headers=self.header)
        data = response.content.decode("utf8")
        self.save_data(data)

    def run(self):
        self.member()

login = Login_Yaozh()
login.auto_login()
