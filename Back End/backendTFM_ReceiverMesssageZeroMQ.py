import time
import threading
import zmq

def worker_routine(worker_url, context=None):
    """Worker routine"""
    context = context or zmq.Context.instance()
    # Socket to talk to dispatcher
    socket = context.socket(zmq.REP)

    socket.connect(worker_url)

    cont = 0
    while True:
        print("------------ <|Mensagem " + str(cont) + "|> ---------------")
        string  = socket.recv()

        print("Solicitação Recebida %s: [ %s ]" % (cont, string))

        # do some 'work'
        time.sleep(1)

        #send reply back to client
        mess = input("\tDigite a Mensagem " + str(cont) + ": ")
        while mess == '':
            mess = input("\tDigite a Mensagem " + str(cont) + ": ")
        mess = str.encode(mess)
        socket.send(mess)
        print("-----------------------------\n")
        cont = cont + 1

def main():
    """Server routine"""

    url_worker = "inproc://*:9999"
    url_client = "tcp://*:5555"
    #print(url_worker,url_client)
    # Prepare our context and sockets
    context = zmq.Context.instance()

    # Socket to talk to clients
    clients = context.socket(zmq.ROUTER)
    clients.bind(url_client)

    # Socket to talk to workers
    workers = context.socket(zmq.DEALER)
    workers.bind(url_worker)

    # Launch pool of worker threads
    #for i in range(5):
    thread = threading.Thread(target=worker_routine, args=(url_worker,))
    thread.start()

    zmq.proxy(clients, workers)

    # We never get here but clean up anyhow
    clients.close()
    workers.close()
    context.term()

if __name__ == "__main__":
    main()