
import time
import webbrowser

url = input("Enter url: ")
duration = input('Enter duration: ')
for i in range(15):
    webbrowser.open_new(url)
    time.sleep(int(duration))
