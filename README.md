# Multi-threading vs Multi-processing


Multi-threading: Multithreading is a system in which multiple threads are created of a process for increasing the computing speed of the system. 
In multithreading, many threads of a process are executed simultaneously and process creation in multithreading is done according to economical.

1. In Multithreading, many threads are created of a single process for increasing computing power.
2.	In multithreading, many threads of a process are executed simultaneously.
3.	Multithreading is not classified in any categories.
4.	In Multithreading, process creation is according to economical.
5.	In Multithreading, a common address space is shared by all the threads.


Multi-Processing: Multiprocessing is a system that has more than one or two processors. 
In Multiprocessing, CPUs are added for increasing computing speed of the system. Because of Multiprocessing, There are many processes are executed simultaneously.

1. In Multiprocessing, CPUs are added for increasing computing power.
2.	In Multiprocessing, Many processes are executed simultaneously.	
3.	Multiprocessing are classified into Symmetric and Asymmetric.
4.	In Multiprocessing, Process creation is a time-consuming process.
5.	In Multiprocessing, every process owned a separate address space.



Comparison:
Note that using multithreading for CPU-bound processes might slow down performance due to competing resources that ensure only one thread can
execute at a time, and overhead is incurred in dealing with multiple threads.

On the other hand, multiprocessing can be used for IO-bound processes. However, overhead for managing multiple processes is higher than managing 
multiple threads as illustrated above. You may notice that multiprocessing might lead to higher CPU utilization due to multiple CPU cores being 
used by the program, which is expected
