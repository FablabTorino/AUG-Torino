function pushetta(destin, text)
--len=tostring(43+string.len(text))
len1="80"
sk=net.createConnection(net.TCP, 0)
sk:on("receive", function(sck, c) print(c) end )
sk:connect(80,"149.210.164.152")
sk:send("POST /api/pushes/".. destin.."/ HTTP/1.1\r\nUser-Agent: test/1.0.0\r\nHost: api.pushetta.com\r\nAccept: */*\r\nAuthorization: Token 459bd6735bb43a0877219deca123a0d48c30e9d0\r\nContent-Type: application/json\r\nContent-Length: 73\r\n\r\n")
sk:send("{\"body\": \""..text.."\", \"message_type\": \"plain/text\"}\r\n\r\n") 
end



-- pushetta("espmqtt_ret", dofile("dht22.lua").read(1))


-- pushetta("espmqtt_ret", "coco")
