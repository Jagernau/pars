import requests
import bs4
import html_to_json

class ParsSite:
    def __init__(self, address):
        """Принимает адресс сайта
            хранит словарь title_adress - имя
        картинки_её адресс"""
        self.addres = address
        self.content = requests.get(address, headers = {'User-Agent': 'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2'}).content
        self.js = None
        self.dom = None

    def give_pic_links(self):
        """Составляет словарь = "Имя картинки"
        : "Ссылка на каринку"."""
        dom = self.addres.replace("https://",""). split("/")[0]
        self.dom = dom
        domain = f"https://{dom}"
        content = self.content.decode("utf-8")
        soup = bs4.BeautifulSoup(content, "html.parser")
        img_soup = str(soup.find_all("img"))
        img = html_to_json.convert(img_soup)
        self.js = img

        with open("cool.json", "w") as f:
            f.write(str(soup))
        if len(img) >= 1:
            z = []
            for i in img["img"]:
                a = i["_attributes"]
                for x in a.values():
                    if ".avif" in x:
                        if "https://" in x:
                            z.append(x)
                        else:
                            z.append(f"{domain}{x}")
                                                
                    if ".webp" in x:
                        if "https://" in x:
                            z.append(x)
                        else:
                            z.append(f"{domain}/{x}")
                                                
                    if ".svg" in x:
                        if "https://" in x:
                            z.append(x)
                        else:
                            z.append(f"{domain}/{x}")
                        
                    if ".png" in x:
                        if "https://" in x:
                            z.append(x)
                        else:
                            z.append(f"{domain}/{x}")
                                                
                    if ".jpg" in x:
                        if "https://" in x:
                            z.append(x)
                        else:
                            z.append(f"{domain}/{x}")
        else:
            pass
        with open("comon.json", "w") as f:
            f.write(str(z))
        return z
        
