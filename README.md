# SDN Topology Change Detector using POX & Mininet

## Problem Statement
The objective of this project is to implement a Software Defined Networking (SDN) solution using Mininet and a POX controller. The system demonstrates controller–switch interaction, OpenFlow match–action rule design, handling of packet_in events, and dynamic network behavior under different scenarios such as allowed vs blocked traffic and link failure vs recovery.

---

## Technologies Used
- Mininet (Network Emulator)
- POX Controller (OpenFlow Controller)
- OpenFlow Protocol

---

## Project Description
This project implements a learning switch using the POX controller with additional functionalities:
- MAC address learning
- Flow rule installation
- Traffic control using OpenFlow rules
- Blocking specific traffic (h1 → h3)
- Handling topology changes (link failure and recovery)

---

## Setup & Execution Steps

### Step 1: Clean Environment

sudo pkill -f pox  
sudo mn -c  

---

### Step 2: Start POX Controller

cd ~/pox  
./pox.py log.level --DEBUG misc.tcd_pox  

---

### Step 3: Start Mininet Topology

sudo mn --topo linear,3 --controller=remote,ip=127.0.0.1,port=6633  

---

### Step 4: Display Topology

nodes  
net  
links  

---

## Test Scenarios

### Scenario 1: Normal Connectivity

pingall  

Expected Output:
- 0% packet loss
- All hosts communicate successfully

---

### Scenario 2: Allowed vs Blocked Traffic

h1 ping h2  
h1 ping h3  

Expected Output:
- h1 → h2 works normally
- h1 → h3 fails (blocked by controller)

---

### Scenario 3: Link Failure

link s1 s2 down  
pingall  

Expected Output:
- Packet loss observed
- Network disruption

---

### Scenario 4: Link Recovery

link s1 s2 up  
pingall  

Expected Output:
- Network restored
- 0% packet loss

---

### Flow Table Verification

sh ovs-ofctl dump-flows s1  

Expected Output:
- Flow rules installed by controller are displayed

---

## Expected Output Summary
- Normal network: 0% packet loss  
- Allowed traffic: successful communication  
- Blocked traffic: 100% packet loss  
- Link failure: packet loss observed  
- Link recovery: network restored  
- Flow tables: OpenFlow rules visible  
