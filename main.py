def on_received_string(receivedString):
    basic.show_icon(IconNames.NO)
    soundExpression.sad.play()
    basic.pause(2000)
radio.on_received_string(on_received_string)

basic.show_string("Hola Jorge")

def on_forever():
    if input.acceleration(Dimension.X) > 550:
        basic.show_icon(IconNames.NO)
        soundExpression.giggle.play()
        radio.send_string("")
        basic.pause(2000)
    elif input.acceleration(Dimension.Y) > 550:
        basic.show_icon(IconNames.NO)
        soundExpression.giggle.play()
        radio.send_string("")
        basic.pause(2000)
    else:
        basic.clear_screen()
        basic.pause(2000)
basic.forever(on_forever)
