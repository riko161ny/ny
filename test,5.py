from turtle import*
shape("turtle")
color("green")
bgcolor("black")
speed(6)



def drawline(date):
    for i in range(len(date)):
        if i  ==0:
            penup()
        goto(date[i][0],date[i][1])
        pendown()
drawline([[-75,165],[75,165]])
drawline([[75,165],[50,75]])

drawline([[-75,35],[75,35]])
drawline([[75,35],[50,-75]])
drawline([[0,50],[-30,-75]])

drawline([[50,-115],[-75,-150]])
drawline([[0,-130],[0,-225]])



ht()
done()
