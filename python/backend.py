from urllib.request import urlopen
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    useful_data = False
    songs=[]
    current_song={}
    state = ""
    def handle_starttag(self, tag, attrs):
        try:
            if (str(tag) == "ul" and dict(attrs)["class"] == "group board_content"):
                    self.useful_data=True
                    code=dict(attrs)["redir"]
                    self.current_song={}
                    self.current_song["code"] = code.split("/")[4]
            if( self.useful_data ==True and str(tag)=="li"):
                self.state = str(dict(attrs)["class"]) #optimize this
        except: 
            pass
    def handle_endtag(self, tag):
        if (str(tag) == "ul"):
            self.songs.append(self.current_song)
            self.useful_data=False
    def handle_data(self, data):
        if (self.useful_data==True):
            if (len(self.state) > 3 and any(self.state in s for s in ["band","title","stats length","stats kbps hd", "stats kbps"])):
                if self.state not in self.current_song :
                    self.current_song[self.state] = data

#url="http://www.goear.com/search/ymca"
#data = urlopen(url).read()
f = open("/home/rob/MyProjects/GoearDownloader/Audios y musica de ymca online.htm","r", encoding='utf-8')
data=f.read().encode('ascii','ignore')
parser=MyHTMLParser()
parser.feed(str(data))
print(parser.songs)
