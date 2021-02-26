import socket

MSG_LENGTH = 64
DISCONNECTED = '!CONNECTION CLOSED'

# serverIp = '120.53.107.28'
remote_ip = socket.gethostbyname(socket.gethostname())
remote_port = 5050
remote_addr = (remote_ip, remote_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(remote_addr)
print(f'客户机工作地址：{client_socket.getsockname()}')


def send_recv(msg):
    """
    功能：客户机向服务器发送消息并接收服务器的回送消息
    :param msg: 消息内容
    """
    message = msg.encode('utf-8')  # 消息编码
    msg_len = len(message)  # 消息长度
    str_len = str(msg_len).encode('utf-8')  # 长度编码
    str_len += b' ' * (MSG_LENGTH - len(str_len))  # 空白处补空格
    client_socket.send(str_len)  # 发送消息长度
    client_socket.send(message)  # 发送消息内容
    echo_message = client_socket.recv(1024).decode('utf-8')  # 接收服务器消息
    print(echo_message)


while True:
    inputStr = input('请输入待发送的字符串(Q:结束会话）：')
    if inputStr.lower() == 'q':
        break
    send_recv(inputStr)  # 发送消息

send_recv(DISCONNECTED)  # 通知服务器会话线程，本客户机会话结束
client_socket.close()
