#
import pygtk
#
pygtk.require('2.0')
#
import gtk
#
 
#
class Simple:
#
     def __init__(self):
#
          self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
#
          self.fenetre.set_position(gtk.WIN_POS_CENTER)
#
          self.fenetre.connect("delete_event", self.evenement_supprimer)
#
          self.box1 = gtk.HBox(False,0)
#
          self.fenetre.add(self.box1)
#
          self.bouton = gtk.Button("Bouton 1")
#
          self.bouton.connect("clicked",self.clicBouton1,None)
#
          self.box1.pack_start(self.bouton,True,False,0)
#
          self.bouton.show()
#
          self.bouton2 = gtk.Button("Bouton 2")
#
          self.bouton2.connect("clicked",self.clicBouton2,None)
#
          self.box1.pack_start(self.bouton2,True,False,0)
#
          self.bouton2.show()
#
          self.box1.show()
#
          self.fenetre.show()
#
     def main(self):
#
          gtk.main()
#
     def evenement_supprimer(self, widget, event, data=None):
#
          gtk.main_quit()
#
          return False
#
     def clicBouton1(self,widget,data=None):
#
          print "Clic bouton 1"
#
     def clicBouton2(self,widget,data=None):
#
          print "Clic bouton 2"
#
          #gtk.main_quit()
#
if __name__ == "__main__":
#
     simple = Simple()
#
     simple.main()
#
 
