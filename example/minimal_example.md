<!---
Markdown description for SystemRDL register map.

Don't override. Generated from:   example/minimal_example.rdl
-->

## some_register_map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x8

<p>This address map contains some example registers to show
how RDL can be utilized in various situations.</p>

|Offset| Identifier|                Name                |
|------|-----------|------------------------------------|
|  0x0 |chip_id_reg|This chip part number and revision #|
|  0x4 |   enable  |           Enable register          |

### chip_id_reg

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x4

<p>This register cotains the part # and revision # for XYZ ASIC</p>

|Bits|Identifier|Access|  Reset  |Name|
|----|----------|------|---------|----|
| 3:0|  rev_num |   r  |   0x1   |  — |
|31:4| part_num |   r  |0x1234567|  — |

#### rev_num

<p>This field represents the chips revision number</p>

#### part_num

<p>This field represents the chips part number</p>

### enable

- Absolute Address: 0x4
- Base Offset: 0x4
- Size: 0x4

<p>Toggle the peripheral enable on write</p>

|Bits|Identifier|Access|Reset|     Name    |
|----|----------|------|-----|-------------|
|  0 |  enable  |w, wot|  —  |Enable toggle|
