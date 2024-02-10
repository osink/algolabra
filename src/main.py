'''Main class for launching program'''
import tkinter as tk
from map import Map
#from ui import UI

def main():
    '''Init program'''
    # Open UI
    window = tk.Tk()
    greeting = tk.Label(text="Heiiii")
    greeting.pack()

    window.mainloop()
    # Create empty map
    newMap = Map(50,50)
    # Generate content for map !!FUNCTION ITSELF WORK IN PROGRESS!!
    newMap.generate()
    # Print map
    print(newMap)

if __name__ == '__main__':
    main()
