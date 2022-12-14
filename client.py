import socket, threading
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.0.196', 7976))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(msg)
        except:
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        msg = '{}: {}'.format(nickname, input(''))
        client.send(msg.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
