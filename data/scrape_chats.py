import requests
import socket
import logging
from emoji import demojize


server = 'irc.chat.twitch.tv'
port = 6667
nickname = '_______'
token = 'oauth:1245'
channel = '#hasanabi'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('%s_chat.log' % channel[1:], encoding='utf-8')])


def main():
    sock = socket.socket()
    sock.connect((server,port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    try:
        while True:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
            elif len(resp) > 0:
                logging.info(demojize(resp))
    except KeyboardInterrupt:
        sock.close()
        exit()


if __name__ == '__main__':
    main()