

BROKER = "iot.pushetta.com"

BRPORT = 1883
BRUSER = "459bd6735bb43a0877219deca123a0d48c30e9d0"
BRPWD = "pushetta"
CLIENTID = "ESP8266-" .. node.chipid()


m = mqtt.Client( CLIENTID, 120, BRUSER, BRPWD)

m:on("message", function(conn, topic, data) 
 
  if data ~= nil then
 -- print(data)


i=1
a={}
for token in string.gmatch(data, "[^%s]+") do
   a[i]=token
   print(a[i])
   i=i+1
end

 if a[1]=="colorlamp" then
 --colorchngled 100,200,100  (<255)
  colorchngled(3, 30,a[2],a[3],a[4])
 
 elseif a[1]=="colorneoled" then
 --colorneoled 100,200,100  (<255)
  colorneoled(3, 30,a[2],a[3],a[4])
 
 
 elseif a[1]=="gettemp" then
  -- tmr.wdclr()
 -- local a=(dofile("dht22.lua").read(1))
  
  print(a)
   pushetta("espmqtt_ret", a)
  
 
 elseif a[1]=="led" then
   led(a[2],a[3],a[4])
  

 else pushetta("espmqtt_ret", a[1])
  end

end
end)


m:connect( BROKER , BRPORT, 0, function(conn)

    -- subscribe topic with qos = 0
    m:subscribe("/pushetta.com/channels/espmqtt",0, function(conn) print("subscribe success") end)
end)
