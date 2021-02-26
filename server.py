import socket
import threading
import time

MSG_LENGTH = 64
DISCONNECTED = '!CONNECTION CLOSED'
connections = 0

# server_ip = '0.0.0.0'
server_ip = socket.gethostbyname(socket.gethostname())
server_port = 5050
server_addr = (server_ip, server_port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_addr)

server_socket.listen()
print(f'服务器开始在{server_addr}侦听...')


def handle_client(client_socket, client_addr):
    """
    功能：处理与客户机的会话
    :param client_socket: 会话套接字
    :param client_addr: 客户机地址
    """
    print(f'新连接建立，远程客户机地址是：{client_addr}')
    connected = True
    while connected:
        msg_len = client_socket.recv(MSG_LENGTH).decode('utf-8')  # 接收消息长度
        if msg_len:
            msg_len = int(msg_len)
            msg = client_socket.recv(msg_len).decode('utf-8')  # 接收消息内容
            if msg == DISCONNECTED:  # 收到客户机断开连接的消息
                connected = False
                print(f'客户机：{client_addr}断开了连接！')
                global connections
                connections -= 1
                print(f'服务器当前活动连接数量是：{connections}')

            print(f'来自客户机{client_addr}的消息是：{msg}')
            # 回送消息
            echo_message = f'服务器{client_socket.getsockname()}收到消息：{msg}, ' \
                           f'时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} '
            client_socket.send_recv(echo_message.encode('utf-8'))
    client_socket.close()  # 关闭会话连接


while True:
    new_socket, new_addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(new_socket, new_addr))
    client_thread.start()
    connections += 1
    print(f'服务器端当前活动连接数量是：{connections}')
