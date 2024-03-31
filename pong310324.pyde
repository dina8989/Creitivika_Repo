mode='вправо'
mode2='вверх'
x=100
y=300
def setup():
    size(600,600)

def draw():
    global mode,x,y,mode2
    background(0)
    # for x
    if x <= 0:
        mode = 'вправо'
    if x >= 600:
        mode = 'влево'
    if mode=='вправо':
        x = x + 4
    if mode=='влево':
        x = x - 4
    
    # for y
    if y <= 600:
        mode2 = 'вверх'
    if mode2=='вверх':
        y = y + 6
    ellipse(x,y,90,90)
    
    #команда для проигрыша
    if y >= 600:
        mode2 = 'вниз'
    if mode2=='вниз':
        push()
        fill(229,63,63)
        textSize(40)
        textMode(CENTER)
        text(u"ты проиграл",180,300)
        pop()
        noLoop()
        
    #  дощечка для "победы"
    if keyPressed and key == CODED:
        if keyCode == LEFT:
            rect_x = rect_x - 4
        if keyCode == RIGHT:
            rect_x = rect_x + 4
    rect(180,500,130,10)

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
        
              
    
