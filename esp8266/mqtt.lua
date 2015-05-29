BROKER = "m20.cloudmqtt.com"
BRPORT = 18232
BRUSER = "jpihezei"
BRPWD  = "lRf-uYQr9ELu"
CLIENTID = "ESP8266-" ..  node.chipid()

--dofile("baro.lc")

print "Connecting to MQTT broker. Please wait..."
m = mqtt.Client( CLIENTID, 120, BRUSER, BRPWD)
-- on publish message receive event
    m:on("message", function(conn, topic, data) 
      print(topic .. ":" ) 
      if data ~= nil then
        print(data)
      end
    end)

m:connect( BROKER , BRPORT, 0, function(conn)
     print("Connected to MQTT:" .. BROKER .. ":" .. BRPORT .." as " .. CLIENTID )
     --m:publish("sensors/".. CLIENTID .. "/temperature",read_temp(i2c_addr),0,0, function(conn)
     --print ("temp published") 

     -- subscribe topic with qos = 0
    --m:subscribe("sensors/".. CLIENTID .. "/test",0, function(conn) 
        --print("subscribe success") 
    --end)
    
    tmr.delay(10000)
     --m:publish("sensors/".. CLIENTID .. "/test",42,0,0, function(conn)
     m:publish("test",42,0,0, function(conn)
     print ("test published")
     tmr.delay(10000)
     --m:publish("sensors/".. CLIENTID .. "/pressure",read_pressure(i2c_addr),0,0, function(conn)
     --print ("pressure published") 
     --node.dsleep(60*1000000)
     --end)
  end)
end)


