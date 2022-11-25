# VLSM (VLSM Variable Length Subnetting)

### Variable Length Subent mask 
`Example`
Let’s say I want to subnet my `192.168.1.0` network in the most efficient way, let’s take another look at the requirements I just showed you:
-   One subnet for 12 hosts (A).
-   One subnet for 44 hosts (B).
-   One subnet for 2 hosts (C).
-   One subnet for 24 hosts (D).
`Solution`
1) We will start with The biggest subnet first.
	So we will start with subnet B which needs 44 hosts so the smallest suitable subnet is 64.
	`192.168.1.0`
2) We will go to subnet D which needs 32.
	`192.168.1.64`
3) We will go to subnet A which needs 16.
	`192.168.1.96`
4) We will go to subnet C which needs 4.
	`192.168.1.112`

subnet number | network address| first usable ip| last usable ip | broadcast address
---|---|---|---|---
B | 192.168.1.0  | 192.168.1.1 | 192.168.1.62|192.168.1.63
D | 192.168.1.64 | 192.168.1.65|192.168.1.94|192.168.1.95
A | 192.168.1.96 | 192.168.1.97|192.168.1.110|192.168.1.111
C | 192.168.1.112| 192.168.1.113|192.168.1.114|192.168.1.115


Here is a python Application using a **PyQt5** Library to make a UI.
**To be able to run this application in your Computer You have to install the requirements.txt file**

<img src="https://github.com/yahiamostafa/VLSM/blob/main/Screenshot%20from%202022-11-25%2019-57-22.png" alt="Alt text" title="Screenshot from the The Application">

<img src="https://github.com/yahiamostafa/VLSM/blob/main/Screenshot%20from%202022-11-25%2019-57-35.png" alt="Alt text" title="Screenshot from the The Application">
