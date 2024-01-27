-----------------------------------------------------------
 The package provides the Fortran90 version for a number
 of bound constrained problems for global optimization
-----------------------------------------------------------
0- Gunzip and untar the archive in a folder on your computer by
   issuing in a directory of your choice (ex. curdir) the command

   $> tar -zxvf TESTGO.tar.gz

1- At command prompt in curdir execute

   $> ./run_testgo.sh

   and you are done!

   This will run a simple main program on the collection of 74 
   bound constrained global optimization problems and output 
   in file ris.tex the following information:

   column 1 gives the PROBLEM NAME
   column 2 gives the NUMBER OF VARIABLES
   column 3 gives the known global minimum value (f*)
   if problem has <= 4 variables,
      column 4   - 4+ n-1 give the lower bounds on the variables
      column 4+n - 4+2n-1 give the upper bounds on the variables
   otherwise
      column 4 and  5 give the lower bounds of variables 1 and 2
      column 6 and  7 give the lower bounds of variables n-1 and n
      column 8 and  9 give the upper bounds of variables 1 and 2
      column 9 and 10 give the upper bounds of variables n-1 and n

