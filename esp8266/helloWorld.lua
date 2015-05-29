--ledpin connected on pin 3 -> gpio0
--button connected on pin 4 -> gpio2

pin=3
button=4


--turn on a led and turn it back off
function blink()
    gpio.mode(pin,gpio.OUTPUT)
    print("turn pin on")
    gpio.write(pin,gpio.HIGH)
    tmr.delay(1000000)
    print("turn pin off")
    gpio.write(pin,gpio.LOW)
    tmr.delay(1000000)
end

--button collegato a gnd con il pullup 
--normalmente il pin è HIGH
--quando premo il pulsante va a LOW e il trigger scatta 
gpio.mode(button,gpio.INT,gpio.PULLUP)

gpio.trig(button,"down",
function()
    print("pressed")
    blink()
    print("fine")
end
)

-[[
pinmode=gpio.LOW
--toggle pin based on previous state
function togglepin(input, pin)
    gpio.mode(pin,gpio.OUTPUT)
    gpio.mode(input,gpio.INPUT,gpio.PULLUP)
    print("read pin: "..input.." value: "..gpio.read(input))
    if (gpio.read(input) == 0 and pinmode == gpio.LOW)then
        print("turn pin on");
        gpio.write(pin,gpio.HIGH);
        pinmode=gpio.HIGH;
    elseif(gpio.read(input) == 0 and pinmode == gpio.HIGH)then
        print("turn pin off");
        gpio.write(pin,gpio.LOW);
        pinmode=gpio.LOW;
    end
end

--tmr.alarm(0, 1000, 1, function() 
--    togglepin(button, pin) 
--end )
]]-
    
