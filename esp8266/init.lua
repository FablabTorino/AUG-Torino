
--dofile("wifi.lua")
--dofile("helloWorld.lua")
print("hello world")

SSID="FABLAB_TORINO"
PASSWD="FablabTorino"


--cfg={}
--cfg.ssid="ESP-"..node.chipid()
--cfg.pwd="password"
--print(cfg.ssid)
wifi.setmode(wifi.STATION)
--wifi.ap.config(cfg)
wifi.sta.config(SSID,PASSWD)

wifi.sta.getip()

sv=net.createServer(net.TCP, 30)   


sv:listen(80,function(c)
  c:on("receive", function(c, pl) 
     print(pl) 
  end)
  c:send("hello there")
end)
