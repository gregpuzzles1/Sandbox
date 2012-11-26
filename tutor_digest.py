from Tkinter import Tk, Frame, Canvas, BOTH

class Avatar(Frame):
    def __init__(self,parent=None,width=100,height=100,ovalness=1,bgFrameColor='Orange',bgCanvasColor='Black'):
        Frame.__init__(self,parent,width=width,height=height,bg=bgFrameColor)
        self.grid()
        #self.grid_propagate(0)

        self.width=width
        self.height=height
        self.ovalness=ovalness
        self.bgFrameColor=bgFrameColor
        self.bgCanvasColor=bgCanvasColor
 
        self.canvas1=Canvas(self,width=width/2,height=height/2,bg=bgCanvasColor,borderwidth=0)
        self.canvas1.grid(row=0,column=0,ipadx=0,ipady=0,padx=0,pady=0)
        self.canvas1.grid_propagate(0)
        self.canvas2=Canvas(self,width=width/2,height=height/2,bg=bgCanvasColor,borderwidth=0)
        self.canvas2.grid(row=1,column=1,ipadx=0,ipady=0,padx=0,pady=0)
        self.canvas2.grid_propagate(0)

        self.draw()
    def draw(self):
        pass
    
if __name__=='__main__':
    root=Tk()
    x=Avatar(parent=root)
    x.mainloop()

