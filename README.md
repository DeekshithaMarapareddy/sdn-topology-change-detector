# SDN Topology Change Detector using POX & Mininet

## 📌 Problem Statement
The objective of this project is to implement a Software Defined Networking (SDN) solution using Mininet and a POX controller. The system demonstrates controller–switch interaction, handling of packet_in events, and OpenFlow match–action rule design. It also shows how the controller can dynamically manage network behavior by allowing or blocking specific traffic flows and responding to topology changes such as link failures and recovery.

---

## ⚙️ Setup & Execution Steps

### 1. Clean previous setup
```bash
sudo pkill -f pox
sudo mn -c
2. Start POX controller
cd ~/pox
./pox.py log.level --DEBUG misc.tcd_pox
3. Start Mininet topology
sudo mn --topo linear,3 --controller=remote,ip=127.0.0.1,port=6633
4. Display topology
nodes
net
links
5. Test normal connectivity
pingall
6. Test selective traffic (allowed vs blocked)
h1 ping h2   # allowed
h1 ping h3   # blocked
7. Simulate link failure
link s1 s2 down
pingall
8. Restore network
link s1 s2 up
pingall
9. Verify flow rules
sh ovs-ofctl dump-flows s1
📊 Expected Output
Normal Network: pingall shows 0% packet loss
Allowed Traffic: Communication between h1 and h2 is successful
Blocked Traffic: h1 ping h3 results in 100% packet loss
Link Failure: Bringing link down results in packet loss
Recovery: Restoring the link brings network back to 0% packet loss
Flow Rules: ovs-ofctl dump-flows shows match–action rules installed by the controller

---
