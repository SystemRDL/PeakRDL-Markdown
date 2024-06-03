<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: some_register_map
  - example/accelera_generic_example.rdl
-->

## some_register_map address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x2004

<p>This address map contains some example registers to show
how RDL can be utilized in various situations.</p>

|Offset|    Identifier    |                Name                |
|------|------------------|------------------------------------|
|0x0000|    chip_id_reg   |This chip part number and revision #|
|0x0004|    link_status   |                  —                 |
|0x0010|     myRegInst    |                  —                 |
|0x0020|  spi4_pkt_count  |                  —                 |
|0x0024|gige_pkt_count_reg|                  —                 |
|0x0100|   fifo_port[0]   |                  —                 |
|0x0110|   fifo_port[1]   |                  —                 |
|0x0120|   fifo_port[2]   |                  —                 |
|0x0130|   fifo_port[3]   |                  —                 |
|0x0140|   fifo_port[4]   |                  —                 |
|0x0150|   fifo_port[5]   |                  —                 |
|0x0160|   fifo_port[6]   |                  —                 |
|0x0170|   fifo_port[7]   |                  —                 |
|0x1000|vc_pkt_count[0][0]|                  —                 |
|0x1004|vc_pkt_count[0][1]|                  —                 |
|0x1008|vc_pkt_count[1][0]|                  —                 |
|0x100C|vc_pkt_count[1][1]|                  —                 |
|0x1010|vc_pkt_count[2][0]|                  —                 |
|0x1014|vc_pkt_count[2][1]|                  —                 |
|0x1018|vc_pkt_count[3][0]|                  —                 |
|0x101C|vc_pkt_count[3][1]|                  —                 |
|0x1020|vc_pkt_count[4][0]|                  —                 |
|0x1024|vc_pkt_count[4][1]|                  —                 |
|0x1028|vc_pkt_count[5][0]|                  —                 |
|0x102C|vc_pkt_count[5][1]|                  —                 |
|0x1030|vc_pkt_count[6][0]|                  —                 |
|0x1034|vc_pkt_count[6][1]|                  —                 |
|0x1038|vc_pkt_count[7][0]|                  —                 |
|0x103C|vc_pkt_count[7][1]|                  —                 |
|0x2000|   empty_addrmap  |Empty addrmap with unsupported node.|
