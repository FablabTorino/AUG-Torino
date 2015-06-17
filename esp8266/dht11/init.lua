wifi.setmode(wifi.STATION)
--wifi.sta.config("FABLAB_TORINO","FablabTorino")
wifi.sta.config("FASTWEB-1-ddufVHRPqndR","0123456789")
--dofile("colorchngled.lua")
--dofile("led rgb.lua")
print("1")
   tmr.alarm(3,20000,1, function() 
   a=(dofile("dht22.lua").read(4))
   print(a)
   end)
print("2")
dofile("pushetta.lua")
print("3")

function connected(conn)
   print("Wifi console connected.")
   function s_output(str)
      if (conn~=nil)    then
         conn:send(str)
      end
   end
   node.output(s_output,0)
   conn:on("receive", function(conn, pl) 
      node.input(pl) 
   end)
   conn:on("disconnection",function(conn) 
      node.output(nil) 
   end)
   print("Welcome to NodeMcu world.")
end
function startServer()
  
   sv=net.createServer(net.TCP, 180)
   sv:listen(2323, connected)
   print("Telnet Server running at :2323")
   print("===Now, logon and input LUA.====")
end
tmr.alarm(1, 1000, 1, function() 
   if wifi.sta.getip()==nil then
      print("Connect AP, Waiting...") 
   else
      print("Wifi AP connected. Wicon IP:")
      print(wifi.sta.getip())
     -- startServer()
      dofile("Pushetta MQTT.lua")
      tmr.stop(1)
   end
end)



