from OSMsvgFile import OSMsvgFile
import svg

class csvg:
    def __init__(self, file_name: str):
        
        self.fname = file_name
        self.svgfile = OSMsvgFile ()        
        self.svgfile.open ()    
        self.svgfile.open (""" """, 297, 210)
        self.offsetx = 0
        self.offsety = 0
        self.scalex = 1
        self.scaley = 1

    def setcoef (self, offsetx: float, offsety: float, scalex:float, scaley:float):
        self.offsetx = offsetx
        self.offsety = offsety
        self.scalex = scalex
        self.scaley = scaley

    def addlabel (self, x: float, y: float, label: str):
        x1 = x * self.scalex + self.offsetx
        y1 = y * self.scaley + self.offsety
        txt = svg.Text (text=label, x=x1, y=y1)
        txt.style = "font: bold Luciole;font-size:8pt;"
        self.svgfile.addsvg (txt)
        
    def save (self):
        self.svgfile.close ()
        print (self.svgfile.getSVGString ())
        self.svgfile.writeToFile (self.fname)