for i in range(10):
    timmy.color(random.choice(colour_list))
    timmy.begin_fill()
    timmy.circle(10)
    timmy.end_fill()
    timmy.penup
    timmy.fd(50)
    timmy.pendown