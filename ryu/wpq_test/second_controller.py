#-*- coding: UTF-8 -*-
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.mac import haddr_to_bin
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types

class PeiQiaoWang_controller(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PeiQiaoWang_controller, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPFeaturesRequest)
    def switch_features_handle(self, ev):
        # logging.debug("ing")
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        print msg, datapath, ofproto, parser

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
        print "msg.port=", msg.ports
        # print "datapath=", datapath

        # ofp = datapath.ofproto
        # ofp_parser = datapath.ofproto_parser
        # e = ethernet.ethernet(dst='00:00:00:00:ff:ff',
        #                       src='08:60:6e:7f:74:e7',
        #                       ethertype=ether.ETH_TYPE_ARP)
        #
        # a = arp.arp(hwtype=1, proto=0x0800, hlen=6, plen=4, opcode=2,
        #             src_mac='08:60:6e:7f:74:e7', src_ip='192.0.2.1',
        #             dst_mac='00:00:00:00:00:00', dst_ip='192.0.2.2')
        # p = packet.Packet()
        # p.add_protocol(e)
        # p.add_protocol(a)
        # p.serialize()
        # #
        # actions = [ofp_parser.OFPActionOutput(port=ofp.OFPP_TABLE)]
        # req = ofp_parser.OFPPacketOut(datapath=datapath, buffer_id=ofp.OFP_NO_BUFFER, in_port=1,
        #                               actions=actions, data=p)
        # datapath.send_msg(req)
        # print "ok"
        # print "ofp=", ofp
        # print "msg.datapath_id=", msg.datapath_id
        # print "datapath=", datapath
        # print "ofproto=", ofproto
        # print "parser=", parser
        # print "OFP_NO_BUFFER=", ofp.OFP_NO_BUFFER
    #Switch Configuration系列

    #OFPSetConfig

    #
    # @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    # def packet_in_handle(self, ev):
    #     print "in"
    #     print "ss"
    #     msg = ev.msg
    #     print msg
        # print utils.hex_array(msg.data)
    #     dpid = msg.datapath.id
    #     in_port = msg.match['in_port']

    #
    # def send_packet_out(self, datapath, buffer_id, in_port):
    #     ofp = datapath.ofproto
    #     ofp_parser = datapath.ofproto_parser
    #
    #     actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD, 0)]
    #     req = ofp_parser.OFPPacketOut(datapath, buffer_id,
    #                                   in_port, actions)
    #     datapath.send_msg(req)
