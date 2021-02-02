package com.Rishabh;

import com.Rishabh.Process;
// Import package.Filename
public class Main {

    public static void main(String[] args) {
	// write your code here
        Process.nProcesses = 3;

        // Calling static methods in c++
        // Class::method()
        // Calling static method in java
        // ClassName.method()
        Process p1 = new Process(0);
        Process p2 = new Process(1);
        Process p3 = new Process(2);

        p1.newEvent();
        p2.newEvent();

        Process.sendMessage(p3, p2);
        Process.sendMessage(p1, p2);

        p1.newEvent();
        p2.newEvent();
        p3.newEvent();
        Process.sendMessage(p1, p3);


        // Print values of clocks
        p1.printClock();
        p2.printClock();
        p3.printClock();



    }
    // Nice It is done
}
