'''
A simple general simulation of Lamport's mutual exclusion algorithm
-- Note : This is not a general solution ... it is only applicable to this tc
'''
class RequestMessage:
    def __init__(self, timestamp, process_id):
        self.timestamp = timestamp
        self.process_id = process_id

    def __str__(self) -> str:
        print(f'<{self.timestamp}, {self.process_id}>')



class Site:
    def __init__(self, id, timestamp):
        self.id = id
        self.timestamp = timestamp
        self.n_replies = 0
        self.request_queue = []
        self.is_requesting_cs = False
    
    def send_req_message(self, req_set):
        # prepare a req message
        req_message = RequestMessage(self.timestamp, self.id)

        for site in req_set:
            # Send req message to all the sites in req set
            site.request_queue.append(req_message)

            print(f'Request sent to site S{site.id}')

            self.n_replies += 1

    def enter_cs(self):

        print(f'Site S{self.id} is entering the critical section')

    
    def send_release_message(self, req_set):
        print(f'Site S{self.id} is releasing critical section')
        for site in req_set:
            print(f'Release message sent to Site S{site.id}')
            site.request_queue.pop()

    
    def print_req_queue(self):
        if len(self.request_queue) == 0:
            return
        
        print(f'--------Site S{self.id} Queue----------')

        for req_msg in self.request_queue:
            print(f'<{req_msg.timestamp}, {req_msg.process_id}>')

        print('\n')



def main():
    site_one = Site(1, 2)
    site_two = Site(2, 1)
    site_three = Site(3, 2)
    request_set = {site_one, site_two, site_three}

    site_two.send_req_message(request_set)
    site_one.send_req_message(request_set)
    # print(site_one.request_queue)
    
    #Time to enter CS
    for site in request_set:
        if (site.n_replies == len(request_set)) and (site.request_queue[0].process_id == site.id):
            site.enter_cs()

            site.send_release_message(req_set = request_set)

            site_one.print_req_queue()
            site_two.print_req_queue()

            # send release message to other sites



if __name__ == "__main__":
    main() 

# A Kind of basic simulation of Lamport's algo
# Implement the next algorithm fully -> using sockets and all the stuff
# Learn UDP
# Learn Socket programming in Python
# Implement the algo