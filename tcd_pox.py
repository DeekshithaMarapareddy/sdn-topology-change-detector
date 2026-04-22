from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.ipv4 import ipv4

log = core.getLogger()

mac_table = {}

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.dpid
    in_port = event.port

    mac_table.setdefault(dpid, {})
    mac_table[dpid][packet.src] = in_port

    ip_packet = packet.find('ipv4')

    # 🚫 BLOCK h1 → h3
    if ip_packet:
        src_ip = str(ip_packet.srcip)
        dst_ip = str(ip_packet.dstip)

        if src_ip == "10.0.0.1" and dst_ip == "10.0.0.3":
            log.info("🚫 BLOCKING h1 → h3 (ONLY DROP RULE)")

            drop = of.ofp_flow_mod()
            drop.priority = 200   # VERY IMPORTANT (higher than forwarding)

            drop.match.dl_type = 0x0800
            drop.match.nw_src = ip_packet.srcip
            drop.match.nw_dst = ip_packet.dstip

            # No action → DROP
            event.connection.send(drop)

            return  # 🔥 STOP HERE (DO NOT FORWARD)

    # ✅ NORMAL FORWARDING (only for allowed traffic)
    if packet.dst in mac_table[dpid]:
        out_port = mac_table[dpid][packet.dst]

        flow = of.ofp_flow_mod()
        flow.priority = 10
        flow.match.dl_dst = packet.dst
        flow.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(flow)

        out = of.ofp_packet_out()
        out.data = event.ofp
        out.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(out)

    else:
        out = of.ofp_packet_out()
        out.data = event.ofp
        out.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(out)


def launch():
    log.info("🚀 FINAL CONTROLLER (NO CONFLICT)")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
