from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.bind((mailserver,port))
    clientSocket.listen(1)
    # Fill in end

    recv = clientSocket.recv(1025).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1025).decode()

    # Send MAIL FROM command and print server response.
    # Fill in start
    MailFromCommand = 'MAIL FROM\r\n'
    clientSocket.send(MailFromCommand.encode())
    recv2 = clientSocket.recv(1025).decode()
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    RcptToCommand = 'RCPT TO\r\n'
    clientSocket.send(RcptToCommand.encode())
    recv3 = clientSocket.recv(1025).decode()
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1025).decode()
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    QuitCommand = 'QUIT\r\n'
    clientSocket.send(QuitCommand.encode())
    recv5 = clientSocket.recv(1025).decode()
    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
