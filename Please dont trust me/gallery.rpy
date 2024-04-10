init python:
    gallery = Gallery()

    gallery.button("Ambulance")
    gallery.unlock_image("images/arts/Ambulance.png")


screen gallery:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        add gallery.make_button(name="Ambulance",unlocked="images/arts/Ambulance.png",locked="images/arts/Ambulance.png")
        textbutton "Return" action Return()
