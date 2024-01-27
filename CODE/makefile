FC = gfortran
CC = gcc
RM = rm -f

FFLAGS = -O3
#FFLAGS = -g

FUNCT := pippo
..PHONY: funct

EXEC = testgo

OBJS   = main.o $(FUNCT).o

all: exe

exe:  $(OBJS)
	$(FC) -o $(EXEC) $(OBJS)

.SUFFIXES : .f90 .o

.f90.o: $* ; $(FC) $(FFLAGS) -c $*.f90

clean: 
	$(RM) *.o
	$(RM) *.mod
	$(RM) fort.*
	$(RM) *~
	$(RM) best.txt
	$(RM) $(EXEC)

