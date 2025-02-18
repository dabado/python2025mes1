-- comentarios: con doble guion

/*
comentario varias lineas
las que sean
*/

select * from DEPT;
select APELLIDO,oficio from emp ;
select * from DEPT;
select APELLIDO,oficio from emp order by "APELLIDO" asc;
select * from emp order by "APELLIDO" desc ;

select * from emp where 'APELLIDO' <> 'tovar' ;

select * from emp where 'APELLIDO' = 'negro' ;
select * from EMP where DEPT_NO = 10;
select * from EMP ;
select * from EMP where oficio = 'ANALISTA' or oficio = 'DIRECTOR';


select * from EMP where DEPT_NO=10 or DEPT_NO=20 and OFICIO = 'DIRECTOR' order by DEPT_NO;
select * from EMP where OFICIO <> 'VENDEDOR' ;
select * from EMP where not OFICIO = 'VENDEDOR' ;--not prohibido -- 

select * from EMP where OFICIO <> 'VENDEDOR' and SALARIO BETWEEN 31800 and 39000 ;
select * from EMP where SALARIO >= 31800 and SALARIO <= 39000;

select * from EMP where DEPT_NO=10 or DEPT_NO=20 or DEPT_NO=30 or DEPT_NO=50 or DEPT_NO=88;
select * from EMP where DEPT_NO in (10,20,30,50,88);
select * from EMP where DEPT_NO not in (10,20,30);

select * from EMP where OFICIO like '%IRE%' or OFICIO like '%VENDE%';
select * from EMP where APELLIDO like 's%' ;
select * from EMP where APELLIDO like 's%a' ;
select * from EMP where APELLIDO like 's%_a' ;

select * from EMP where APELLIDO like '%a';
select DISTINCT OFICIO  from EMP  ;



select APELLIDO,(SALARIO + COMISION) as TOTALES from EMP;


select APELLIDO,(SALARIO + COMISION) as TOTALES from EMP order by TOTALES  where (SALARIO + COMISION) >= 210000;

--- order by ordena respecto al cursor y where a partir de un campo de la tabla ---

select APELLIDO, OFICIO, SALARIO, COMISION ,(SALARIO + COMISION) as TOTALES from EMP where (SALARIO + COMISION)  > 100000;
select * from EMP order by DEPT_NO , OFICIO;
select * from EMP where FECHA_ALT > '1/1/70' order by emp_no ;




select * from plantilla where TURNO like 'N'; 



select * from DOCTOR ; --- where FUNCION =  ; ---