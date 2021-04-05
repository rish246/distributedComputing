import socket

class Process:
    def __init__(self, id):
        self.id = id
        self.waits_for = []


    def started_waiting_for(self, process):
        self.waits_for.append(process)


class ExternalProcess:
    def __init__(self, id, UDP_IP, UDP_Port):
        self.id = id
        self.UDP_IP = UDP_IP
        self.UDP_Port = UDP_Port




def recieve_probe(parent_id : int, imm_parent : Process, cur_process) -> bool:

    print(f'Probe recieved by process P{cur_process.id}')

    if(isinstance(cur_process, ExternalProcess)):
        print(f'Process P{cur_process.id} is an external process')
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        probe_msg = str(parent_id) + '-' + str(imm_parent.id) + '-' + str(cur_process.id)
        print(probe_msg)
        client_socket.sendto(probe_msg.encode(), (cur_process.UDP_IP, cur_process.UDP_Port))
        return False

    if(cur_process.id == parent_id):
        print(f'Deadlock found at process P{cur_process.id} from process P{imm_parent.id}')
        return True


    

    return send_probe(parent_id, cur_process)

    

def send_probe(parent_id : int, cur_process) -> bool:
    # found_deadlock = False
    # check for externalProcess

    for neighbour in cur_process.waits_for:
        found_deadlock = recieve_probe(parent_id, cur_process, neighbour)
        if found_deadlock:
            return True
    
    return False

    


def main():
    p1 = Process(1)
    p2 = Process(2)
    p3 = Process(3)
    p4 = Process(4)
    p5 = Process(5)
    p6 = Process(6)
    p7 = Process(7)
    p8 = Process(8)
    p9 = Process(9)
    p10 = Process(10)

    # create the wait for graph
    p1.started_waiting_for(p2)
    p2.started_waiting_for(p3)
    p3.started_waiting_for(p4)
    p4.started_waiting_for(p5)
    p4.started_waiting_for(p6)
    p5.started_waiting_for(p7)
    p6.started_waiting_for(p8)
    p7.started_waiting_for(p10)
    p8.started_waiting_for(p9)
    p9.started_waiting_for(p1)

    # start probe from p1
    found_deadlock = send_probe(1, p1)
    if found_deadlock:
        print(f'System is in a deadlock condition')
    else:
        print(f'System is deadlock free')



if __name__ == "__main__":
    main()