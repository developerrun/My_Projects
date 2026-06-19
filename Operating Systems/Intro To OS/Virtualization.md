Virtualization:
When OS tends to create an illusion for the running processes, where they have their own private memory where they can either read or write data. 

- The problem that arises is if this virtualization is not implemented, running processes will tend to overwrite the data at a particular address continously


For example:
If process 2345 and process 2348 simulataneously access 0x1000 if process 2345 gets access to the address first and writes the data at that address then process 2348 writes the data the data previously written by process 2345 will be said to be overwritten (if physical hardware is being accessed)
