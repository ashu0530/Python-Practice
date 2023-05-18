#Very simple syntax. Easy to learn for begineers

print("Hello")

#** General Purpose Language:
#       console application and scripts
#       Desktop apps
#       Web apps
#       Game dev
#       ML,AI,DL,BIG DATA, IOT

#** Multiparadigm Support
#       Procedural style programming like C
#       OOPS like java
#       Functional like LISP

#** Portable or platform independent - Programs are typically first compiled into an intermediate code, then the code is run by the interpreter

#** Dynamically Typed: No need to specify value type like in java or c++ which is statically typed
x = 10
y ="geeks"
x = "python"

#** Advantages and Disadvantages - In dynamically typed language the type is assigned at the runtime when your program is running, but in c++ java at compile time.
# - More chances of run time errors
# - Slower

#** Feature - Automatic garbage collection- Don't worry about releasing the memory, Rich libraries

#** Popular using python - Youtube, DropBox, netflix=2019 story, Instragram, GFG use python

################################### Python Standard and implementation #############################################################

#- Cpython : implementation in c programming 
#- Jython : import java files in python
#- Ironpython: compatible with .net
#- PyPy: Cosidered faster


################################## Python Program Execution #######################################################

#Compiler = Compiler is a software takes High level language code C++, python, java, convert to this hll to binary code, byte code or any low level code

#- Cpython:
#   Python Program .pyc ----->Compile----->ByteCode=.pyc------->interpreter executed line by line

# ---> C++ ----> C++ Compiler(windows,linux) ----> Binary code
# ---> Java ---> Java Compiler ----> Byte code -----> Interpreted

#- Why so much steps first compile and interpreted ? Ans = make code platform independent

# Platform - A platform is combination of OS and architecture = Intel+Windows or Linux+Intel arch


################################## Python Programs Platform independence ##############################################################################

# Pythoncode ---> Compiler ---> ByteCode(Platform Independent intermediate code) ----> Interpreterline by line ----> by PVM (Python virtual machine) on linux,windows executed

################################### How Python programs are Executed #########################################################3

# >>> python a.py  #this command does both compilation and interpretation
# >>> python -m py_compile a.py  #Compilation the code not run produce compile file
