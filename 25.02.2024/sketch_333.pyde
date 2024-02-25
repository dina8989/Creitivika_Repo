r=1
g=1
b=1
s=5
def setup():
    size(300,300)
    background (255,255,255)
def draw():
    global r,g,b,s
    push()
    stroke(r,g,b)
    strokeWeight(s)
    line(mouseX,mouseY,pmouseX,pmouseY)
    pop()
    
    rect(10,20,50,40)
    rect(70,20,50,40)
    rect(130,20,50,40)
def mouseClicked():
    global r,g,b,s
    if mouseX > 10 and mouseX < 60 and mouseY > 20 and mouseY < 20+40:
        r=random(255)
        g=random(255)
        b=random(255)
    if mouseX > 70 and mouseX < 120 and mouseY > 20 and mouseY < 20+40:    
        background(255,255,255)
    if mouseX > 130 and mouseX < 180 and mouseY > 20 and mouseY < 20+40: 
        s=s+10
        
