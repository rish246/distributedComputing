import  socket
from EdgeChasing import Process, ExternalProcess, send_probe, recieve_probe

siteB_Port = 4050
siteB_IP = "127.0.0.1"

siteC_Port = 4060
siteC_IP = "127.0.0.1"

# treat siteA as client and then as server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((siteB_IP, siteB_Port))


def main():
    p4 = Process(4)
    p5 = Process(5)
    p6 = Process(6)
    p7 = Process(7)

    p8 = ExternalProcess(8, siteC_IP, siteC_Port)
    p9 = ExternalProcess(9, siteC_IP, siteC_Port)

    p4.started_waiting_for(p5)
    p4.started_waiting_for(p6)
    p5.started_waiting_for(p7)
    p6.started_waiting_for(p8)
    p7.started_waiting_for(p9)
    # while True: 


    processes = {
        4 : p4,
        5 : p5,
        6 : p6,
        7 : p7
    }


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
    
    # extract the process ID and hence corresponding process
    #Extract data,

    # clientSocket.sendto(data, (siteC_IP, siteC_Port))
if __name__ == "__main__":
    main()