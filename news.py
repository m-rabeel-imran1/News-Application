import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import io 
import webbrowser
class news:
    def __init__(self):
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=47a0d47c78b84790899ed8a96f36eaa9").json()
        self.load_gui()
        self.load_news_item(0)
    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.configure(background="black")
        self.root.resizable(0,0)
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()  
    def get_link(self,url):
        webbrowser.open(url)

    def load_news_item(self,index):
        self.clear()  
        try:
            img_url = self.data["articles"][index]["urlToImage"]
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img)
            label = Label(self.root,image=photo)
            label.pack()
        except:
            img_url = "https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg"
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img)
            label = Label(self.root,image=photo)
            label.pack()

        heading = Label(self.root,text=self.data["articles"][index]["title"],bg="black",fg="white",wraplength=350,justify="center")    
        heading.pack(pady=(10,20))
        heading.config(font=("verdana",15))

        details = Label(self.root,text=self.data["articles"][index]["description"],bg="black",fg="white",wraplength=350,justify="center")    
        details.pack(pady=(2,20))
        details.config(font=("verdana",12))
        

        frame = Frame(self.root,bg="black")
        frame.pack(expand=True,fill=BOTH)
        
        #if index != 0:
        previous = Button(frame,text="Prev",width=16,height=3,command=lambda:self.load_news_item(index-1))
        previous.pack(side=LEFT)

        read = Button(frame,text="Read",width=16,height=3,command=lambda:self.get_link(self.data["articles"][index]["url"]))
        read.pack(side=LEFT)
        
        #if index != len(self.data["articles"])-1:
        next = Button(frame,text="Next",width=16,height=3,command=lambda:self.load_news_item(index+1))
        next.pack(side=LEFT)

        self.root.mainloop()

obj = news()