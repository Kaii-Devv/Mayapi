from flask import Flask
from flask_restful import Resource, Api
from random import choice
from flask_cors import CORS
import requests,re

app = Flask(__name__)
api = Api(app)
CORS(app)

class MyApi(Resource):
    def get(self):
        ses = requests.session()
        mail = choice(['catgroup.uk', 'goatmail.uk', 'sendnow.win', 'ccmail.uk', 'exdonuts.com', 'hamham.uk', 'digdig.org', 'owleyes.ch', 'stayhome.li', 'fanclub.pm', 'hotsoup.be', 'simaenaga.com', 'tapi.re', 'fuwari.be', 'magim.be', 'mirai.re', 'moimoi.re', 'heisei.be', 'honeys.be', 'mbox.re', 'uma3.be', 'instaddr.ch', 'quicksend.ch', 'instaddr.win', 'instaddr.uk', 'meruado.uk', 'nekosan.uk', 'niseko.be', 'kpost.be', 'wanko.be', 'mofu.be', 'usako.net', 'eay.jp', 'via.tokyo.jp', 'ichigo.me', 'choco.la', 'cream.pink', 'merry.pink', 'neko2.net', 'fuwamofu.com', 'ruru.be', 'macr2.com', 'f5.si', 'svk.jp'])
        x=ses.get("https://m.kuku.lu/index.php")
        user=""
        c = ses.get("https://m.kuku.lu/id.php").text
        ff=ses.get(f"https://m.kuku.lu/index.php?action=addMailAddrByManual&nopost=1&by_system=1&t={re.search('t=(.*?)&',str(c)).group(1)}&csrf_token_check={re.search('csrf_token_check=(.*?)&',str(c)).group(1)}&newdomain={mail}&newuser={user}&recaptcha_token=&").text.replace("OK:","")
        cok = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        hasil={"email":ff,"cookie":cok}
        if not "@" in str(hasil):
            hasil=auto()
        return hasil
api.add_resource(MyApi, "/auto",methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True,port=8888)
