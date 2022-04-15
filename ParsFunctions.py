from requests import get
from yadisk import YaDisk
from progress.bar import ChargingBar

def  save_file(arg, adres = None):
    bar = ChargingBar('Процесс', max=len(arg))

    adr = adres.replace("https://",""). replace("/","_")
    disk = YaDisk(token="AQAAAAAVyse2AAfN4-OYguK_4U1qhRGkX7U7-mc")
    if disk.is_dir(f"/pars/{adr}") == False:
        disk.mkdir(f"/pars/{adr}")
    else:
        pass
    counts = 0
    for i in arg:
        bar.next()
        req = get(i,headers = {'User-Agent': 'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2'})
        if req.status_code == 200:
            counts += 1
            disk.upload_url(i, f"pars/{adr}/{i.replace('https://', '').replace('/', '_')}_{counts}.jpg")
                                   
        else:
            pass
    bar.finish()

    