'''Main class for launching program'''
import tkinter as tk
from map import Map
#from ui import UI

def main():
    '''Init program'''
    mapsize = [100, 100]
    
    # Create empty map

    # TODO: Create way to generate same map again and again
    #  

    newMap = Map(mapsize[0],mapsize[1])
    # Generate content for map !!FUNCTION ITSELF WORK IN PROGRESS!!
    newMap.generate()
    newMap.triangulate()
    # Open UI
    # TODO: Create better visualization with information
    window = tk.Tk()
    window.geometry('1200x1200')
    canvas = tk.Canvas(window, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)
    newMap.draw(canvas)
    window.mainloop()

if __name__ == '__main__':
    main()
