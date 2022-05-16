import requests
from bs4 import BeautifulSoup
import re
import tldextract

branches = ["cerrahi"]
for branch in branches:
    print("[*] STARTING "+ branch + " [*]")
    start_url = "https://dergipark.org.tr/tr/search?q=" + branch + "&section=articles"
    r = requests.get(start_url)
    html_content = r.text
    soup = BeautifulSoup(html_content, features="html.parser")
    links = []
    for tag in soup.find_all('a', href=True):
        links.append(tag['href'])


    def filter_links(links):
        ext = tldextract.extract(start_url)
        domain = ext.domain
        filtered_links = []
        for link in links:
            if domain in link:
                filtered_links.append(link)
        return filtered_links


    hehe =filter_links(links)
    pdflinks = []
    if hehe:
        for line in hehe:
            if re. search("issue", line):
                pdflinks.append(line)
        
        b = []

        for dlink in pdflinks:
            b = requests.get(dlink)
            
            soup = BeautifulSoup(b.text, features="html.parser")
            linkss = []
            if soup:
                for tag in soup.find_all('a', href=True):
                    
                    linkss.append(tag['href'])
                
                download = []
                for x in linkss:
                    if "download" in x:
                        download.append(x)
                        
                if download[0]:            
                    
                    print("https://dergipark.org.tr"+download[0])                    
                    print ("-------------")
                    pdfurl = "https://dergipark.org.tr" + download[0]
                    r = requests.get(pdfurl, stream=True)
                    fname = str(download[0].split("/")[-1:])
                    
                    with open('./tmp/' + fname + ".pdf", 'wb') as fd:
                        for chunk in r.iter_content(2048):
                            fd.write(chunk)
                else:
                    print("download[0]):" + download[0])
                    continue

            else:
                print("soup:" + soup)
                continue                                        
    else:
       print("hehe:" + hehe)
       continue            