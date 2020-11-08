from graphics import *
import random
from math import *
import time


run = True
offset = time.time()
win = GraphWin("Physics Sandbox",1000,800,autoflush= False)
win.setCoords(0,0,100,100)
update(60)

g = 0.1
Force=0

theta = pi/6
mass = 10 # 0 - 100
elasticity = 1 
ballVx = 0 
ballVy = 0 
ballPosx=50 
ballPosy=50 
dballVx=0
dballVy=0


#Menu Interface Small
menuBoxSmall = Rectangle(Point(1,1),Point(5,4.5))
menuBoxSmall.draw(win)
menuBoxSmallBar1 = Rectangle(Point(1.5,1.5),Point(4.5,2))
menuBoxSmallBar1.draw(win)
menuBoxSmallBar2 = Rectangle(Point(1.5,2.5),Point(4.5,3))
menuBoxSmallBar2.draw(win)
menuBoxSmallBar3 = Rectangle(Point(1.5,3.5),Point(4.5,4))
menuBoxSmallBar3.draw(win)

#Run Button
runButton = Rectangle(Point(95,1),Point(99,5))
runButton.draw(win)
runButtonPlay = Polygon(Point(96.333,1.75),Point(96.333,4.25),Point(97.888,3))
runButtonStop = Rectangle(Point(96.333,2),Point(97.888,4))
runButtonPlay.draw(win)

while run:
    windowTime = time.time() - offset
    #Checks current key and mouse position. Refreshes every loop
    currentKey = win.checkKey()
    currentMouse = win.checkMouse()
    
    #Opens the menu when menu button is clicked
    if currentMouse != None and currentMouse.getX() >= 1 and currentMouse.getX() <= 5 and currentMouse.getY() >= 1 and currentMouse.getY() <= 4.5:
        
            menuRun = True
            
            #Menu Interface Main
            menuBoxLarge = Rectangle(Point(0,0),Point(20,100))
            menuBoxLarge.setFill("white")
            menuBoxLarge.draw(win)
     
            #Menu Option 1: Gravity
            menuBoxLargeBallGravity = Rectangle(Point(1,86),Point(19,95))
            menuBoxLargeBallGravity.draw(win)
            menuBoxLargeBallGravityText = Text(Point(10,90.5),"Gravity")
            menuBoxLargeBallGravityText.setSize(24)
            menuBoxLargeBallGravityText.setFace("times roman")
            menuBoxLargeBallGravityText.draw(win)            

            #Menu Option 2: Mass
            menuBoxLargeBallMass = Rectangle(Point(1,76),Point(19,85))
            menuBoxLargeBallMass.draw(win)
            menuBoxLargeBallMassText = Text(Point(10,80.5),"Mass")
            menuBoxLargeBallMassText.setSize(24)
            menuBoxLargeBallMassText.setFace("times roman")
            menuBoxLargeBallMassText.draw(win)
            
            #Menu Option 3: Elasticity
            menuBoxLargeBallElasticity = Rectangle(Point(1,66),Point(19,75))
            menuBoxLargeBallElasticity.draw(win)
            menuBoxLargeBallElasticityText = Text(Point(10,70.5),"Elasticity (Bounciness)")
            menuBoxLargeBallElasticityText.setSize(16)
            menuBoxLargeBallElasticityText.setFace("times roman")
            menuBoxLargeBallElasticityText.draw(win)
            
            #Menu Option 4: Ball V X
            menuBoxLargeBallVX = Rectangle(Point(1,56),Point(19,65))
            menuBoxLargeBallVX.draw(win)
            menuBoxLargeBallVXText = Text(Point(10,60.5),"Horizontal Velocity")
            menuBoxLargeBallVXText.setSize(16)
            menuBoxLargeBallVXText.setFace("times roman")
            menuBoxLargeBallVXText.draw(win)

            #Menu Option 5: Ball V Y
            menuBoxLargeBallVY = Rectangle(Point(1,46),Point(19,55))
            menuBoxLargeBallVY.draw(win)
            menuBoxLargeBallVYText = Text(Point(10,50.5),"Vertical Velocity")
            menuBoxLargeBallVYText.setSize(16)
            menuBoxLargeBallVYText.setFace("times roman")
            menuBoxLargeBallVYText.draw(win)

            #Menu Option 6: Ball Pos X
            menuBoxLargeBallPosX = Rectangle(Point(1,36),Point(19,45))
            menuBoxLargeBallPosX.draw(win)
            menuBoxLargeBallPosXText = Text(Point(10,40.5),"Horizontal Position ")
            menuBoxLargeBallPosXText.setSize(15)
            menuBoxLargeBallPosXText.setFace("times roman")
            menuBoxLargeBallPosXText.draw(win)

            #Menu Option 7: Ball Pos Y
            menuBoxLargeBallPosY = Rectangle(Point(1,26),Point(19,35))
            menuBoxLargeBallPosY.draw(win)
            menuBoxLargeBallPosYText = Text(Point(10,30.5),"Vertical Position")
            menuBoxLargeBallPosYText.setSize(16)
            menuBoxLargeBallPosYText.setFace("times roman")
            menuBoxLargeBallPosYText.draw(win)

            #Menu Escape Menu Visual
            menuBoxLargeCloseMenu = Rectangle(Point(1,16),Point(19,25))
            menuBoxLargeCloseMenu.draw(win)
            menuBoxLargeCloseMenuText = Text(Point(10,20.5),"Close Menu")
            menuBoxLargeCloseMenuText.setSize(24)
            menuBoxLargeCloseMenuText.setFace("times roman")
            menuBoxLargeCloseMenuText.draw(win)

            #Menu Interface Escape Sandbox Visual
            menuBoxLargeCloseSandbox = Rectangle(Point(1,6),Point(19,15))
            menuBoxLargeCloseSandbox.draw(win)
            menuBoxLargeCloseSandboxText = Text(Point(10,10.5),"Exit Sandbox")
            menuBoxLargeCloseSandboxText.setSize(24)
            menuBoxLargeCloseSandboxText.setFace("times roman")
            menuBoxLargeCloseSandboxText.draw(win)

            #Menu Interface Funtions
            while menuRun:
                currentMouseMenu = win.checkMouse()

                #Menu Option 1: Gravity
                if currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 86 and currentMouseMenu.getY() <= 95:

                    menuOption1Gravity = Rectangle(Point(25,45),Point(75,75))
                    menuOption1Gravity.setFill("white")
                    menuOption1Gravity.draw(win)
                        
                    menuOption1GravityAdd = Rectangle(Point(64,46),Point(74,56))
                    menuOption1GravityAdd.draw(win)
                    menuOption1GravityAddText = Text(Point(69,51),"+")
                    menuOption1GravityAddText.setSize(36)
                    menuOption1GravityAddText.setFace("times roman")
                    menuOption1GravityAddText.draw(win)

                    menuOption1GravityMinus = Rectangle(Point(26,46),Point(36,56))
                    menuOption1GravityMinus.draw(win)
                    menuOption1GravityMinusText = Text(Point(31,51),"-")
                    menuOption1GravityMinusText.setSize(36)
                    menuOption1GravityMinusText.setFace("times roman")
                    menuOption1GravityMinusText.draw(win)

                    menuOption1GravityEscape = Rectangle(Point(26,69),Point(31,74))
                    menuOption1GravityEscape.draw(win)
                    menuOption1GravityEscapeText = Text(Point(28.5,71.5),"X")
                    menuOption1GravityEscapeText.setSize(28)                        
                    menuOption1GravityEscapeText.setFace("times roman")
                    menuOption1GravityEscapeText.draw(win)

                    menuOption1GravityCurrentText = Text(Point(50,65),str(round(g,1)) + " m/s/s")
                    menuOption1GravityCurrentText.setSize(36)
                    menuOption1GravityCurrentText.setFace("times roman")
                    menuOption1GravityCurrentText.draw(win)
                    
                    while True:
                        currentMouseOption1 = win.checkMouse()
                        #Check Add Button
                        if currentMouseOption1 != None and currentMouseOption1.getX() >= 64 and currentMouseOption1.getX() <= 74 and currentMouseOption1.getY() >= 46 and currentMouseOption1.getY() <= 56:
                            g += 0.1
                            if g > 10:
                                g = 10
                            menuOption1GravityCurrentText.setText(str(round(g,1)) + " m/s/s")
                        #Check Minus Button
                        elif currentMouseOption1 != None and currentMouseOption1.getX() >= 26 and currentMouseOption1.getX() <= 36 and currentMouseOption1.getY() >= 46 and currentMouseOption1.getY() <= 56:
                            g -= 0.1
                            if g < 0:
                                g = 0
                            menuOption1GravityCurrentText.setText(str(round(g,1)) + " m/s/s")

                        #Check Close Button
                        if currentMouseOption1 != None and currentMouseOption1.getX() >= 26 and currentMouseOption1.getX() <= 31 and currentMouseOption1.getY() >= 69 and currentMouseOption1.getY() <= 74:
                            menuOption1Gravity.undraw()
                            menuOption1GravityAdd.undraw()
                            menuOption1GravityAddText.undraw()
                            menuOption1GravityMinus.undraw()
                            menuOption1GravityMinusText.undraw()
                            menuOption1GravityEscape.undraw()
                            menuOption1GravityEscapeText.undraw()
                            menuOption1GravityCurrentText.undraw()
                            break

                #Menu Option 2: Mass
                if currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 76 and currentMouseMenu.getY() <= 85:

                    menuOption2Mass = Rectangle(Point(25,45),Point(75,75))
                    menuOption2Mass.setFill("white")
                    menuOption2Mass.draw(win)
                        
                    menuOption2MassAdd = Rectangle(Point(64,46),Point(74,56))
                    menuOption2MassAdd.draw(win)
                    menuOption2MassAddText = Text(Point(69,51),"+")
                    menuOption2MassAddText.setSize(36)
                    menuOption2MassAddText.setFace("times roman")
                    menuOption2MassAddText.draw(win)

                    menuOption2MassMinus = Rectangle(Point(26,46),Point(36,56))
                    menuOption2MassMinus.draw(win)
                    menuOption2MassMinusText = Text(Point(31,51),"-")
                    menuOption2MassMinusText.setSize(36)
                    menuOption2MassMinusText.setFace("times roman")
                    menuOption2MassMinusText.draw(win)

                    menuOption2MassEscape = Rectangle(Point(26,69),Point(31,74))
                    menuOption2MassEscape.draw(win)
                    menuOption2MassEscapeText = Text(Point(28.5,71.5),"X")
                    menuOption2MassEscapeText.setSize(28)                        
                    menuOption2MassEscapeText.setFace("times roman")
                    menuOption2MassEscapeText.draw(win)

                    menuOption2MassCurrentText = Text(Point(50,65),str(mass) + " kg")
                    menuOption2MassCurrentText.setSize(36)
                    menuOption2MassCurrentText.setFace("times roman")
                    menuOption2MassCurrentText.draw(win)
                    
                    while True:
                        currentMouseOption2 = win.checkMouse()
                        #Check Add Button
                        if currentMouseOption2 != None and currentMouseOption2.getX() >= 64 and currentMouseOption2.getX() <= 74 and currentMouseOption2.getY() >= 46 and currentMouseOption2.getY() <= 56:
                            mass += 1
                            if mass > 100:
                                mass = 100
                            menuOption2MassCurrentText.setText(str(mass) + " kg")
                        #Check Minus Button
                        elif currentMouseOption2 != None and currentMouseOption2.getX() >= 26 and currentMouseOption2.getX() <= 36 and currentMouseOption2.getY() >= 46 and currentMouseOption2.getY() <= 56:
                            mass -= 1
                            if mass < 0:
                                mass = 0
                            menuOption2MassCurrentText.setText(str(mass) + " kg")
                        #Check Close Button
                        elif currentMouseOption2 != None and currentMouseOption2.getX() >= 26 and currentMouseOption2.getX() <= 31 and currentMouseOption2.getY() >= 69 and currentMouseOption2.getY() <= 74:
                            menuOption2Mass.undraw()
                            menuOption2MassAdd.undraw()
                            menuOption2MassAddText.undraw()
                            menuOption2MassMinus.undraw()
                            menuOption2MassMinusText.undraw()
                            menuOption2MassEscape.undraw()
                            menuOption2MassEscapeText.undraw()
                            menuOption2MassCurrentText.undraw()
                            break


                #Menu Option 3: Elasticity
                if currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 66 and currentMouseMenu.getY() <= 75:

                    menuOption3Elasticity = Rectangle(Point(25,45),Point(75,75))
                    menuOption3Elasticity.setFill("white")
                    menuOption3Elasticity.draw(win)
                        
                    menuOption3ElasticityAdd = Rectangle(Point(64,46),Point(74,56))
                    menuOption3ElasticityAdd.draw(win)
                    menuOption3ElasticityAddText = Text(Point(69,51),"+")
                    menuOption3ElasticityAddText.setSize(36)
                    menuOption3ElasticityAddText.setFace("times roman")
                    menuOption3ElasticityAddText.draw(win)

                    menuOption3ElasticityMinus = Rectangle(Point(26,46),Point(36,56))
                    menuOption3ElasticityMinus.draw(win)
                    menuOption3ElasticityMinusText = Text(Point(31,51),"-")
                    menuOption3ElasticityMinusText.setSize(36)
                    menuOption3ElasticityMinusText.setFace("times roman")
                    menuOption3ElasticityMinusText.draw(win)

                    menuOption3ElasticityEscape = Rectangle(Point(26,69),Point(31,74))
                    menuOption3ElasticityEscape.draw(win)
                    menuOption3ElasticityEscapeText = Text(Point(28.5,71.5),"X")
                    menuOption3ElasticityEscapeText.setSize(28)                        
                    menuOption3ElasticityEscapeText.setFace("times roman")
                    menuOption3ElasticityEscapeText.draw(win)

                    menuOption3ElasticityCurrentText = Text(Point(50,65),str(100*round(elasticity,1)) + "% elasticity")
                    menuOption3ElasticityCurrentText.setSize(36)
                    menuOption3ElasticityCurrentText.setFace("times roman")
                    menuOption3ElasticityCurrentText.draw(win)
                    
                    while True:
                        currentMouseOption3 = win.checkMouse()
                        #Check Add Button
                        if currentMouseOption3 != None and currentMouseOption3.getX() >= 64 and currentMouseOption3.getX() <= 74 and currentMouseOption3.getY() >= 46 and currentMouseOption3.getY() <= 56:
                            elasticity += 0.1
                            if elasticity > 1:
                                elasticity = 1
                            menuOption3ElasticityCurrentText.setText(str(100*round(elasticity,1)) + "% elasticity")
                        #Check Minus Button
                        elif currentMouseOption3 != None and currentMouseOption3.getX() >= 26 and currentMouseOption3.getX() <= 36 and currentMouseOption3.getY() >= 46 and currentMouseOption3.getY() <= 56:
                            elasticity -= 0.1
                            if elasticity < 0:
                                elasticity = 0
                            menuOption3ElasticityCurrentText.setText(str(100*round(elasticity,1)) + "% elasticity")
                        #Check Close Button
                        elif currentMouseOption3 != None and currentMouseOption3.getX() >= 26 and currentMouseOption3.getX() <= 31 and currentMouseOption3.getY() >= 69 and currentMouseOption3.getY() <= 74:
                            menuOption3Elasticity.undraw()
                            menuOption3ElasticityAdd.undraw()
                            menuOption3ElasticityAddText.undraw()
                            menuOption3ElasticityMinus.undraw()
                            menuOption3ElasticityMinusText.undraw()
                            menuOption3ElasticityEscape.undraw()
                            menuOption3ElasticityEscapeText.undraw()
                            menuOption3ElasticityCurrentText.undraw()
                            break


                #Menu Option 4: Ball Vx Change
                if currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 56 and currentMouseMenu.getY() <= 65:

                    menuOption4ballVxChange = Rectangle(Point(25,45),Point(75,75))
                    menuOption4ballVxChange.setFill("white")
                    menuOption4ballVxChange.draw(win)
                        
                    menuOption4ballVxChangeAdd = Rectangle(Point(64,46),Point(74,56))
                    menuOption4ballVxChangeAdd.draw(win)
                    menuOption4ballVxChangeAddText = Text(Point(69,51),"+")
                    menuOption4ballVxChangeAddText.setSize(36)
                    menuOption4ballVxChangeAddText.setFace("times roman")
                    menuOption4ballVxChangeAddText.draw(win)

                    menuOption4ballVxChangeMinus = Rectangle(Point(26,46),Point(36,56))
                    menuOption4ballVxChangeMinus.draw(win)
                    menuOption4ballVxChangeMinusText = Text(Point(31,51),"-")
                    menuOption4ballVxChangeMinusText.setSize(36)
                    menuOption4ballVxChangeMinusText.setFace("times roman")
                    menuOption4ballVxChangeMinusText.draw(win)

                    menuOption4ballVxChangeEscape = Rectangle(Point(26,69),Point(31,74))
                    menuOption4ballVxChangeEscape.draw(win)
                    menuOption4ballVxChangeEscapeText = Text(Point(28.5,71.5),"X")
                    menuOption4ballVxChangeEscapeText.setSize(28)                        
                    menuOption4ballVxChangeEscapeText.setFace("times roman")
                    menuOption4ballVxChangeEscapeText.draw(win)

                    menuOption4ballVxChangeCurrentText = Text(Point(50,65),str(ballVx) + " m/s")
                    menuOption4ballVxChangeCurrentText.setSize(36)
                    menuOption4ballVxChangeCurrentText.setFace("times roman")
                    menuOption4ballVxChangeCurrentText.draw(win)
                    
                    while True:
                        currentMouseOption4 = win.checkMouse()
                        #Check Add Button
                        if currentMouseOption4 != None and currentMouseOption4.getX() >= 64 and currentMouseOption4.getX() <= 74 and currentMouseOption4.getY() >= 46 and currentMouseOption4.getY() <= 56:
                            ballVx += 1
                            if ballVx > 10:
                                ballVx = 10
                            menuOption4ballVxChangeCurrentText.setText(str(ballVx) + " m/s")
                            #ballVx/= 100

                        #Check Minus Button
                        elif currentMouseOption4 != None and currentMouseOption4.getX() >= 26 and currentMouseOption4.getX() <= 36 and currentMouseOption4.getY() >= 46 and currentMouseOption4.getY() <= 56:
                            ballVx -= 1
                            if ballVx < -10:
                                ballVx = -10
                            menuOption4ballVxChangeCurrentText.setText(str(ballVx) + " m/s")
                            #ballVx/= 100

                        #Check Close Button
                        elif currentMouseOption4 != None and currentMouseOption4.getX() >= 26 and currentMouseOption4.getX() <= 31 and currentMouseOption4.getY() >= 69 and currentMouseOption4.getY() <= 74:
                            menuOption4ballVxChange.undraw()
                            menuOption4ballVxChangeAdd.undraw()
                            menuOption4ballVxChangeAddText.undraw()
                            menuOption4ballVxChangeMinus.undraw()
                            menuOption4ballVxChangeMinusText.undraw()
                            menuOption4ballVxChangeEscape.undraw()
                            menuOption4ballVxChangeEscapeText.undraw()
                            menuOption4ballVxChangeCurrentText.undraw()
                            break


                #Menu Option 5: Ball Vy Change
                if currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 46 and currentMouseMenu.getY() <= 55:

                    menuOption5ballVyChange = Rectangle(Point(25,45),Point(75,75))
                    menuOption5ballVyChange.setFill("white")
                    menuOption5ballVyChange.draw(win)
                        
                    menuOption5ballVyChangeAdd = Rectangle(Point(64,46),Point(74,56))
                    menuOption5ballVyChangeAdd.draw(win)
                    menuOption5ballVyChangeAddText = Text(Point(69,51),"+")
                    menuOption5ballVyChangeAddText.setSize(36)
                    menuOption5ballVyChangeAddText.setFace("times roman")
                    menuOption5ballVyChangeAddText.draw(win)

                    menuOption5ballVyChangeMinus = Rectangle(Point(26,46),Point(36,56))
                    menuOption5ballVyChangeMinus.draw(win)
                    menuOption5ballVyChangeMinusText = Text(Point(31,51),"-")
                    menuOption5ballVyChangeMinusText.setSize(36)
                    menuOption5ballVyChangeMinusText.setFace("times roman")
                    menuOption5ballVyChangeMinusText.draw(win)

                    menuOption5ballVyChangeEscape = Rectangle(Point(26,69),Point(31,74))
                    menuOption5ballVyChangeEscape.draw(win)
                    menuOption5ballVyChangeEscapeText = Text(Point(28.5,71.5),"X")
                    menuOption5ballVyChangeEscapeText.setSize(28)                        
                    menuOption5ballVyChangeEscapeText.setFace("times roman")
                    menuOption5ballVyChangeEscapeText.draw(win)

                    menuOption5ballVyChangeCurrentText = Text(Point(50,65),str(ballVy) + " m/s")
                    menuOption5ballVyChangeCurrentText.setSize(36)
                    menuOption5ballVyChangeCurrentText.setFace("times roman")
                    menuOption5ballVyChangeCurrentText.draw(win)
                    
                    while True:
                        currentMouseOption5 = win.checkMouse()
                        #Check Add Button
                        if currentMouseOption5 != None and currentMouseOption5.getX() >= 64 and currentMouseOption5.getX() <= 74 and currentMouseOption5.getY() >= 46 and currentMouseOption5.getY() <= 56:
                            ballVy += 1
                            if ballVy > 10:
                                ballVy = 10
                            menuOption5ballVyChangeCurrentText.setText(str(ballVy) + " m/s")
                            #ballVy/= 100
                        #Check Minus Button
                        elif currentMouseOption5 != None and currentMouseOption5.getX() >= 26 and currentMouseOption5.getX() <= 36 and currentMouseOption5.getY() >= 46 and currentMouseOption5.getY() <= 56:
                            ballVy -= 1
                            if ballVy < -10:
                                ballVy = -10
                            menuOption5ballVyChangeCurrentText.setText(str(ballVy) + " m/s")
                            #ballVy/= 100

                        #Check Close Button
                        elif currentMouseOption5 != None and currentMouseOption5.getX() >= 26 and currentMouseOption5.getX() <= 31 and currentMouseOption5.getY() >= 69 and currentMouseOption5.getY() <= 74:
                            menuOption5ballVyChange.undraw()
                            menuOption5ballVyChangeAdd.undraw()
                            menuOption5ballVyChangeAddText.undraw()
                            menuOption5ballVyChangeMinus.undraw()
                            menuOption5ballVyChangeMinusText.undraw()
                            menuOption5ballVyChangeEscape.undraw()
                            menuOption5ballVyChangeEscapeText.undraw()
                            menuOption5ballVyChangeCurrentText.undraw()
                            break


                #Menu Option 6: Ball Pos X Change
                if currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 36 and currentMouseMenu.getY() <= 45:

                    menuOption6BallPosXChange = Rectangle(Point(25,45),Point(75,75))
                    menuOption6BallPosXChange.setFill("white")
                    menuOption6BallPosXChange.draw(win)
                        
                    menuOption6BallPosXChangeAdd = Rectangle(Point(64,46),Point(74,56))
                    menuOption6BallPosXChangeAdd.draw(win)
                    menuOption6BallPosXChangeAddText = Text(Point(69,51),"+")
                    menuOption6BallPosXChangeAddText.setSize(36)
                    menuOption6BallPosXChangeAddText.setFace("times roman")
                    menuOption6BallPosXChangeAddText.draw(win)

                    menuOption6BallPosXChangeMinus = Rectangle(Point(26,46),Point(36,56))
                    menuOption6BallPosXChangeMinus.draw(win)
                    menuOption6BallPosXChangeMinusText = Text(Point(31,51),"-")
                    menuOption6BallPosXChangeMinusText.setSize(36)
                    menuOption6BallPosXChangeMinusText.setFace("times roman")
                    menuOption6BallPosXChangeMinusText.draw(win)

                    menuOption6BallPosXChangeEscape = Rectangle(Point(26,69),Point(31,74))
                    menuOption6BallPosXChangeEscape.draw(win)
                    menuOption6BallPosXChangeEscapeText = Text(Point(28.5,71.5),"X")
                    menuOption6BallPosXChangeEscapeText.setSize(28)                        
                    menuOption6BallPosXChangeEscapeText.setFace("times roman")
                    menuOption6BallPosXChangeEscapeText.draw(win)

                    menuOption6BallPosXChangeCurrentText = Text(Point(50,65),str(ballPosx) + " m")
                    menuOption6BallPosXChangeCurrentText.setSize(36)
                    menuOption6BallPosXChangeCurrentText.setFace("times roman")
                    menuOption6BallPosXChangeCurrentText.draw(win)
                    
                    while True:
                        currentMouseOption6 = win.checkMouse()
                        #Check Add Button
                        if currentMouseOption6 != None and currentMouseOption6.getX() >= 64 and currentMouseOption6.getX() <= 74 and currentMouseOption6.getY() >= 46 and currentMouseOption6.getY() <= 56:
                            ballPosx += 1
                            if ballPosx > 75:
                                ballPosx = 75
                            menuOption6BallPosXChangeCurrentText.setText(str(ballPosx) + " m")
                        #Check Minus Button
                        elif currentMouseOption6 != None and currentMouseOption6.getX() >= 26 and currentMouseOption6.getX() <= 36 and currentMouseOption6.getY() >= 46 and currentMouseOption6.getY() <= 56:
                            ballPosx -= 1
                            if ballPosx < 0:
                                ballPosx = 0
                            menuOption6BallPosXChangeCurrentText.setText(str(ballPosx) + " m")
                        #Check Close Button
                        elif currentMouseOption6 != None and currentMouseOption6.getX() >= 26 and currentMouseOption6.getX() <= 31 and currentMouseOption6.getY() >= 69 and currentMouseOption6.getY() <= 74:
                            menuOption6BallPosXChange.undraw()
                            menuOption6BallPosXChangeAdd.undraw()
                            menuOption6BallPosXChangeAddText.undraw()
                            menuOption6BallPosXChangeMinus.undraw()
                            menuOption6BallPosXChangeMinusText.undraw()
                            menuOption6BallPosXChangeEscape.undraw()
                            menuOption6BallPosXChangeEscapeText.undraw()
                            menuOption6BallPosXChangeCurrentText.undraw()
                            break

                #Menu Option 7: Ball Pos Y Change
                if currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 26 and currentMouseMenu.getY() <= 35:

                    menuOption7BallPosYChange = Rectangle(Point(25,45),Point(75,75))
                    menuOption7BallPosYChange.setFill("white")
                    menuOption7BallPosYChange.draw(win)
                        
                    menuOption7BallPosYChangeAdd = Rectangle(Point(64,46),Point(74,56))
                    menuOption7BallPosYChangeAdd.draw(win)
                    menuOption7BallPosYChangeAddText = Text(Point(69,51),"+")
                    menuOption7BallPosYChangeAddText.setSize(36)
                    menuOption7BallPosYChangeAddText.setFace("times roman")
                    menuOption7BallPosYChangeAddText.draw(win)

                    menuOption7BallPosYChangeMinus = Rectangle(Point(26,46),Point(36,56))
                    menuOption7BallPosYChangeMinus.draw(win)
                    menuOption7BallPosYChangeMinusText = Text(Point(31,51),"-")
                    menuOption7BallPosYChangeMinusText.setSize(36)
                    menuOption7BallPosYChangeMinusText.setFace("times roman")
                    menuOption7BallPosYChangeMinusText.draw(win)

                    menuOption7BallPosYChangeEscape = Rectangle(Point(26,69),Point(31,74))
                    menuOption7BallPosYChangeEscape.draw(win)
                    menuOption7BallPosYChangeEscapeText = Text(Point(28.5,71.5),"X")
                    menuOption7BallPosYChangeEscapeText.setSize(28)                        
                    menuOption7BallPosYChangeEscapeText.setFace("times roman")
                    menuOption7BallPosYChangeEscapeText.draw(win)

                    menuOption7BallPosYChangeCurrentText = Text(Point(50,65),str(ballPosy) + " m")
                    menuOption7BallPosYChangeCurrentText.setSize(36)
                    menuOption7BallPosYChangeCurrentText.setFace("times roman")
                    menuOption7BallPosYChangeCurrentText.draw(win)
                    
                    while True:
                        currentMouseOption7 = win.checkMouse()
                        #Check Add Button
                        if currentMouseOption7 != None and currentMouseOption7.getX() >= 64 and currentMouseOption7.getX() <= 74 and currentMouseOption7.getY() >= 46 and currentMouseOption7.getY() <= 56:
                            ballPosy += 1
                            if ballPosy > 75:
                                ballPosy = 75
                            menuOption7BallPosYChangeCurrentText.setText(str(ballPosy) + " m")
                        #Check Minus Button
                        elif currentMouseOption7 != None and currentMouseOption7.getX() >= 26 and currentMouseOption7.getX() <= 36 and currentMouseOption7.getY() >= 46 and currentMouseOption7.getY() <= 56:
                            ballPosy -= 1
                            if ballPosy < 0:
                                ballPosy = 0
                            menuOption7BallPosYChangeCurrentText.setText(str(ballPosy) + " m")
                        #Check Close Button
                        elif currentMouseOption7 != None and currentMouseOption7.getX() >= 26 and currentMouseOption7.getX() <= 31 and currentMouseOption7.getY() >= 69 and currentMouseOption7.getY() <= 74:
                            menuOption7BallPosYChange.undraw()
                            menuOption7BallPosYChangeAdd.undraw()
                            menuOption7BallPosYChangeAddText.undraw()
                            menuOption7BallPosYChangeMinus.undraw()
                            menuOption7BallPosYChangeMinusText.undraw()
                            menuOption7BallPosYChangeEscape.undraw()
                            menuOption7BallPosYChangeEscapeText.undraw()
                            menuOption7BallPosYChangeCurrentText.undraw()
                            break

            





                #Escape Menu
                elif currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 16 and currentMouseMenu.getY() <= 25:
                    menuBoxLarge.undraw()
                    menuBoxLargeCloseMenu.undraw()
                    menuBoxLargeCloseMenuText.undraw()
                    
                    menuBoxLargeCloseSandbox.undraw()
                    menuBoxLargeCloseSandboxText.undraw()
                    
                    menuBoxLargeBallPosY.undraw()
                    menuBoxLargeBallPosYText.undraw()
                    
                    menuBoxLargeBallPosX.undraw()
                    menuBoxLargeBallPosXText.undraw()
                    
                    menuBoxLargeBallVY.undraw()
                    menuBoxLargeBallVYText.undraw()
                    
                    menuBoxLargeBallVX.undraw()
                    menuBoxLargeBallVXText.undraw()
                    
                    menuBoxLargeBallElasticity.undraw()
                    menuBoxLargeBallElasticityText.undraw()

                    menuBoxLargeBallMass.undraw()
                    menuBoxLargeBallMassText.undraw()

                    menuBoxLargeBallGravity.undraw()
                    menuBoxLargeBallGravityText.undraw()
                    
                    menuRun = False
                #Escape Sandbox Program 
                elif currentMouseMenu != None and currentMouseMenu.getX() >= 1 and currentMouseMenu.getX() <= 19 and currentMouseMenu.getY() >= 6 and currentMouseMenu.getY() <= 15:
                    #Main Escape Box
                    escapeConfirmationTextBoxMain = Rectangle(Point(25,45),Point(75,75))
                    escapeConfirmationTextBoxMain.setFill("white")
                    escapeConfirmationTextBoxMain.draw(win)

                    #Escape Box for Option "Yes"
                    escapeConfirmationTextBoxYes = Rectangle(Point(28,48),Point(47,54))
                    escapeConfirmationTextBoxYes.draw(win)
                    #Escape Box Word "Yes" for Escape Box Option "Yes"
                    escapeConfirmationTextYes = Text(Point(37.5,51),"Yes")
                    escapeConfirmationTextYes.setSize(24)
                    escapeConfirmationTextYes.setFace("times roman")
                    escapeConfirmationTextYes.draw(win)

                    #Escape Box for Option "No"
                    escapeConfirmationTextBoxNo = Rectangle(Point(53,48),Point(72,54))
                    escapeConfirmationTextBoxNo.draw(win)
                    #Escape Box Word "No" for Escape Box Option "No"
                    escapeConfirmationTextNo = Text(Point(62.5,51),"No")
                    escapeConfirmationTextNo.setSize(24)
                    escapeConfirmationTextNo.setFace("times roman")
                    escapeConfirmationTextNo.draw(win)

                    #Escape Box Confirmation Text
                    escapeConfirmationText = Text(Point(50,65),"Are you sure you want to exit?")
                    escapeConfirmationText.setSize(32)
                    escapeConfirmationText.setFace("times roman")
                    escapeConfirmationText.draw(win)
                            
                    #Checks Mouse Click Position. If within box "Yes", close program. If within box "No", close exit screen and return 
                    #to program. Else, do nothing.
                    while True:
                        clickPoint = win.getMouse()
                        if clickPoint.getX() >= 28 and clickPoint.getX() <= 47 and clickPoint.getY() >= 48 and clickPoint.getY() <=54:
                            win.close()
                        elif clickPoint.getX() >= 53 and clickPoint.getX() <= 72 and clickPoint.getY() >= 48 and clickPoint.getY() <=54:
                            escapeConfirmationTextBoxMain.undraw()
                            escapeConfirmationTextBoxYes.undraw()
                            escapeConfirmationTextYes.undraw()
                            escapeConfirmationTextBoxNo.undraw()
                            escapeConfirmationTextNo.undraw()
                            escapeConfirmationText.undraw()
                            break

            



    
    
    


    
    #Main Program Running
    if currentMouse != None and currentMouse.getX() > 95 and currentMouse.getX() < 99 and currentMouse.getY() > 1 and currentMouse.getY() < 5:
        offset = time.time()
        programRun = True
        ball = Circle(Point(ballPosx,ballPosy), 5)
        ball.setFill("blue")
        ball.draw(win)
        runButtonStop.draw(win)
        runButtonPlay.undraw()
        while programRun:
            currentMouseProgram = win.checkMouse()
            #Ball Movement

            
            s = time.time() - offset

            y_acc = (Force*sin(theta)-mass*g)/mass
            x_acc = (Force*cos(theta))/mass

            

            dballVx += x_acc*s
            dballVy += y_acc*s

            dballPosx = 0.5*x_acc*s**2+(dballVx+ballVx)*s
            dballPosy = 0.5*y_acc*s**2+(dballVy + ballVy)*s

            ball.move(dballPosx, dballPosy)

            ballPosx += dballPosx
            ballPosy += dballPosy

            if ballPosy < 5:
                ball.move(0,3)
                ballVy += dballVy
                ballVy *= -elasticity
                ballPosy += 3
                dballVy = 0
                offset = time.time()
            elif ballPosx < 5:
                ball.move(3,0)
                ballVx += dballVx
                ballVx *= -elasticity
                ballPosx += 3
                dballVx = 0
                offset = time.time()
            elif ballPosx > 95:
                ball.move(-3,0)
                ballVx += dballVx
                ballVx *= -elasticity
                ballPosx -= 3
                dballVx = 0
            elif ballPosy > 95:
                ball.move(0,-3)
                ballVy += dballVy
                ballVy *= -elasticity
                ballPosy -= 3
                dballVy = 0
                offset = time.time()
            if currentMouseProgram != None and currentMouseProgram.getX() > 95 and currentMouseProgram.getX() < 99 and currentMouseProgram.getY() > 1 and currentMouseProgram.getY() < 5:
                ball.undraw()
                ballVx = 0
                ballVy = 0 
                dballVx=0
                dballVy=0
                runButtonStop.undraw()
                runButtonPlay.draw(win)
                programRun = False
    
