"""
Real-time network traffic capturing using scapy.all.sniff
"""

from datetime import datetime
from colored import fg, attr
from scapy.all import sniff

class NetSniff:
	def __init__(self, interf="eth0", apply_filter=None, count=0):
		"""
		Args:
			interf (str): the infertace to capture packets on.
			apply_filter (str): apply tcpdump filter to live capture.
			count (int): number of packets to capture, 0=infinite.
		"""
		self._interf = interf
		self._apply_filter = apply_filter
		self._count = count

	@property
	def interf(self):
		return self._interf

	@property
	def apply_filter(self):
		return self._apply_filter
	
	@property
	def count(self):
		return self._count
	
	def prn(self, pkt):
	    """ The print message for every captured packet

	    Args:
	        pkt (scapy.layers.l2.Ether): the packet captured
	    """
	    return (
	    	f"[{str(datetime.now())[11:19]}]" \
	    	f" {pkt[0].src}" \
	    	f" {pkt[0].dst}" \
	    	f" %s{str(pkt[1].payload.name).upper()}%s" \
	    	f" {pkt[1].src}:{pkt[2].sport} %s\u2192%s {pkt[1].dst}:{pkt[2].dport}" \
	    	% (fg(150), attr(0), fg(9), attr(0))
	    )
	def capture(self):
		""" Begin capturing live packets with scapy.all.sniff """
		sniff(
			iface=self.interf, filter=self.apply_filter,
			count=self.count, prn=self.prn
		)
