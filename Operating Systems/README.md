# Operating Systems Internals (OSTEP Study)

Welcome to my operating systems internals laboratory. This directory documents my low-level engineering journey as I work through the foundational textbook **"Operating Systems: Three Easy Pieces" (OSTEP)**. 

My goal is to build a rock-solid understanding of how modern operating system kernels interface with hardware, manage memory, and handle concurrent execution.

## 📚 The Three Easy Pieces

I am breaking my notes, experiments, and code labs down into the three core pillars of OS architecture:

### 1. Virtualization
* **CPU Virtualization:** Process mechanics, Limited Direct Execution (LDE), and scheduling policies.
* **Memory Virtualization:** Address spaces, address translation, paging, Translation Lookaside Buffers (TLBs), and swap space.

### 2. Concurrency
* Thread creation, locks, and condition variables.
* Semaphores and common concurrency bugs (deadlocks, atomicity violations).

### 3. Persistence
* I/O devices and storage internals (Hard disks and SSDs).
* File system organization, directory structures, and crash consistency (journaling/FSCK).

## Tools & Technologies
* **Language:** C (for system calls, pointer manipulation, and architectural experiments)
* **Operating System:** Linux
* **Analysis Tools:** `gcc`, `gdb` (debugging), and `strace` (system call tracking)

##  Progress Directory
* `/Virtualization` — Labs and chapter summaries for CPU and memory management. *(Coming Soon)*
* `/Concurrency` — Threading implementations and multi-threaded synchronization. *(Coming Soon)*
* `/Persistence` — File systems and low-level storage exploration. *(Coming Soon)*

---
*Deep dive initiated: June 2026.*
