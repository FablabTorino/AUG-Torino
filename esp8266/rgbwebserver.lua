---ledpin connected on pin 4 old gpio2
ledpin=4

r=0
g=0
b=0

SSID="FABLAB_TORINO"
PASSWD="FablabTorino"


--cfg={}
--cfg.ssid="ESP-"..node.chipid()
--cfg.pwd="password"
--print(cfg.ssid)
wifi.setmode(wifi.STATION)
--wifi.ap.config(cfg)
wifi.sta.config(SSID,PASSWD)

--usage:
--http://192.168.43.115/?r=100&g=20&b=30

--ws2812.writergb(ledpin, string.char(r,g,b))
--ws2812.writergb(ledpin, string.char(r2,g2,b2))

--led1 = 3
--led2 = 4
--gpio.mode(led1, gpio.OUTPUT)
--gpio.mode(led2, gpio.OUTPUT)
srv=net.createServer(net.TCP)
srv:listen(80,function(conn)
    conn:on("receive", function(client,request)
        local buf = "";
        local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");
        if(method == nil)then
            _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP");
        end
        local _GET = {}
        if (vars ~= nil)then
            for k, v in string.gmatch(vars, "(%w+)=(%w+)&*") do
                _GET[k] = v
            end
        end
        
        local _on,_off = "",""
        if(_GET.r ~= nil and _GET.r<256)then
            r=_GET.r;
        end
        if(_GET.g ~= nil and _GET.g<256)then
            g=_GET.g;
        end
        if(_GET.b ~= nil and _GET.b<256)then
            b=_GET.b;
        end
        ws2812.writergb(ledpin, string.char(r,g,b))

        buf = buf.."<p> RGB value ";
        buf = buf..r;
        buf = buf..":";
        buf = buf..g;
        buf = buf..":";
        buf = buf..b;
        buf = buf.."</p>";
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)

print(wifi.sta.getip())