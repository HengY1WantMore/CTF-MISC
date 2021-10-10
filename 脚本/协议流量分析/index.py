import pyshark

# 过滤回显请求
cap = pyshark.FileCapture('icmp_len_binary.pcap', display_filter="icmp && icmp.type==8")
cap.load_packets()
flag = ''
con1 = ""
con2 = ""

# 因为发现都是观察每一条流量的length值都是32或64
for i in range(0, len(cap)):
    if cap[i].icmp.data_len == '32':
        con1 += '0'
        con2 += '1'
    elif cap[i].icmp.data_len == '64':
        con1 += '1'
        con2 += '0'
print('con1:')
print(con1)
print('con2:')
print(con2)
cap.close()