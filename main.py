from tkinter import ttk
import tkinter as tk
import Stocks

class Application(tk.Frame):
    
    def __init__(self, master, image):
        self.image = image
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.pack()
        
    def createWindow(self):
        self.window = tk.Label(self.master, image = self.image).place(x=0,y=0,relwidth=1, relheight=1)

    def addTitle(self, tmaster, txt):
        img = tk.PhotoImage(file = 'labelcollection.png')
        label = tk.Label(tmaster, text = txt, image = img, height = 50, bg='black', compound = 'center', font=('Sylfaen', 50, 'italic')).place(relx = 0.5, rely = 0.9, anchor = 'center')
        self.image = img

    def createButton(self, bmaster, btext, bx, by, banchor, bcommand=None):
        button = ttk.Button(bmaster, text = btext, command = bcommand).place(relx=bx, rely=by, anchor=banchor)

    def createTextEntry(self, emaster, ewidth, eheight, ex, ey, eanchor, ename):        
        text = tk.Text(master = emaster, width = ewidth, height = eheight).place(relx=ex, rely=ey, anchor=eanchor)
        label = tk.Label(master = emaster, width = 10, height = 1, text = ename, font=('Sylfaen', 14, 'bold')).place(relx=(ex-0.2),rely=(ey), anchor=eanchor)
                       
    def downloadCollection(self):
        #download to excel spreadsheet
        pass

    def addCollection(self):
        #add to collection
        pass

    def stockWindow(self):
        s = Application(self.master, self.image)
        s.createWindow()
        title = s.addTitle(self.master, 'Stocks')
        
        ticker = s.createTextEntry(self.master, 20, 1, 0.6, 0.235, 'center', 'Ticker:')
        company = s.createTextEntry(self.master, 20, 1, 0.6, 0.315, 'center', 'Company:')
        price = s.createTextEntry(self.master, 20, 1, 0.6, 0.4, 'center', 'Price:')
        
        stock = tk.StringVar()
        ttk.Radiobutton(self.master, text = 'Owned', variable = stock, value = 'Owned').place(relx=0.55, rely=0.475, anchor= 'center')
        ttk.Radiobutton(self.master, text = 'Watching', variable = stock, value = 'Watching').place(relx=0.556, rely=0.51, anchor= 'center')
        s.createButton(self.master, 'Add to Portfolio', 0.565, 0.66, 'center', self.addCollection)
        s.createButton(self.master, 'Menu', 0.05, 0.945, 'sw', self.menuWindow)
        s.createButton(self.master, 'Download Portfolio', 0.98, 0.95, 'se', self.downloadCollection)

    def vinylWindow(self):
        v = Application(self.master, self.image)
        v.createWindow()
        v.addTitle(self.master, 'Vinyl')
        
        v.createButton(self.master, 'Menu', 0.05, 0.945, 'sw', self.menuWindow)
        v.createButton(self.master, 'Download Collection', 0.98, 0.95, 'se', self.downloadCollection)
        v.createButton(self.master, 'Add to collection', 0.565, 0.66, 'center', self.addCollection)

    def watchesWindow(self):
        w = Application(self.master, self.image)
        w.createWindow()
        w.addTitle(self.master, 'Watch')
        
        w.createButton(self.master, 'Menu', 0.05, 0.945, 'sw', self.menuWindow)
        w.createButton(self.master, 'Download Collection', 0.98, 0.95, 'se', self.downloadCollection)
        model = w.createTextEntry(self.master, 20, 1, 0.6, 0.235, 'center', 'Model:')
        company = w.createTextEntry(self.master, 20, 1, 0.6, 0.315, 'center', 'Company:')
        price = w.createTextEntry(self.master, 20, 1, 0.6, 0.4, 'center', 'Price:')
        power = tk.StringVar()
        ttk.Radiobutton(self.master, text = 'Automatic', variable = power, value = 'Automatic').place(relx=0.56, rely=0.475, anchor= 'center')
        ttk.Radiobutton(self.master, text = 'Quartz/Battery', variable = power, value = 'Quartz/Battery').place(relx=0.57, rely=0.505, anchor= 'center')
        w.createButton(self.master, 'Add to collection', 0.565, 0.66, 'center', self.addCollection)
        
    def menuWindow(self):
        m = Application(self.master, self.image)
        m.createWindow()
        m.addTitle(self.master, 'Menu')
        m.createButton(self.master, 'Stocks', 0.35, 0.235, 'center', self.stockWindow)
        m.createButton(self.master, 'Vinyl Collection', 0.357, 0.315, 'center', self.vinylWindow)
        m.createButton(self.master, 'Watch Collection', 0.36, 0.4, 'center', self.watchesWindow)

def main():
    root = tk.Tk()
    root.title("Collection-boi")
    background = tk.PhotoImage(file = 'collection.png')
    app = Application(root, background)
    app.menuWindow()
    root.resizable(False,False)
    root.geometry("1000x600")
    
if __name__ == "__main__": main()
