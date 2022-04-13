import ParsClasses as pc
import  ParsFunctions as pf

user = input()
site = pc.ParsSite(user)
links = site.give_pic_links()

pf.save_file(links, site.addres)

    