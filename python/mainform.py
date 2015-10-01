from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("mainform.glade")

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def onButton1Pressed(self, button):
        print("Button1 Pressed")
        entry = builder.get_object("entry1")
        print(entry.get_text())

builder.connect_signals(Handler())
window = builder.get_object("window1")
window.show_all()
liststore=builder.get_object("liststore1")
liststore.append(["Titolo1","Artista1","53:27","320"])

Gtk.main()
