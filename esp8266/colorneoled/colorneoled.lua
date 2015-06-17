gpio.mode(3, gpio.OUTPUT)
gpio.write(3, gpio.LOW)
ws2812.writergb(3, string.char(0, 0, 0):rep(30))

function colorneoled(gpio, nleds, color1, color2, color3)

a=string.char(color1)..string.char(color2)..string.char(color3)
ws2812.writergb(gpio, a:rep(nleds))

end

