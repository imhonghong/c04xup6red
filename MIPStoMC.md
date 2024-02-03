# MIPStoMC

### MIPS to machine code converter

some function is included:

- decimal to 5bits binary number (unsigned)
- decimal to 16bits binary number (unsigned)
- decimal to 16bits binary number (signed)

<aside>
📌 Since I’m a beginner of python, these functions are my naive approach, which means it may cause more computing time. If you’re good at py, using the library built in py may be a better solution.

</aside>

### Guide for user

- only ***$1,$2,…$31*** are valid register names,
***$v0,$zero,$t0***… are invalid, which may cause wrong result
- case of commands can be ignored
- you only need to give the input file path in the main function,
since Window’s file path contains backslash,
so I use raw-string in python to solve this problem
- the function will generate a txt file automatically in the same direction of input file,
and the output file name is suffixed with a ***_MC*** compared to the input file name.
- Besides the output file, terminal will print the machine codes with spaces (to separate different part of machine codes, such as op-code, rd,rs,immediate value…), which have more readability than the 32bits machine code without spaces.
- jump command will print the target in decimal directly

### Example

add $1,$2,$6 ---> valid

SUB $2 $6 $4 ---> valid, case is ignored

and $r1,$r2,$r3 ->invalid, only digit type is accepted

### Reference

All data are from url: [opencores.org](https://opencores.org/projects/plasma/opcodes)