# 计算机体系结构

早期的软件编写是直接面向硬件系统的, 当时的软硬件紧密耦合.
IBM在 System/360中引入了ISA的概念, 软件人员可以面向ISA进行开发.
ISA描述了了编程时所需要的抽象机器, 而不是其具体实现.
ISA包括了一套指令集和寄存器.

## 处理器系统层次

ISA将软硬件解耦, 处理器的外部呈现和内部实现可以分离.

- 指令集体系结构 / Architecture
- 处理器微架构 / Microarchitecture
- 物理实现(工艺实现)

| 指令集 | 微架构       | 处理器                                  |
| ------ | ------------ | --------------------------------------- |
| x86    | P6           | 奔腾2/奔腾3 Pentium II/III, Pentium Pro |
|        | NetBurst     | 奔腾4 Pentimu 4, 志强 Xeon              |
| ARMv7  | ARMCortex-A8 | TI OMAP 3430, SamsungStringPC110        |

## 指令集的发展

- CISC 复杂指令集计算机
- RISC 精简指令集计算机
- 后RISC
  - Pentium Pro 所采用的P6微架构中, 将x86的CISC解码为类似RISC的微操作

五种常见的指令集:

- x86

- ARM

- MIPS

- Power

- C6000

## 指令集架构 Instruction Set Architecture

四种主要ISA:Stack,Accumulator,Register-Memory,Load-Store.

现代的处理器多为Reg-Mem或者Load-Store的

- Stack

似乎已经没有流行的硬件.这种结构对寄存器没有特别的要求.在各种高级语言虚拟机(HLL VM)中,非常地流行.

- Load-Store

可以肯定它是一个RISC处理器,那么它必有pipeline.如经典的MIPS的5段流水线和ARM的3段流水线.

### 指令集的实现

## 来源

整理自:

- [面试宝典3：计算机体系结构](https://csbabel.wordpress.com/2010/10/31/interviewbible-3-computer-architecture/amp/?__twitter_impression=true)
- 大话处理器