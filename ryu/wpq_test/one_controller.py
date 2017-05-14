#-*- coding: UTF-8 -*-
from ryu.base import app_manager
from ryu.base.app_manager import lookup_service_brick
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.ofproto import ether
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib.packet import ethernet, arp, packet
from ryu.lib.packet import lldp
from ryu.lib.dpid import dpid_to_str, str_to_dpid
import logging
from ryu.lib import addrconv
from ryu.topology.switches import LLDPPacket
from ryu.lib import ofctl_utils
import struct
from ryu.topology.switches import Switches

class PeiQiaoWang_controller(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PeiQiaoWang_controller, self).__init__(*args, **kwargs)
        self.name = 'first peiqiao app'
        self.sw_module = lookup_service_brick('swithes')
        print "it's init"
        print self.sw_module
        print "ADD=", ofproto_v1_3.OFPFC_ADD

    # @set_ev_cls(ofp_event.EventOFPFeaturesRequest)
    # def switch_features_handle(self, ev):
    #     logging.debug("ing")
    #     msg = ev.msg
    #     datapath = msg.datapath
    #     ofproto = datapath.ofproto
    #     parser = datapath.ofproto_parser
    #     print msg, datapath, ofproto, parser

    #handshake系列

    #OFPFeaturesRequest_由控制器发送

    #OFPSwitchFeatures
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures)
    def switch_switch_feature_handle(self, ev):
        print "go"
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        print msg
        print "datapath=", datapath
        print datapath.id
        print type(datapath.id)
        ofp = datapath.ofproto
        ofp_parser = datapath.ofproto_parser

#LLDP报文格式，DA=0x0180-C200-000E, SA=所需地址，TYPE=0X88CC,Data:LLDPDU
#LLDPDU Chassis ID TLV,(交换机id),PORT ID TLV(端口号),Time To LIVE TLV(TTL),End of LLDPDU TLV

        # dst = lldp.LLDP_MAC_NEAREST_BRIDGE
        # print "dst=", dst
        # src = '00:00:00:00:00:01'
        # dpid = 1
        # port_no = 1
        # e = ethernet.ethernet(dst=dst,
        #                       src=src,
        #                       ethertype=ether.ETH_TYPE_LLDP)
        # p = packet.Packet()
        #
        # tlv_chassis_id = lldp.ChassisID(subtype=lldp.ChassisID.SUB_LOCALLY_ASSIGNED,
        #                                 chassis_id=(LLDPPacket.CHASSIS_ID_FMT %
        #                                             dpid_to_str(dpid)).encode('ascii'))
        #
        # tlv_port_id = lldp.PortID(subtype=lldp.PortID.SUB_PORT_COMPONENT,
        #                           port_id=struct.pack(
        #                               LLDPPacket.PORT_ID_STR,
        #                               port_no))
        #
        # tlv_ttl = lldp.TTL(ttl=120)
        # tlv_end = lldp.End()
        # tlvs = (tlv_chassis_id, tlv_port_id, tlv_ttl, tlv_end)
        # lldp_pkt = lldp.lldp(tlvs)
        # print lldp_pkt
        # print e
        #
        # p.add_protocol(e)
        # p.add_protocol(lldp_pkt)
        # p.serialize()
        #
        # actions = [ofp_parser.OFPActionOutput(port=2)]
        # req = ofp_parser.OFPPacketOut(datapath=datapath, buffer_id=ofp.OFP_NO_BUFFER, in_port=ofp.OFPP_CONTROLLER,
        #                               actions=actions, data=p)
        # print req
        # datapath.send_msg(req)




        print "ok"
        # print "ofp=", ofp
        # print "msg.datapath_id=", msg.datapath_id
        # print "datapath=", datapath
        # print "ofproto=", ofproto
        # print "parser=", parser


        print "OFP_NO_BUFFER=", ofp.OFP_NO_BUFFER
    #Switch Configuration系列

    #OFPSetConfig


    @set_ev_cls(ofp_event.EventOFPPacketIn)
    def packet_in_handle(self, ev):
        print "in"
        msg = ev.msg
        print msg
        # print ofctl_utils.hex_array(msg.data)
        dpid = msg.datapath.id

        # print msg.datapath
        pkt = packet.Packet(msg.data)
        print pkt.protocols

        print dpid
        in_port = msg.match['in_port']


