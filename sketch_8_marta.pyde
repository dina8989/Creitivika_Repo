l=0
qwedfghjkl=0
ra=0
def setup():
    global qwedfghjkl,l,ra
    size(800,800)
    background(247,175,175)
    imageMode(CENTER)
    qwedfghjkl=loadImage("roza.png")
    ra=loadImage("roza1.png")
    
def draw():
    global qwedfghjkl,l,ra
    translate(420,340)
    rotate(radians(l))
    image(qwedfghjkl,0,0,300,350)
    image(qwedfghjkl,480,360,300,350)
    image(qwedfghjkl,440,370,300,350)
    image(qwedfghjkl,490,430,300,350)
    image(qwedfghjkl,410,390,300,350)
    image(ra,420,340,300,350)
    image(ra,410,360,300,350)
    image(ra,370,370,300,350)
    image(ra,400,400,300,350)
    textSize(80)
    fill(255,82,82)
    text(u'с 8 марта ;)',200,660)
