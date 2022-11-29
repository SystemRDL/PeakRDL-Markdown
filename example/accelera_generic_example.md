<!---
Markdown description for SystemRDL register map.

Don't override. Generated from:   example/accelera_generic_example.rdl
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
|0x0100|   fifo_port[8]   |                  —                 |
|0x0110|   fifo_port[8]   |                  —                 |
|0x0120|   fifo_port[8]   |                  —                 |
|0x0130|   fifo_port[8]   |                  —                 |
|0x0140|   fifo_port[8]   |                  —                 |
|0x0150|   fifo_port[8]   |                  —                 |
|0x0160|   fifo_port[8]   |                  —                 |
|0x0170|   fifo_port[8]   |                  —                 |
|0x1000|vc_pkt_count[8][2]|                  —                 |
|0x1004|vc_pkt_count[8][2]|                  —                 |
|0x1008|vc_pkt_count[8][2]|                  —                 |
|0x100C|vc_pkt_count[8][2]|                  —                 |
|0x1010|vc_pkt_count[8][2]|                  —                 |
|0x1014|vc_pkt_count[8][2]|                  —                 |
|0x1018|vc_pkt_count[8][2]|                  —                 |
|0x101C|vc_pkt_count[8][2]|                  —                 |
|0x1020|vc_pkt_count[8][2]|                  —                 |
|0x1024|vc_pkt_count[8][2]|                  —                 |
|0x1028|vc_pkt_count[8][2]|                  —                 |
|0x102C|vc_pkt_count[8][2]|                  —                 |
|0x1030|vc_pkt_count[8][2]|                  —                 |
|0x1034|vc_pkt_count[8][2]|                  —                 |
|0x1038|vc_pkt_count[8][2]|                  —                 |
|0x103C|vc_pkt_count[8][2]|                  —                 |
|0x2000|   empty_addrmap  |Empty addrmap with unsupported node.|

### chip_id_reg register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x4

<p>This register cotains the part # and revision # for XYZ ASIC</p>

|Bits|Identifier|Access|  Reset  |Name|
|----|----------|------|---------|----|
|31:4| part_num |   r  |0x1234567|  — |

#### part_num field

<p>This field represents the chips part number</p>

### link_status register

- Absolute Address: 0x4
- Base Offset: 0x4
- Size: 0x4

| Bits|Identifier|Access|Reset|Name|
|-----|----------|------|-----|----|
| 3:0 |   port0  |   r  |  —  |  — |
| 7:4 |   port1  |   r  |  —  |  — |
| 11:8|   port2  |   r  |  —  |  — |
|15:12|   port3  |   r  |  —  |  — |

#### port0 field

<p>Status of a Serdes Link</p>

#### port1 field

<p>Status of a Serdes Link</p>

#### port2 field

<p>Status of a Serdes Link</p>

#### port3 field

<p>Status of a Serdes Link</p>

### myRegInst register

- Absolute Address: 0x10
- Base Offset: 0x10
- Size: 0x4

| Bits|Identifier| Access |Reset|Name|
|-----|----------|--------|-----|----|
| 1:0 |   data0  |rw, rclr| 0x0 |  — |
| 3:2 |   data1  |rw, rclr| 0x1 |  — |
| 5:4 |   data2  |rw, rclr| 0x2 |  — |
| 7:6 |   data3  |rw, rclr| 0x3 |  — |
| 9:8 |   data4  |rw, rclr| 0x0 |  — |
|11:10|   data5  |rw, rclr| 0x1 |  — |
|13:12|   data6  |rw, rclr| 0x2 |  — |
|15:14|   data7  |rw, rclr| 0x3 |  — |
|17:16|   data8  |rw, rclr| 0x0 |  — |
|19:18|   data9  |rw, rclr| 0x1 |  — |
|21:20|  data10  |rw, rclr| 0x2 |  — |
|23:22|  data11  |rw, rclr| 0x3 |  — |
|25:24|  data12  |rw, rclr| 0x0 |  — |
|27:26|  data13  |rw, rclr| 0x1 |  — |
|29:28|  data14  |rw, rclr| 0x2 |  — |
|31:30|  data15  |rw, rclr| 0x3 |  — |

#### data0 field

<p>My example 2bit status field</p>

#### data1 field

<p>My example 2bit status field</p>

#### data2 field

<p>My example 2bit status field</p>

#### data3 field

<p>My example 2bit status field</p>

#### data4 field

<p>My example 2bit status field</p>

#### data5 field

<p>My example 2bit status field</p>

#### data6 field

<p>My example 2bit status field</p>

#### data7 field

<p>My example 2bit status field</p>

#### data8 field

<p>My example 2bit status field</p>

#### data9 field

<p>My example 2bit status field</p>

#### data10 field

<p>My example 2bit status field</p>

#### data11 field

<p>My example 2bit status field</p>

#### data12 field

<p>My example 2bit status field</p>

#### data13 field

<p>My example 2bit status field</p>

#### data14 field

<p>My example 2bit status field</p>

#### data15 field

<p>My example 2bit status field</p>

### spi4_pkt_count register

- Absolute Address: 0x20
- Base Offset: 0x20
- Size: 0x4

| Bits|Identifier| Access |Reset|Name|
|-----|----------|--------|-----|----|
| 15:0|   port1  |rw, rclr|  —  |  — |
|31:16|   port0  |rw, rclr|  —  |  — |

#### port1 field

<p>Number of certain packet type seen</p>

#### port0 field

<p>Number of certain packet type seen</p>

### gige_pkt_count_reg register

- Absolute Address: 0x24
- Base Offset: 0x24
- Size: 0x4

| Bits|Identifier| Access |Reset|Name|
|-----|----------|--------|-----|----|
| 7:0 |   port3  |rw, rclr|  —  |  — |
| 15:8|   port2  |rw, rclr|  —  |  — |
|23:16|   port1  |rw, rclr|  —  |  — |
|31:24|   port0  |rw, rclr|  —  |  — |

#### port3 field

<p>Number of certain packet type seen</p>

#### port2 field

<p>Number of certain packet type seen</p>

#### port1 field

<p>Number of certain packet type seen</p>

#### port0 field

<p>Number of certain packet type seen</p>

## fifo_port register file

- Absolute Address: 0x100
- Base Offset: 0x100
- Size: 0xC
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

|Offset|Identifier|Name|
|------|----------|----|
|  0x0 |   head   |  — |
|  0x4 |   tail   |  — |
|  0x8 |  status  |  — |

### head register

- Absolute Address: 0x100
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### tail register

- Absolute Address: 0x104
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### status register

- Absolute Address: 0x108
- Base Offset: 0x8
- Size: 0x4

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |    full    |  rw  | 0x0 |  — |
|  1 |    empty   |  rw  | 0x1 |  — |
|  4 |almost_empty|  rw  | 0x1 |  — |
|  5 | almost_full|  rw  | 0x0 |  — |

## fifo_port register file

- Absolute Address: 0x110
- Base Offset: 0x100
- Size: 0xC
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

|Offset|Identifier|Name|
|------|----------|----|
|  0x0 |   head   |  — |
|  0x4 |   tail   |  — |
|  0x8 |  status  |  — |

### head register

- Absolute Address: 0x110
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### tail register

- Absolute Address: 0x114
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### status register

- Absolute Address: 0x118
- Base Offset: 0x8
- Size: 0x4

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |    full    |  rw  | 0x0 |  — |
|  1 |    empty   |  rw  | 0x1 |  — |
|  4 |almost_empty|  rw  | 0x1 |  — |
|  5 | almost_full|  rw  | 0x0 |  — |

## fifo_port register file

- Absolute Address: 0x120
- Base Offset: 0x100
- Size: 0xC
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

|Offset|Identifier|Name|
|------|----------|----|
|  0x0 |   head   |  — |
|  0x4 |   tail   |  — |
|  0x8 |  status  |  — |

### head register

- Absolute Address: 0x120
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### tail register

- Absolute Address: 0x124
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### status register

- Absolute Address: 0x128
- Base Offset: 0x8
- Size: 0x4

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |    full    |  rw  | 0x0 |  — |
|  1 |    empty   |  rw  | 0x1 |  — |
|  4 |almost_empty|  rw  | 0x1 |  — |
|  5 | almost_full|  rw  | 0x0 |  — |

## fifo_port register file

- Absolute Address: 0x130
- Base Offset: 0x100
- Size: 0xC
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

|Offset|Identifier|Name|
|------|----------|----|
|  0x0 |   head   |  — |
|  0x4 |   tail   |  — |
|  0x8 |  status  |  — |

### head register

- Absolute Address: 0x130
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### tail register

- Absolute Address: 0x134
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### status register

- Absolute Address: 0x138
- Base Offset: 0x8
- Size: 0x4

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |    full    |  rw  | 0x0 |  — |
|  1 |    empty   |  rw  | 0x1 |  — |
|  4 |almost_empty|  rw  | 0x1 |  — |
|  5 | almost_full|  rw  | 0x0 |  — |

## fifo_port register file

- Absolute Address: 0x140
- Base Offset: 0x100
- Size: 0xC
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

|Offset|Identifier|Name|
|------|----------|----|
|  0x0 |   head   |  — |
|  0x4 |   tail   |  — |
|  0x8 |  status  |  — |

### head register

- Absolute Address: 0x140
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### tail register

- Absolute Address: 0x144
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### status register

- Absolute Address: 0x148
- Base Offset: 0x8
- Size: 0x4

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |    full    |  rw  | 0x0 |  — |
|  1 |    empty   |  rw  | 0x1 |  — |
|  4 |almost_empty|  rw  | 0x1 |  — |
|  5 | almost_full|  rw  | 0x0 |  — |

## fifo_port register file

- Absolute Address: 0x150
- Base Offset: 0x100
- Size: 0xC
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

|Offset|Identifier|Name|
|------|----------|----|
|  0x0 |   head   |  — |
|  0x4 |   tail   |  — |
|  0x8 |  status  |  — |

### head register

- Absolute Address: 0x150
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### tail register

- Absolute Address: 0x154
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### status register

- Absolute Address: 0x158
- Base Offset: 0x8
- Size: 0x4

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |    full    |  rw  | 0x0 |  — |
|  1 |    empty   |  rw  | 0x1 |  — |
|  4 |almost_empty|  rw  | 0x1 |  — |
|  5 | almost_full|  rw  | 0x0 |  — |

## fifo_port register file

- Absolute Address: 0x160
- Base Offset: 0x100
- Size: 0xC
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

|Offset|Identifier|Name|
|------|----------|----|
|  0x0 |   head   |  — |
|  0x4 |   tail   |  — |
|  0x8 |  status  |  — |

### head register

- Absolute Address: 0x160
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### tail register

- Absolute Address: 0x164
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### status register

- Absolute Address: 0x168
- Base Offset: 0x8
- Size: 0x4

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |    full    |  rw  | 0x0 |  — |
|  1 |    empty   |  rw  | 0x1 |  — |
|  4 |almost_empty|  rw  | 0x1 |  — |
|  5 | almost_full|  rw  | 0x0 |  — |

## fifo_port register file

- Absolute Address: 0x170
- Base Offset: 0x100
- Size: 0xC
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

|Offset|Identifier|Name|
|------|----------|----|
|  0x0 |   head   |  — |
|  0x4 |   tail   |  — |
|  0x8 |  status  |  — |

### head register

- Absolute Address: 0x170
- Base Offset: 0x0
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### tail register

- Absolute Address: 0x174
- Base Offset: 0x4
- Size: 0x4

|Bits|Identifier|Access|Reset|Name|
|----|----------|------|-----|----|
|31:0|   data   |  rw  |  —  |  — |

### status register

- Absolute Address: 0x178
- Base Offset: 0x8
- Size: 0x4

|Bits| Identifier |Access|Reset|Name|
|----|------------|------|-----|----|
|  0 |    full    |  rw  | 0x0 |  — |
|  1 |    empty   |  rw  | 0x1 |  — |
|  4 |almost_empty|  rw  | 0x1 |  — |
|  5 | almost_full|  rw  | 0x0 |  — |

### vc_pkt_count register

- Absolute Address: 0x1000
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1004
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1008
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x100C
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1010
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1014
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1018
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x101C
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1020
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1024
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1028
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x102C
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1030
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1034
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x1038
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

### vc_pkt_count register

- Absolute Address: 0x103C
- Base Offset: 0x1000
- Size: 0x4
- Array Dimensions: [8, 2]
- Array Stride: 0x4
- Total Size: 0x40

|Bits|Identifier| Access |Reset|Name|
|----|----------|--------|-----|----|
|30:0| vc_count |rw, rclr| 0x0 |  — |
| 31 |  active  |   rw   | 0x1 |  — |

#### vc_count field

<p>Number of certain packet type seen</p>

#### active field

<p>VC is Active</p>

## empty_addrmap address map

- Absolute Address: 0x2000
- Base Offset: 0x2000
- Size: 0x4

No supported members.

