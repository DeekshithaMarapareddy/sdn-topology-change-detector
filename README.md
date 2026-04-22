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
3. Start Mininet Topology
sudo mn --topo linear,3 --controller=remote,ip=127.0.0.1,port=6633
4. Display Topology
nodes
net
links
🧪 Test Scenarios
✅ Scenario 1: Normal Connectivity
pingall

✔ Expected:

0% dropped
🚫 Scenario 2: Blocked Traffic (Policy Enforcement)
h1 ping h3

✔ Expected:

100% packet loss

✔ Explanation:
Traffic from host h1 (10.0.0.1) to h3 (10.0.0.3) is blocked using OpenFlow drop rule.

 Scenario 3: Link Failure
link s1 s2 down
pingall

Expected:
Packet loss observed
Scenario 4: Recovery
link s1 s2 up
pingall

Expected:
0% dropped
Flow Table Verification
sh ovs-ofctl dump-flows s1

Shows installed OpenFlow rules (match → action)

 Expected Output Summary
Scenario	Expected Result
Normal network	0% packet loss
h1 → h3	Blocked (100% loss)
Link down	Packet loss
Link up	Recovery
 Conclusion

This project demonstrates how SDN enables centralized control over network behavior. The controller dynamically installs flow rules, blocks specific traffic, and adapts to topology changes efficiently.


---
