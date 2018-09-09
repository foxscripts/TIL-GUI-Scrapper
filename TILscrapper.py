import tkinter as tk
from bs4 import BeautifulSoup
import requests

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

url = requests.get('https://www.reddit.com/r/todayilearned/', headers=headers)
urlContent =BeautifulSoup(url.content, "lxml")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.myWindow()

    def myWindow(self):
        self.get_data = tk.Button(root, text="Get Data", command=self.web_data)
        self.get_data.pack(side="top")

        self.data_msg = tk.Label(root, text="Click the Button!")
        self.data_msg.pack()

    def web_data(self):
        for headings in urlContent.find_all('h2'):
            headings = headings.text
            self.data_msg.config(text = "\n" + str(headings))

root = tk.Tk()
root.title("TIL scrapper")
root.geometry("1600x900")
app = Application(master=root)
app.mainloop()