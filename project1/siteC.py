import  socket
from EdgeChasing import  Process, ExternalProcess, send_probe

siteA_Port = 4040
siteA_IP = "127.0.0.1"

siteC_Port = 4060
siteC_IP = "127.0.0.1"

# treat siteA as client and then as server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((siteC_IP, siteC_Port))


# clientSocket.sendto(data, (siteA_IP, siteA_Port))
def main():
    p8 = Process(8)
    p9 = Process(9)
    p10 = Process(10)
    p1 = ExternalProcess(1, siteA_IP, siteA_Port)


    p8.started_waiting_for(p10)
    p10.started_waiting_for(p1)
    # p5.started_waiting_for(p7)
    # p6.started_waiting_for(p8)
    # p7.started_waiting_for(p9)
    # while True: 


    processes = {
        8 : p8,
        9 : p9,
        10 : p10    
    }

    while True:

        data, addr = serverSocket.recvfrom(1024)

        data = [int(d) for d in data.decode().split('-')]

        parent_id, imm_parent_id, site_proc_id = data[0], data[1], data[2]

        if parent_id == site_proc_id:
            print(f'Deadlock detected at process P{site_proc_id} coming from P{imm_parent_id}')
            exit(1)

        print(site_proc_id)

        found_deadlock_in_site = send_probe(parent_id, processes[site_proc_id])

        if found_deadlock_in_site:
            print(f'Deadlock found in site B')
        else:
            print(f'Site B is deadlock free')





if __name__ == "__main__":
    main()