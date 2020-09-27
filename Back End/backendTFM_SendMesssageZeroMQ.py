import zmq

context = zmq.Context()

#  Socket to talk to server
print("CONECTANDO COM O SERVIDOR")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
#for request in range(10):
    #print("Sending request %s …" % request)
    #socket.send(b"Hello")

    #  Get the reply.
    #message = socket.recv()
    #print("Received reply %s [ %s ]" % (request, message))

def SendMessage(mensagem, cont):
    print("\t\tEnviando Requisição")

    print("\t\tEviando Mensagem %s [ %s ]" % (cont, mensagem))
    socket.send(mensagem)

    #  Get the reply.
    message = socket.recv()
    print("\t\tResposta Recebida %s [ %s ]" % (cont, message))

cont = 0
while True:
    print("------------ <|Mensagem " + str(cont) + "|> ---------------")
    mess = input("\tDigite a Mensagem " + str(cont) + ": ")
    #print(mess)
    while mess == '':
        mess = input("\tDigite a Mensagem " + str(cont) + ": ")
    mess = str.encode(mess)
    #print(mess)
    SendMessage(mess, cont)
    print("-----------------------------\n")
    cont = cont+1