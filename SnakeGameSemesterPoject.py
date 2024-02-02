import Draw 

import random


CANVAS_SIZE = 500 

# Setting apple and snake size.
canvaSize = 25

# Divinding canvas into a Gridsize: CANVAS_SIZE // canvaSize. 
numCols = CANVAS_SIZE // canvaSize

numRows = CANVAS_SIZE // canvaSize


# Snake: create a 2D list, each item is a body part. 
def makeSnake(size): 
    ans=[] 

    for i in range (size+2): # Starting size of snake at 3. 
        ans.append([0, size-i])
       
    return ans 


# Draw board: display snake, apple and score.
# Draw snake and apple same size, we want to have the same scale.
def drawBoard(snake, appleRow, appleCol, size):  
    # Display apple at random spot.
    Draw.clear()
    
    Draw.setColor(Draw.RED) 

    Draw.filledOval(appleCol*canvaSize, appleRow*canvaSize, canvaSize, canvaSize)  # x,y of apple * its size  
    
    # Draw circle for every body-part of snake.  
    for i in snake: 
        snakeRow = i[0]  
        
        snakeCol = i[1]

        x = snakeCol * canvaSize 
                                 # x,y of snake * its size
        y = snakeRow * canvaSize

        Draw.setColor(Draw.GREEN) 

        Draw.filledRect(x, y, canvaSize, canvaSize) 
    
    # Display score.
    Draw.setColor(Draw.WHITE)

    Draw.setFontSize(14)
    
    Draw.setFontFamily("Courier")

    Draw.string("Point: "+ str(size-1) + "/10", 375, 480) #size starting at 1, starting score = size -1 and increase every time through the loop.
 
    # Increasing snake speed every time snake grow (every win)
    Draw.show(300 - (size * 20))
    


# Moving snake: every time the snake moves, insert new head at front of list in the specified direction, and drop the last body-part. 
def moveSnake(snake, dx, dy): 
    # Get the direction and add dx,dy into the old head to get the new head.
    newHeadRow = snake[0][0] + dy         

    newHeadCol = snake[0][1] + dx 
       
    newSnake = [] 
        
    newSnake.append([newHeadRow, newHeadCol]) 
    
    # Snake equal new(x,y), plus snake body (list) minus last part of old snake.    
    newSnake = newSnake + snake[:-1]    
    
    return newSnake     
          
           
# Snake hitting apple: if x,y positions of head of snake equal x,y position of apple.
def snakeHitApple(snake, appleRow, appleCol):
    # Get x,y of head of snake.
    snakeRow = snake[0][0]

    snakeCol = snake[0][1]
    
    # Compare (x,y)SnakeHead and (x,y)Apple.
    return appleRow == snakeRow and appleCol == snakeCol


# Snake hitting walls: if x,y position of head of snake cross walls/Gridsize.
def snakeHitWalls(snake, numRows, numCols): 
    # Get x,y of head of snake.
    snakeRow = snake[0][0]

    snakeCol = snake[0][1] 

    # Compare (x,y)SnakeHead and x's and y's of walls.
    if snakeRow < 0 or snakeRow >= numRows: 

        return True 

    elif snakeCol < 0 or snakeCol >= numCols:

        return True 

# Snake hitting hitself:if x,y possition of head of snake is found in the x,y positions of other body-part.
def snakeHitItself(snake): 
        return snake[0] in snake[1:]


#Playing the game: 
def playGame(size): 
    # Set x,y position of Apple to a random int.
    appleCol = (random.randint(0,  numCols-1)) # Making sure apple won't appear off the canvas when multiplying the x position by apple size (numCols(20) * canvaSize(25) = 500 OFF CANVA).
    
    appleRow = (random.randint(size+3, numRows-2)) # Making sure apple won't appear: right after the snake in the same row (size+3), or off canvas (numRows(20) * canvaSize(25) = 500 OFF CANVA) or on displayed scored at the last row (numRows-2).

    # Initializing snake
    snake = makeSnake(size)  
    
    # Default direction of snake: Right.
    dx = 1 
        
    dy = 0   
            
    # Loop forever.
    while True: 
        # If key is preesed, get the key, change dx and dy.
        if Draw.hasNextKeyTyped(): 
            typedKey = Draw.nextKeyTyped()
            
            if typedKey == "Left": 
            
                dx = -1 
            
                dy = 0 
            
                
            elif typedKey == "Down": 
            
                dx = 0 
            
                dy = 1 
            
                
            elif typedKey == "Right": 
            
                dx = 1 
            
                dy = 0 
            
              
            elif typedKey == "Up": 
            
                dx = 0 
            
                dy = -1             
                                    
        # Updating Snake with new x,y positions.            
        snake = moveSnake(snake, dx, dy)
        
        # Display the board and play.
        drawBoard(snake, appleRow, appleCol, size)

        if snakeHitApple(snake, appleRow, appleCol): 

            return True    

        
        elif snakeHitWalls(snake, numRows, numCols):

            return False 

        
        elif snakeHitItself(snake):

            return False 

    

def main():  
    # Display Canvas.
    Draw.setCanvasSize(CANVAS_SIZE, CANVAS_SIZE)
    Draw.setBackground(Draw.BLACK) 
    
    # Make the game' pic appear at the start.
    Draw.picture("snake pic.gif",0 ,120)

    Draw.show(500)

    Draw.clear()    

    # Start game, playGame loop and increase size every HitApple, Win after eating 10 apples.
    for size in range(1,3):
        
        # If player lose: HitWalls or itself, display "Game Over" and stop game.
        if playGame(size) == False:
            # Make the game over' pic flash 3 time.
            for i in range(3):

                Draw.clear()

                Draw.picture("game OVER (2).gif", 170, 165)

                Draw.show(500)

                Draw.clear()

                Draw.show(500) 
            
            break   
            
        # If player eat apple 10, display "You Win!".
        elif size == 2:
            for i in range(3):
                # Make the you win' pic flash 3 time.
                Draw.clear()
        
                Draw.picture("WIN.gif", -55, 95)
        
                Draw.show(400)
        
                Draw.clear()
        
                Draw.show(400)              
        
       
 
main()