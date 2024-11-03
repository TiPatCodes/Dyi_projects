import turtle
import random 

# Defining  GLOBAL Variables
WIDTH = 800 # for the window screen width
HEIGHT = 600 # for the window screen width
DELAY   = 150 # this is the millisecond delay
MAXSPEED =  350
BPS  = 15
OFFSET = {
    "up" : (0,20),
    "down" : (0,-20),
    "right" : (20,0),
    "left" : (-20,0)
}
FOOD_SIZE = 25
SNAKE_SIZE = 20
# Defining the list for the snake position
snake =  [[0,0],[SNAKE_SIZE,0],[SNAKE_SIZE,0],[SNAKE_SIZE,0]] # making a snake of the 5 segments
snake_direction  = "up"
score = int()
HIGHEST = 0

#random food point generator 
def get_rndm_food():     
    x = random.randint(- WIDTH/2 + FOOD_SIZE , WIDTH/2 - FOOD_SIZE )
    y = random.randint(- HEIGHT/2 + FOOD_SIZE , HEIGHT/2 - FOOD_SIZE )
    return (x,y)

#distane calculator
def get_distance(pn1, pn2):
    x1,y1 =  pn1
    x2,y2 =  pn2
    dist =  ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return dist

# check for the food collision
def food_collision():
    global food_pos, score , HIGHEST
    if(get_distance(snake[-1],food_pos) < 20):
        food_pos = get_rndm_food()
        food.goto(food_pos)
        score += 1
        if (HIGHEST < score):
            HIGHEST = score
        return True
    return False

#forward motion in particular direction
def forward_motion():
     for segments in snake:
        stmpr.goto(segments[0],segments[1])
        stmpr.stamp()

# for changing the snake direction to Up
def go_up(): 
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

# for changing the snake direction to Down
def go_down(): 
    global snake_direction
    if snake_direction != "up": # has to be u-turn
        snake_direction = "down"

# for changing the snake direction to Left
def go_left(): 
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# for changing the snake direction to Right
def go_right(): 
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

#increase of speed
def incr_speed():
    global DELAY
    DELAY = DELAY - BPS

#decrease of speed
def decr_speed():
    global DELAY
    if DELAY <= MAXSPEED:
        DELAY = DELAY + BPS
def game_loop ():
    global snake,snake_direction,food_pos, score
    snake =  [[0,0],[SNAKE_SIZE,0],[SNAKE_SIZE,0],[SNAKE_SIZE,0]] # making a snake of the 5 segments
    snake_direction  = "up"
    score = 0
    food_pos =  get_rndm_food()
    food.goto(food_pos)
    move_snake()


def move_snake():
    #first we will clear the existing stamps
    stmpr.clearstamps()

    # making cpy of the left most segments of the snake
    new_head = snake[-1].copy()

    # adding pixel to it in horizontal x axis
    new_head[0] += OFFSET[snake_direction][0]

    # adding pixel to it in vertical y axis
    new_head[1] += OFFSET[snake_direction][1]
    
    # adding a collision check 
    if (new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 or new_head[1] < - HEIGHT/2 or new_head[1] > HEIGHT/2):
           game_loop()
           
    else:
        #appending it back to the list
        snake.append(new_head)

        # if food collision is not there then do regular or let it append
        if not food_collision():
            # poping the rightmost one
                snake.pop(0)

        #recalling the forward motion in particular direction
        forward_motion()

        #update screen
        scr.title(f"Score : {score} , HIGHEST : {HIGHEST} , Current speed : {MAXSPEED - DELAY} per second")
        scr.update()

        #Rinse and repeat
        turtle.ontimer(move_snake, DELAY)

    
def main():
    # creating a screen event listener function, which will keep on reading the keyboard event press
    scr.listen()
    
    #creating a event callback functions 
    scr.onkey(go_up,"Up")
    scr.onkey(go_down,"Down")
    scr.onkey(go_left,"Left")
    scr.onkey(go_right,"Right")
    scr.onkey(incr_speed,'i')
    scr.onkey(decr_speed,'d')

    # forward_motion()
    
    game_loop()
    
    
    turtle.done()

   

if __name__== "__main__":

    # Create window /////////
    scr = turtle.Screen()
    scr.setup(WIDTH, HEIGHT)
    # scr.title("SNAKE GAME")
    scr.bgcolor("Cyan")
    # For adding a screen backdrop 
    # scr.bgpic()
    # For adding / registering a shape for the screen update
    # scr.register_shape() 
    scr.tracer(0) # This will turnoff the animation and let us configure the automation by ourselves.

    #Create a turtle /////////
    stmpr = turtle.Turtle()
    stmpr.shape("circle")
    # stmpr.color("yellow")
    stmpr.shapesize(SNAKE_SIZE/20) # it means 100th part of the pixel which is default way of defining the shape size  , this is for pixel controlling.
    # stmpr.stamp() # stamping on that location , by default it starts with the 0,0
    stmpr.penup() # lifting of pen
    # stmpr.goto(10,100) # changing the location
    # stmpr.stamp()

    #Create a food  /////////
    food = turtle.Turtle()
    food.shape("triangle")
    food.color("red")
    food.shapesize(FOOD_SIZE / 20)
    food.penup() # lifting of pen

    main()
