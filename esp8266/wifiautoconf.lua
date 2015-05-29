--wifi autoconfig

SSID="FABLAB_TORINO"
PASSWD="FablabTorino"

--wifi.sta.config("FABLAB_TORINO","FablabTorino")
cfg={}
cfg.ssid="ESP-"..node.chipid()
cfg.pwd="password"

function connect(ssid, password)
    wifi.setmode(wifi.STATIONAP)
    --wifi.ap.config(cfg)
    wifi.sta.disconnect()
    wifi.sta.config(SSID,PASSWD)
    
    tmr.delay(1000000)
    tprint(wifi.sta.getip())
end

function startserver()
ssid=""
password=""
print("start server")
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
        if(_GET.ssid ~= nil and _GET.password ~= nil)then
            SSID=_GET.ssid;
            PASSWD=_GET.password;
            print("ssid: "..SSID.." password: "..PASSWD)
            connect(SSID, PASSWD)
        end
      
        buf = buf.."<p> Set wifi ssid and password </p> ";
        
        buf = buf.."<form action='#' method='GET'>";
        buf = buf.."SSID: <input name='ssid' type='text' />";
        buf = buf.."PASSWORD: <input name='password' type='text' />";
        buf = buf.."<input type='submit' />";
        buf = buf.."</form>";
        
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)
end

--the execution starts here

connect(SSID, PASSWD)

--if can't connect to access point I'll start my own and use a webserver to autoconfigure the web
if (wifi.sta.getip() == nil) then 
    print("not connected, starting my own: "..cfg.ssid)
    
    wifi.setmode(wifi.STATIONAP)
    wifi.ap.config(cfg)
    print(wifi.ap.getip())
    startserver()
end

print(wifi.sta.getip())
--nil

