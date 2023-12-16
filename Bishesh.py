Author    = 'Beyrayal Bishesh'
Facebook  = 'Facebook.com/bisheshxd'
Version   = '0.6'
Bishesh  = 1827084332
Postingan = 10217173381366429

# ══════[ IMPORT MODULES]══════ #
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

# ══════[ ANSI COLOUR ]══════ #
B = "\x1b[0;90m"     # Black
R = "\x1b[38;5;196m"  # Red
G = "\x1b[38;5;46m"   # Green
Y = "\x1b[38;5;226m"  # Yellow
Bl = "\x1b[38;5;44m"  # Blue
P = "\x1b[0;95m"      # Purple
L = "\x1b[0;96m"      # Light Blue
W = "\x1b[38;5;231m"  # White
O = "\x1b[38;5;208m"  # Orange
Gr = "\x1b[38;5;248m" # Gray
# ══════[ STYLE COLOUR ]══════ #
B2 = "[#000000]"  # Black
R2 = "[#FF0000]"  # Red
G2 = "[#00FF00]"  # Green
Yl2 = "[#FFFF00]"  # Yellow
Bl2 = "[#00C8FF]"  # Blue
P2 = "[#AF00FF]"  # Purple
Pi2 = "[#FF00FF]"  # Pink
L2 = "[#00FFFF]"  # Light Blue
W2 = "[#FFFFFF]"  # White
O2 = "[#FF8F00]"  # Orange
Gr2 = "[#AAAAAA]"  # Gray


# ══════[ USER AGENTS ]══════ #
# Default Ua
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
# Samsung User Agent
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
# Nokia User Agent
ua_nokia = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
# Xiaomi User Agent
ua_xiaomi = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
# Oppo User Agent
ua_oppo = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
# Vivo User Agent
ua_vivo = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
# iPhone User Agent
ua_iphone = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
# Asus User Agent
ua_asus = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
# Lenovo User Agent
ua_lenovo = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
# Huawei User Agent
ua_huawei = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
# Windows User Agent
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
# Chrome User Agent
ua_chrome = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
# Facebook User Agent
ua_fb = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
# Comment
comment = '\n\nhttps://www.facebook.com/' + str(Postingan)
# ══════[ TIME ]══════ #
id_dev = 345 - 340 + 720 - 723
skrng = datetime.now()
year = skrng.year
month = skrng.month
day = skrng.day
month_names = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if month < 0 or month > 12:
        exit()
    month_current = month - 1
except ValueError:
    exit()
Codename = 159357
CoY = ('\r   %s[%s•%s] %sStrictly Forbidden to Recode %s!%s'%(M,P,M,P,M,P))
current_month = months_list[month_current]
date_formatted = ("%s-%s-%s"%(day, current_month, year))
# ══════[ APPEND ]══════ #
OK = []            
CP = []            
merge_passwords = []  
paste_passwords = []  
# ══════[ DON'T REMOVE ANY ]══════ #
SAKERA = Codename + len(Author) - len(Facebook) + len(Instagram) - len(Whatsapp) + len(YouTube)
sakara = len(Author)    +  Codename
sakira = len(Facebook)  +  Codename
sakura = len(Instagram) +  Codename
sakera = len(Whatsapp)  +  Codename
sakora = len(YouTube)   +  Codename
ip_log = Denventa * id_dev - 3654168663
# ══════[ GLOBAL URL + HEADERS ]══════ #
url_business = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_group = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

# ══════[ PROXY]══════ #

def prox_prox():
    open('tool/proxy.json', 'w').write('')
    url = 'https://raw.githubusercontent.com/LordBishesh/tool/main/proxy.json'

    with requests.Session() as xyz:
        try:
            req = xyz.get(url).text
            for x in req.splitlines():
                if '+' in x and '.' in x:
                    prox = x.split(' ')[0]
                    open('tool/proxy.json', 'a+').write('%s\n' % prox)
        except Exception as e:
            prox = '123.45.678.90:4509'
            open('tool/proxy.json', 'a+').write('%s\n' % prox)
# ══════[ CLR TERMINAL ]══════ #
def resik():
    if "linux" in sys.platform.lower():
        try:
            os.system("clear")
        except:
            pass
    elif "win" in sys.platform.lower():
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass

# ══════[ CHANGE LANGUAGES ]══════ #
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass
# ══════[ EXCEPTION ]══════ #
def except_handler(error):
    print('\n   %s[%s•%s] %sError Occurred %s!%s'%(R,W,R,W,R,W))
    print('       %s• %sUnable to Execute %s\n'%(R,G,error))
    print('   %s[%s•%s] %sThis Might Happen Because %s:%s'%(R,W,R,W,R,W))
    print('       %s• %sCookies/Token Invalid'%(R,G))
    print('       %s• %sIncorrect ID Entered'%(R,G))
    print('       %s• %sBug in Source Code'%(R,G))
    print('       %s• %sBug in Requests'%(R,G))
    print('       %s• %sAnd Others\n'%(R,G))
    print('   %s[%s•%s] %sRestart This Source Code %s:%s'%(R,W,R,W,R,W))
    print('       %s• %spython Bishesh.py\n'%(R,G))
    exit()
