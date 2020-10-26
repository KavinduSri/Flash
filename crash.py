
print(" ▄▀ █▀▀▄ ▄▀▄ ▄▀▀ █░░     ▄▀▀ ▀ ▀█▀ █▀▀ ▄▀▀ ")
print(" █░ █▐█▀ █▀█ ░▀▄ █▀▄     ░▀▄ █ ░█░ █▀▀ ░▀▄ ")
print(" ░▀ ▀░▀▀ ▀░▀ ▀▀░ ▀░▀     ▀▀░ ▀ ░▀░ ▀▀▀ ▀▀░ ")
print("                                   MAKE BY Flash(KS)")


while True:
    import requests as r
    from bs4 import BeautifulSoup as b
    try:
        inp = input("Enter ID: ")
        url = "https://www.google.com/search?q=inurl:.php?id="+inp
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189"}
        res = r.get(url, headers=headers)
        soup = b(res.content, 'html.parser')
        results = soup.find_all("div",{"class":"yuRUbf"})
        h = []
        for i in range(len(results)):
            h.append(results[i].find('a')['href'])
            for k in h:
                print(k)
    except:
        print("None")
  
