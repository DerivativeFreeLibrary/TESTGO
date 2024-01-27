!============================================================================================
!    TESTGO - A collection of bound constrained problems for global optimization.  
!    by G.Liuzzi, S.Lucidi, V.Piccialli (see Ref. below)
!
!    Copyright (C) 2014  G.Liuzzi, S.Lucidi, V.Piccialli
!
!    This program is free software: you can redistribute it and/or modify
!    it under the terms of the GNU General Public License as published by
!    the Free Software Foundation, either version 3 of the License, or
!    (at your option) any later version.
!
!    This program is distributed in the hope that it will be useful,
!    but WITHOUT ANY WARRANTY; without even the implied warranty of
!    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!    GNU General Public License for more details.
!
!    You should have received a copy of the GNU General Public License
!    along with this program.  If not, see <http://www.gnu.org/licenses/>.
!
!    G.Liuzzi, S.Lucidi, V.Piccialli: Exploiting derivative-free local searches in 
!    DIRECT-type algorithms for global optimization. 
!    Computational Optimization and Applications, to appear (2014)
!
!==============================================================================================
module m_testCE
	double precision, allocatable:: M_griew(:,:)
end module m_testCE

program main
	use m_testCE
	implicit none
	include 'parametri.fi'

	integer		:: n, i, j
	character*40		:: nomefun
	character ( len = 64)	:: file_input
	real*8			:: lb(nn), ub(nn), x(nn)
	real*8			:: fglob, f, rr
	real*8			:: c
	external		:: funct, grad
 
	n = nn

	write(*,*) 'n=',n

	!----------------------------------------
	! Set bounds, nomefun and other problem
	! dependent parameters
	!----------------------------------------
	open(2,file='nomefun',status='OLD')
	read(2,100) nomefun
	close(2)
 	write(*,*) nomefun
	if (nomefun==' Griewrot2') then
		allocate(M_griew(n,n))
		if (n ==2) then
			file_input = 'matrixM_2.txt'
			call read_M(n,file_input)
		endif
		if (n ==10) then
			file_input = 'matrixM_10.txt'
			call read_M(n,file_input)
		endif
		if (n ==30) then
			file_input = 'matrixM_30.txt'
			call read_M(n,file_input)
		endif
		if (n ==50) then
			file_input = 'matrixM_50.txt'
			call read_M(n,file_input)

		endif
		if ((n.ne.10).and.(n.ne. 2).and.(n.ne.30).and.(n.ne.50)) then
			c = 3.0d0
			write(*,*) c
			call rot_matrix(n,c)
			do i=1,n
				do j=1,n
					call random_number(rr)
					M_griew(i,j)=M_griew(i,j)*(1.0d0+0.3d0*dble(rr))
				enddo
			enddo
		endif
	endif
	if (nomefun ==' ShiftRotRastr') then
		allocate(M_griew(n,n))
		if (n ==2) then
			file_input = 'matrixM_Rastr_2.txt'
			call read_M(n,file_input)
		endif
		if (n ==10) then
			file_input = 'matrixM_Rastr_10.txt'
			call read_M(n,file_input)
		endif
		if (n ==30) then
			file_input = 'matrixM_Rastr_30.txt'
			call read_M(n,file_input)
		endif
		if (n ==50) then
			file_input = 'matrixM_Rastr_50.txt'
			call read_M(n,file_input)
		endif

	endif
	open(2,file='PROBDAT.d',status='OLD')
	read(2,*) fglob

	do i = 1,n
		read(2,*) lb(i), ub(i)
	enddo
	close(2)

	x = (ub+lb)/2.d0

	call funct(n,x,f)

	write(*,*) ' fglob = ',fglob
	write(*,*) '     f = ',f
	write(*,*) '     x = ',x
	write(*,*) '    ub = ',ub
	write(*,*) '    lb = ',lb

	write(2,200) nomefun
	write(2,210) n
	write(2,220) fglob
	if(n <= 4) then
		do i = 1,n
			write(2,230) lb(i)
		enddo
		write(2,240)
		do i = 1,n
			write(2,230) ub(i)
		enddo
		write(2,250)
	else
		do i = 1,2
			write(2,230) lb(i)
		enddo
		write(2,260)
		do i = n-1,n
			write(2,230) lb(i)
		enddo
		write(2,240)
		do i = 1,2
			write(2,230) ub(i)
		enddo
		write(2,260)
		do i = n-1,n
			write(2,230) ub(i)
		enddo
		write(2,250)
	endif

100 	FORMAT(a40)
200 	FORMAT(a20,' & ',$)
210	FORMAT(i4,' & ',$)
220	FORMAT(es16.8,' & ',$)
230	FORMAT(es10.2,' ',$)
240	FORMAT('& ',$)
250	FORMAT(' \\\hline')
260	FORMAT('... ',$)

end program main


subroutine rot_matrix(n,c)

use m_testCE
implicit none

integer ::i,j,n, seed(12), info
double precision:: A(n,n),rr, tau(n), P(n,n), Q1(n,n), &
 Q(n,n), Q2(n,n), v(n,1), Id(n,n), u(n), c, const
double precision:: work(2*n)
real r

seed(1) = 1967408543         
seed(2) = 499
call random_seed(put=seed)

Id=0.0d0
do i=1,n

	Id(i,i) = 1.0d0

enddo

do i=1,n
	do j=1,n
		call random_number(r)
		rr=dble(r)
		A(i,j)=-1.0d0+rr*2.0d0
	enddo
enddo


!CALL DGEQRF(n,n,A,n, tau,work,2*n,info )


P=Id
do i=1,n
	v = 0.0d0
	v(i,1) = 1.0d0
	v(i+1:n,1) = A(i+1:n,i)
	Q1 = P
	Q2 = Id-tau(i)*matmul(v,transpose(v)) 
	P = MATMUL(Q1,Q2)
	
enddo




do i=1,n
	do j=1,n
		call random_number(r)
		rr=dble(r)
		A(i,j)=-1.0d0+rr*2.0d0
	enddo
enddo


!CALL DGEQRF(n,n,A,n, tau,work,2*n,info )

Q = Id
do i=1,n
	v = 0.0d0
	v(i,1) = 1.0d0
	v(i+1:n,1) = A(i+1:n,i)
	Q1 = Q
	Q2 = Id-tau(i)*matmul(v,transpose(v)) 
	Q = MATMUL(Q1,Q2)

enddo


do i = 1,n
	call random_number(r)
	rr=dble(r)
	v(i,1) = rr

enddo
const = (maxval(v(:,1))-minval(v(:,1)))

do i=1,n
	u(i)=c*( (v(i,1)-minval(v(:,1)) )/const)
enddo



do i = 1,n

	Id(i,i) = u(i)

enddo

M_griew=matmul(matmul(P,Id),Q);

!do i=1,n

!	write(*,*)M_griew(i,:)
!	pause


!enddo


return


end subroutine rot_matrix

subroutine read_M(n,file_input)

use m_testCE
implicit none

integer::i, j, icheck,n
character ( len = 64)			::file_input


OPEN(unit=10, FILE=file_input, STATUS='OLD', IOSTAT=ICHECK)
!write(*,*)'n = ',n
do i=1,n

	READ(10,*) (M_griew(i,j),j=1,n)
!	write(*,*)M_griew(i,:)
!	pause

enddo

close(10)

!WRITE(*,*) M_griew
!pause

end subroutine read_M

