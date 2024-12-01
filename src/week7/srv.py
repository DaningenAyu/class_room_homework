import socket
from datetime import datetime

#ネットワーク設定
HOST = "192.168.56.101"
PORT = 60080

#ソケット設定
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(1)

#鯖起動メッセージ
print("start web server. {}:{}".format(HOST,PORT))

while True:
    try:
        cli_con,cli_addr = sock.accept()
        req = cli_con.recv(1024).decode("utf-8")
        now = datetime.now()
        print("[request{}][{}]:{}\n".format(cli_addr,now,req))
        http_res = "HTTP/1.1 200 OK\n\n"
        with open(file="index.html",mode="r",encoding="utf-8") as f:
            http_res += f.read()
            cli_con.sendall(http_res.encode("utf-8"))
        print("push html data\n------------------------------------")
        cli_con.close()
    except KeyboardInterrupt:
        print("fin web server")
        cli_con.close()
        break
