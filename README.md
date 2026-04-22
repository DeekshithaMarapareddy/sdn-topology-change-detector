# SDN Topology Change Detector using POX & Mininet

## 📌 Problem Statement
The goal of this project is to implement a Software Defined Networking (SDN) solution using Mininet and a POX controller to demonstrate:

- Controller–switch interaction
- OpenFlow match–action rule design
- Packet handling using `packet_in` events
- Network behavior under different scenarios

---

## ⚙️ Technologies Used
- Mininet (Network Emulator)
- POX Controller (OpenFlow Controller)
- OpenFlow Protocol

---

## 🧠 Project Description

This project implements a learning switch using POX and extends it with:

- MAC address learning
- Flow rule installation
- Traffic control using OpenFlow rules
- Blocking specific traffic (h1 → h3)
- Handling topology changes (link failure & recovery)

---

## 🚀 Setup & Execution Steps

### 1. Clean Environment
```bash
sudo pkill -f pox
sudo mn -c
2. Start POX Controller
cd ~/pox
./pox.py log.level --DEBUG misc.tcd_pox
3.Start Mininet Topology
sudo mn --topo linear,3 --controller=remote,ip=127.0.0.1,port=6633
4. Display Topology
nodes
net
links
Test Scenarios
Scenario 1: Normal Connectivity
pingall

Expected Output:

0% packet loss
All hosts can communicate
Scenario 2: Allowed vs Blocked Traffic
h1 ping h2
h1 ping h3

Expected Output:

h1 → h2: Successful communication
h1 → h3: 100% packet loss (blocked by controller)
Scenario 3: Link Failure
link s1 s2 down
pingall

Expected Output:

Packet loss observed
Network disruption
Scenario 4: Link Recovery
link s1 s2 up
pingall

Expected Output:

Network restored
0% packet loss
Flow Table Verification
sh ovs-ofctl dump-flows s1

Expected Output:

Flow entries showing match–action rules installed by controller
Expected Output Summary
Normal network: 0% packet loss
Allowed traffic: Successful communication
Blocked traffic: 100% packet loss
Link failure: Packet loss observed
Link recovery: Network restored
Flow tables: Display OpenFlow rules installed by controller

'''
