#include <iostream>
#include <vector>
#include <algorithm>
int nProcesses = 3;

// Make a message transfer routine 
// p1 -> sendsMessage p2
// p1 -> newEvent()
// p2 -> newEvent()

// for(int i = [0:nProcesses))
//	p1.clock[i] = max(p1.clock[i], p2.clock[i]);

class Process {
	int id, nEvents;

public:
	std::vector<int> clock;

	Process(int id) {
		this->id = id;
		this->nEvents = 0;
		clock.resize(3);
	}  


	void newEvent()
	{
		clock[id]++;
		nEvents++;
		printClock();
	}

	void printClock()
	{

		std::cout << "Clock for Event E " << id << nEvents << std::endl;
		for(auto val : clock)
			std::cout << val << ", ";
	
		std::cout << std::endl;
	}

	static void sendMessage(Process &source, Process &dest)
	{
		source.newEvent();

		dest.newEvent();

		for(int i = 0; i < nProcesses; i++)
		{

			dest.clock[i] =std::max(dest.clock[i], source.clock[i]);
		}

		dest.printClock();
	}

};


int main()
{
	Process p1(0), p2(1), p3(2);
	
	p1.newEvent();
	p2.newEvent();
	
	Process::sendMessage(p3, p2);
	Process::sendMessage(p1, p2);
	
	p1.newEvent();
	p2.newEvent();
	p3.newEvent();
	Process::sendMessage(p1, p3);


	// print clock values
	// p1.printClock();
	// p2.printClock();
	// p3.printClock();
	

}
