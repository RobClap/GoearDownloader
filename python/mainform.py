from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("MainForm.glade")

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

Gtk.main()
