# Write your code here :-)
from tkinter import ttk
import tkinter as tk
import tkinter.filedialog
import csv
import json
import pandas as pd

collectionList = []

class Application(tk.Frame):

    def __init__(self, master, image, labelBG):
        self.image = image
        self.labelBG = labelBG
        self.master = master
        self.key = 0
        tk.Frame.__init__(self, self.master)

        self.pack()

    def createWindow(self):
        self.window = tk.Label(self.master, image = self.image).place(x=0,y=0,relwidth=1, relheight=1)

    def addTitle(self, tmaster, txt):
        img = tk.PhotoImage(file = 'images//labelcollection.png')
        label = tk.Label(tmaster, text = txt, image = img, width = 200, height = 50, bg='black', compound = 'center', font=('Sylfaen', 50, 'italic')).place(relx = 0.5, rely = 0.9, anchor = 'center')
        self.image = img

    def exportCollection(self):
        file = tk.filedialog.asksaveasfile()
        pdObj = pd.read_json('tempCollection.json')
        csvData = pdObj.to_csv(file, index=False)

    def importCollection(self):
        file = tk.filedialog.askopenfile()
        inFile = pd.read_csv(file)
        inFile.to_json(r'tempImport.json')

    def addCollection(self, data):
        global collectionList
        collectionList.append(data)
        with open('tempCollection.json', 'w') as outfile:
            json.dump(collectionList, outfile)

    def stockWindow(self):
        s = Application(self.master, self.image, self.labelBG)
        s.createWindow()
        title = s.addTitle(self.master, 'Stocks')

        ticker = ttk.Entry(self.master, width = 20, text = 'Ticker:')
        ticker.place(relx = 0.575, rely = 0.235, anchor = 'center')
        company = ttk.Entry(self.master, width = 20, text = 'Company:')
        company.place(relx = 0.575, rely = 0.315, anchor = 'center')
        price = ttk.Entry(self.master, width = 20, text = 'Price:')
        price.place(relx = 0.575, rely = 0.395, anchor = 'center')

        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Ticker', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.235), anchor='center')
        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Company', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.315), anchor='center')
        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Price', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.395), anchor='center')

        stock = tk.StringVar()
        ttk.Radiobutton(self.master, text = 'Owned', variable = stock, value = 'Owned').place(relx=0.55, rely=0.475, anchor= 'center')
        ttk.Radiobutton(self.master, text = 'Watching', variable = stock, value = 'Watching').place(relx=0.556, rely=0.51, anchor= 'center')

        add = ttk.Button(self.master, text = 'Add to Portfolio', command = lambda: self.addCollection(data={"ticker":ticker.get(), "company":company.get(), "price":price.get()})).place(relx=0.565, rely=0.66, anchor='center')
        menu = ttk.Button(self.master, text = 'Menu', command = self.mainWindow).place(relx=0.05, rely=0.945, anchor='sw')

    def vinylWindow(self):
        v = Application(self.master, self.image, self.labelBG)
        v.createWindow()
        v.addTitle(self.master, 'Vinyl')

        album = ttk.Entry(self.master, width = 20, text = 'Album:')
        album.place(relx = 0.575, rely = 0.235, anchor = 'center')
        artist = ttk.Entry(self.master, width = 20, text = 'Artist:')
        artist.place(relx = 0.575, rely = 0.315, anchor = 'center')
        year = ttk.Entry(self.master, width = 20, text = 'Year:')
        year.place(relx = 0.575, rely = 0.395, anchor = 'center')

        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Album', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.235), anchor='center')
        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Artist', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.315), anchor='center')
        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Year', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.395), anchor='center')

        owned = tk.StringVar()
        ttk.Radiobutton(self.master, text = 'Want', variable = owned, value = 'Want').place(relx=0.54, rely=0.475, anchor= 'center')
        ttk.Radiobutton(self.master, text = 'Owned', variable = owned, value = 'Owned').place(relx=0.545, rely=0.505, anchor= 'center')

        add = ttk.Button(self.master, text = 'Add to Collection', command = lambda: self.addCollection(data={"album":album.get(), "artist":artist.get(), "year":year.get()})).place(relx=0.565, rely=0.66, anchor='center')
        menu = ttk.Button(self.master, text = 'Menu', command = self.mainWindow).place(relx=0.05, rely=0.945, anchor='sw')

    def watchesWindow(self):
        w = Application(self.master, self.image, self.labelBG)
        w.createWindow()
        w.addTitle(self.master, 'Watch')

        model = ttk.Entry(self.master, width = 20, text = 'Model:')
        model.place(relx = 0.575, rely = 0.235, anchor = 'center')
        company = ttk.Entry(self.master, width = 20, text = 'Company:')
        company.place(relx = 0.575, rely = 0.315, anchor = 'center')
        price = ttk.Entry(self.master, width = 20, text = 'Price:')
        price.place(relx = 0.575, rely = 0.395, anchor = 'center')

        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Model', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.235), anchor='center')
        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Company', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.315), anchor='center')
        label = ttk.Label(self.master, width = 8, image = self.labelBG, compound = 'center', text = 'Price', font=('Sylfaen', 14, 'normal')).place(relx=0.4,rely=(0.395), anchor='center')

        power = tk.Ssong.txttringVar()
        ttk.Radiobutton(self.master, text = 'Automatic', variable = power, value = 'Automatic').place(relx=0.56, rely=0.475, anchor= 'center')
        ttk.Radiobutton(self.master, text = 'Quartz/Battery', variable = power, value = 'Quartz/Battery').place(relx=0.57, rely=0.505, anchor= 'center')

        add = ttk.Button(self.master, text = 'Add to Collection', command = lambda: self.addCollection(data={"model":model.get(), "company":company.get(), "price":price.get()})).place(relx=0.565, rely=0.66, anchor='center')
        menu = ttk.Button(self.master, text = 'Menu', command = self.mainWindow).place(relx=0.05, rely=0.945, anchor='sw')

    def mainWindow(self):
        m = Application(self.master, self.image, self.labelBG)
        m.createWindow()
        m.addTitle(self.master, 'Menu')
        stocks = ttk.Button(self.master, text = 'Stock Portfolio', command = self.stockWindow).place(relx=0.5,rely=0.235,anchor='center')
        vinyl = ttk.Button(self.master, text = 'Vinyl Collection', command = self.vinylWindow).place(relx=0.5,rely=0.315,anchor='center')
        watch = ttk.Button(self.master, text = 'Watch Collection', command = self.watchesWindow).place(relx=0.5,rely=0.4,anchor='center')

    def createMenuBar(self, master):
        menubar = tk.Menu(master)
        master.config(menu = menubar)
        file = tk.Menu(menubar)
        help_ = tk.Menu(menubar)

        menubar.add_cascade(menu = file, label = "File")
        file.add_separator()
        file.add_command(label = 'New', command = lambda: print('New Collection'))
        file.add_separator()
        file.add_command(label = 'Import', command = self.importCollection)
        file.add_separator()
        file.add_command(label = 'Export', command = self.exportCollection)

        menubar.add_cascade(menu = help_, label = "Help")
        help_.add_separator()
        help_.add_command(label = 'Read Me', command = lambda: print('Read Me'))
        help_.add_separator()

def main():
    root = tk.Tk()
    root.title("Collection-boi")
    background = tk.PhotoImage(file = 'images//collection.png')
    labelbackground = tk.PhotoImage(file = 'images//labelBG.gif')
    labelbackground = labelbackground.subsample(10,20)
    root.resizable(False,False)
    root.geometry("1000x600")

    style = ttk.Style()
    style.theme_use('xpnative')
    style.configure('TButton', background = 'black')

    app = Application(root, background, labelbackground)
    app.mainWindow()
    app.createMenuBar(root)

if __name__ == "__main__": main()
