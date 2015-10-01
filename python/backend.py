import urllib.request
import urllib
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    useful_data = False
    songs=[]
    urls= set()
    current_song={}
    state = ""

    def handle_starttag(self, tag, attrs):
        try:
            if (str(tag) == "ul" and dict(attrs)["class"] == "group board_content"):
                    self.useful_data=True
                    code=dict(attrs)["redir"]
                    self.current_song={}
                    self.current_song["url"] = "http://www.goear.com/action/sound/get/" + code.split("/")[4]
            if( self.useful_data ==True and str(tag)=="li"):
                self.state = str(dict(attrs)["class"]) #optimize this
        except: 
            pass

    def handle_endtag(self, tag):
        if (str(tag) == "ul"):
            if(len(self.current_song.items())>1 and self.current_song["url"] not in self.urls):
                self.songs.append(self.current_song)
                self.urls.add(self.current_song["url"])
            self.useful_data=False

    def handle_data(self, data):
        if (self.useful_data==True):
            if (len(self.state) > 3 and any(self.state in s for s in ["band","title","stats length","stats kbps hd", "stats kbps"])):
                if self.state not in self.current_song :
                    if(data!='\\n            '):
                        self.current_song[self.state] = data

title= input ("Please insert song title or author: ")
url="http://www.goear.com/search/" + title.replace(" ", "+")
data = urllib.request.urlopen(url).read()
#f = open("/home/rob/MyProjects/GoearDownloader/Audios y musica de ymca online.htm","r", encoding='utf-8')
#data=f.read().encode('ascii','ignore')
parser=MyHTMLParser()
parser.feed(str(data))

#print(parser.songs)
#exit()

import os 
columnsize=int((os.get_terminal_size().columns-10)/3)
print("#   " + "Title".ljust(columnsize) + "Band".ljust(columnsize) + "Length".ljust(columnsize) + "Kbps")
k=0
for song in parser.songs:
    dsong=dict(song)
    try:
        print(str(k).ljust(3) + " " + dsong["title"].ljust(columnsize) + dsong["band"].ljust(columnsize) + dsong["stats length"].ljust(columnsize) + dsong["stats kbps"].ljust(columnsize))
        #print("URL: " + dsong["url"])
        k+=1
    except: 
        try:
            print(str(k).ljust(3) + " " + dsong["title"].ljust(columnsize) + dsong["band"].ljust(columnsize) + dsong["stats length"].ljust(columnsize) + dsong["stats kbps hd"])
            #print("URL: " + dsong["url"])
            k+=1
        except: pass
answ= input("Which song would you like to download? [Please insert #]: ")
print ("Downloading, please wait...")
urllib.request.urlretrieve(dict(parser.songs[int(answ)])["url"],dict(parser.songs[int(answ)])["title"])
print("Done, have a nice day!")
