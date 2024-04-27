y = 40
x = 40
circle_size = 60
circle_speed = 5

# Координаты прямоугольников (препятствий)
rectangles = [
    {"x": 100, "y": 0, "w": 70, "h": 490},
    {"x": 600, "y": 0, "w": 70, "h": 490},
    {"x": 350, "y": 300, "w": 70, "h": 490},
    {"x": 680, "y": 680, "w": 70, "h": 95}
]

def setup():
    size(800, 800)

def draw():
    global x, y
    
    background(115, 133, 232)
    
    # Рисуем препятствия
    fill(71, 91, 160)
    for rect_data in rectangles:
        rect(rect_data["x"], rect_data["y"], rect_data["w"], rect_data["h"])
    
    # Рисуем круг
    fill(24, 61, 201)
    ellipse(x, y, circle_size, circle_size)
    
    # Проверяем столкновения с границами холста и препятствиями
    next_x = x
    next_y = y
    
    if keyPressed:
        if keyCode == UP:
            next_y -= circle_speed
        elif keyCode == DOWN:
            next_y += circle_speed
        elif keyCode == LEFT:
            next_x -= circle_speed
        elif keyCode == RIGHT:
            next_x += circle_speed
    
    # Проверяем, не приведет ли следующее положение круга к столкновению
    can_move = True
    for rect_data in rectangles:
        if (rect_data["x"] < next_x < rect_data["x"] + rect_data["w"] and
                rect_data["y"] < next_y < rect_data["y"] + rect_data["h"]):
            can_move = False
            break
    if not (0 <= next_x <= width and 0 <= next_y <= height):
        can_move = False
    
    # Если можно двигаться, обновляем позицию круга
    if can_move:
        x = next_x
        y = next_y
    else:
        # Если круг касается препятствий или границ холста, возвращаем его в исходное положение
        x = 40
        y = 40
