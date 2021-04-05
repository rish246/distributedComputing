import  socket

from EdgeChasing import Process, ExternalProcess, send_probe, recieve_probe

siteA_Port = 4040
siteA_IP = "127.0.0.1"

siteB_Port = 4050
siteB_IP = "127.0.0.1"

# treat siteA as client and then as server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((siteA_IP, siteA_Port))

# data = "hi"
# clientSocket.sendto(data.encode(), (siteB_IP, siteB_Port))

# while True:
#     data, addr = serverSocket.recvfrom(1024)
#     print(data, addr)
#     clientSocket.sendto(data, (siteB_IP, siteB_Port))

def main():
    p1 = Process(1)
    p2 = Process(2)
    p3 = Process(3)
    p4 = ExternalProcess(4, siteB_IP, siteB_Port)
    p1.started_waiting_for(p2)
    p2.started_waiting_for(p3)
    p3.started_waiting_for(p4)

    found_deadlock_in_site = send_probe(1, p1)
    if found_deadlock_in_site:
        print(f'Deadlock found in site A')
    else:
        print(f'Site A is deadlock free')


    processes = {
        1 : p1,
        2 : p2,
        3 : p3   
    }


    # start listening to external communication
    while True:
        data, addr = serverSocket.recvfrom(1024)
        data = [int(d) for d in data.decode().split('-')]


        parent_id, imm_parent_id, site_proc_id = data[0], data[1], data[2]


        if parent_id == site_proc_id:
            print(f'Deadlock detected at process P{site_proc_id} coming from P{imm_parent_id}')
            exit(1)


        found_deadlock_in_site = send_probe(parent_id, processes[site_proc_id])

        if found_deadlock_in_site:
            print(f'Deadlock found in site B')
        else:
            print(f'Site B is deadlock free')


if __name__ == "__main__":
    main()