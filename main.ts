radio.onReceivedString(function (receivedString) {
    basic.showIcon(IconNames.No)
    soundExpression.sad.play()
    basic.pause(2000)
})
basic.showString("Hola Jorge")
basic.forever(function () {
    if (input.acceleration(Dimension.X) > 550) {
        basic.showIcon(IconNames.No)
        soundExpression.giggle.play()
        radio.sendString("")
        basic.pause(2000)
    } else if (input.acceleration(Dimension.Y) > 550) {
        basic.showIcon(IconNames.No)
        soundExpression.giggle.play()
        radio.sendString("")
        basic.pause(2000)
    } else {
        basic.clearScreen()
        basic.pause(2000)
    }
})
