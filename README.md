Find avoid hook
===========

This script is made for noobs like me, and the idea behind is simple, we want some code to be executed, avoid some others, and at least, hook some imported methods.
Currently hooks plt methods only for ELF i386, x86_64, ARM

Installation
--------------------------

I have tested building in Ubuntu 18.04

Install angr from pip
``` python -m pip install angr ```


Using
-------------------------

Please have a look at the fahook.example method, and if you want to rebuild test1 by yourself, then launch:

``` ./buildTest.sh <arm|x86|x64> ```


