package com.Rishabh;

import java.util.ArrayList;
import java.util.List;

public class Process {
    static public int nProcesses = 3;

    private int id;
    private int nEvents;


    public int[] clock = null;

    public Process(int id)
    {
        this.id = id;
        nEvents = 0;
        clock = new int[nProcesses];
    }

    public void newEvent()
    {
        clock[this.id]++;
        this.nEvents++;

    }


    public void printClock()
    {
        for(int val : clock)
            System.out.printf("%d, ", val);

        System.out.println("\n");

    }

    // Send a message from one process to another
    static public void sendMessage(Process p1, Process p2)
    {
        p1.newEvent();
        p2.newEvent();

        for(int i = 0; i < nProcesses; i++) {
            p2.clock[i] = Math.max(p1.clock[i], p2.clock[i]);
        }
    }

}
