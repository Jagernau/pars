import ParsClasses as pc
import  ParsFunctions as pf


site = pc.ParsSite("https://geo.pro/reportage/703579-traphousenn-kh-captown/")
links = site.give_pic_links()

print(type(site.content))

    