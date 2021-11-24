import dpkt
import socket
import tabulate

pcap = r'D:/Akoko/Apache/Apache_log/week11_dns.pcap'
open_pcap = dpkt.pcap.Reader(open(pcap, 'rb'))

dns_db = {}
counter = 1

for timestamp, packet in open_pcap:
    ethernet_packet = dpkt.ethernet.Ethernet(packet)
    if type(ethernet_packet.data) is dpkt.ip.IP:
        udp = ethernet_packet.data.data
        if udp.sport == 53 or udp.dport ==53:
            dns = dpkt.dns.DNS(udp.data)
            if dns.opcode == dpkt.dns.DNS_QUERY and dns.qr ==dpkt.dns.DNS_R:
                query_list =[]
                answer_list = []
                for query in dns.qd:
                    if query.type == dpkt.dns.DNS_A:
                        query_list.append(query.name)
                    for answer in dns.an:
                        if answer.type == dpkt.dns.DNS_A:
                            answer_list.append(socket.inet_ntoa(answer.ip))
                        if query_list and answer_list:
                            dns_db[counter] = {}; dns_db[counter]['Query'] = query_list; dns_db[counter]['Answer'] = answer_list
        counter +=1
    
    result_list = []
    for k, v in dns_db.items():
        loop_result = []; loop_result.append(k); loop_result.append(v['Query']); loop_result.append(v['Answer'])
        result_list.append(loop_result)


    print(tabulate.tabulate(result_list, headers=['Packet ID', 'Query', 'Answer']))
